#!/usr/bin/env python3
"""Finite checks of collective mixed-program reflection compilation.

Checks matrix moments and evaluates Stinespring-derived diamond upper formulas;
global normalized-Choi trace errors test a maximally entangled input. These finite
checks do not prove the all-dimension theorem or establish novelty.
"""
import argparse
import json
import math
import pathlib
import numpy as np
import scipy
from scipy.linalg import expm

HERE = pathlib.Path(__file__).resolve().parent
RNG = np.random.default_rng(113207)


def swap_matrix(d, count, a, b):
    dim = d ** count
    out = np.zeros((dim, dim), complex)
    for j in range(dim):
        digits = list(np.unravel_index(j, (d,) * count))
        digits[a], digits[b] = digits[b], digits[a]
        i = np.ravel_multi_index(tuple(digits), (d,) * count)
        out[i, j] = 1
    return out


def embed_local(A, count, index):
    result = np.ones((1, 1), complex)
    for j in range(count):
        result = np.kron(result, A if j == index else np.eye(len(A)))
    return result


def opnorm(A):
    return float(np.linalg.norm(A, 2))


def tensor_power(A, count):
    out = np.ones((1, 1), complex)
    for _ in range(count):
        out = np.kron(out, A)
    return out


def check_converse_geometry():
    """Check the physical rotated supports and amplified output states."""
    rows = []
    for r, k, m in ((1, 1, 2), (1, 3, 3), (2, 2, 2), (3, 2, 4)):
        d = r + 1
        theta = math.pi / (4 * k * m)
        basis = np.eye(d, dtype=complex)
        P0 = basis[:, :r] @ basis[:, :r].conj().T
        rotated = math.cos(theta) * basis[:, 0] + math.sin(theta) * basis[:, r]
        Pt = P0 - np.outer(basis[:, 0], basis[:, 0].conj())
        Pt += np.outer(rotated, rotated.conj())
        root0 = P0 / math.sqrt(r)
        fidelity_matrix = root0 @ (Pt / r) @ root0
        eigenvalues = np.linalg.eigvalsh(fidelity_matrix)
        fidelity = float(np.sqrt(np.maximum(eigenvalues, 0)).sum())
        expected = (r - 1 + math.cos(theta)) / r
        plus = (basis[:, 0] + 1j * basis[:, r]) / math.sqrt(2)
        minus = (basis[:, 0] - 1j * basis[:, r]) / math.sqrt(2)
        vp = tensor_power(plus[:, None], k).reshape(-1)
        vm = tensor_power(minus[:, None], k).reshape(-1)
        initial = (vp + vm) / math.sqrt(2)
        R0, Rt = np.eye(d) - 2 * P0, np.eye(d) - 2 * Pt
        relative = tensor_power(R0 @ Rt, k)
        output = np.linalg.matrix_power(relative, m) @ initial
        overlap = float(abs(np.vdot(initial, output)))
        assert abs(fidelity - expected) < 2e-12
        assert overlap < 2e-12
        rows.append({"r": r, "k": k, "m": m, "theta": theta,
                     "root_fidelity": fidelity, "root_fidelity_formula": expected,
                     "ideal_output_overlap": overlap})
    return rows


def trace_norm_hermitian(A):
    return float(np.abs(np.linalg.eigvalsh((A + A.conj().T) / 2)).sum())


def choi_from_super(S, D):
    # S uses column vectorization; Choi tensor order is input then output.
    return S.reshape(D, D, D, D, order="F").transpose(2, 0, 3, 1).reshape(D * D, D * D)


def program_moment(A, eigenvectors, r, D):
    result = np.zeros((D, D), complex)
    for a in range(r):
        V = np.kron(eigenvectors[:, [a]], np.eye(D))
        result += V.conj().T @ A @ V / r
    return result


def channel_from_unitary(U, eigenvectors, r, d, D):
    S = np.zeros((D * D, D * D), complex)
    for a in range(r):
        V = np.kron(eigenvectors[:, [a]], np.eye(D))
        UV = U @ V
        for b in range(d):
            K = UV[b * D:(b + 1) * D, :] / math.sqrt(r)
            S += np.kron(K.conj(), K)
    return S


def strang_sweep(swaps, delta):
    dim = len(swaps[0])
    V = np.eye(dim, dtype=complex)
    # Execute half steps on 1,...,k-1, then full k, then reverse half steps.
    order = [(j, delta / 2) for j in range(len(swaps) - 1)]
    order += [(len(swaps) - 1, delta)]
    order += [(j, delta / 2) for j in reversed(range(len(swaps) - 1))]
    for j, angle in order:
        W = math.cos(angle) * np.eye(dim) - 1j * math.sin(angle) * swaps[j]
        V = W @ V
    return V


def choi_bounds(Sdiff, D):
    J = choi_from_super(Sdiff, D)
    J = (J + J.conj().T) / 2
    vals, vecs = np.linalg.eigh(J)
    absJ = (vecs * np.abs(vals)) @ vecs.conj().T
    # Feasible dual bound ||Tr_output |J|||_infinity.
    partial = np.trace(absJ.reshape(D, D, D, D), axis1=1, axis2=3)
    return {
        "max_entangled_unhalved_trace_error": float(np.abs(vals).sum() / D),
        "choi_dual_diamond_upper": opnorm(partial),
    }


def run_case(d, r, k):
    D = d ** k
    z = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    Q, _ = np.linalg.qr(z)
    P = Q[:, :r] @ Q[:, :r].conj().T
    rho = P / r
    swaps = [swap_matrix(d, k + 1, 0, j + 1) for j in range(k)]
    H = sum(swaps)
    h = program_moment(H, Q, r, D)
    M = program_moment(H @ H, Q, r, D)
    h_formula = sum(embed_local(rho, k, j) for j in range(k))
    M_formula = k * np.eye(D, dtype=complex)
    for i in range(k):
        for j in range(i + 1, k):
            F = swap_matrix(d, k, i, j)
            M_formula += (embed_local(rho, k, i) + embed_local(rho, k, j)) @ F
    variance = M - h @ h
    v = opnorm(variance)
    v_formula = max(k + (k - 1) * m / r - m * m / (r * r) for m in range(k + 1))
    R = np.eye(d) - 2 * P
    target = np.ones((1, 1), complex)
    for _ in range(k):
        target = np.kron(target, R)
    target_S = np.kron(target.conj(), target)
    identity_J = choi_from_super(np.eye(D * D), D)
    vecI = np.eye(D).reshape(D * D, order="F")
    assert opnorm(identity_J - np.outer(vecI, vecI)) < 1e-10

    local = []
    for delta in (0.03, 0.12, 0.4):
        U = expm(-1j * delta * H)
        ideal = expm(-1j * delta * h)
        K0 = program_moment(U, Q, r, D)
        compression = opnorm(K0 - ideal)
        leakage = opnorm(np.eye(D) - K0.conj().T @ K0)
        certified_upper = 2 * compression + leakage
        S = channel_from_unitary(U, Q, r, d, D)
        bounds = choi_bounds(S - np.kron(ideal.conj(), ideal), D)
        local.append({
            "delta": delta,
            "compression_error": compression,
            "compression_bound_delta2v_over2": delta * delta * v / 2,
            "leakage_effect_norm": leakage,
            "leakage_bound_delta2v": delta * delta * v,
            "certified_diamond_upper_from_compression": certified_upper,
            "universal_bound_2delta2v": 2 * delta * delta * v,
            **bounds,
        })
        assert compression <= delta * delta * v / 2 + 2e-12
        assert leakage <= delta * delta * v + 2e-12
        assert bounds["max_entangled_unhalved_trace_error"] <= certified_upper + 2e-12

    global_runs = []
    for N in (32, 128, 512):
        delta = math.pi * r / N
        U = expm(-1j * delta * H)
        V = strang_sweep(swaps, delta)
        S = channel_from_unitary(U, Q, r, d, D)
        SS = channel_from_unitary(V, Q, r, d, D)
        exact_bounds = choi_bounds(np.linalg.matrix_power(S, N) - target_S, D)
        strang_bounds = choi_bounds(np.linalg.matrix_power(SS, N) - target_S, D)
        global_runs.append({
            "N": N,
            "delta": delta,
            "collective": exact_bounds,
            "strang": strang_bounds,
            "universal_collective_diamond_bound": 2 * math.pi ** 2 * r * r * v / N,
            "one_sweep_operator_error": opnorm(U - V),
            "strang_error_div_k3delta3": opnorm(U - V) / (k ** 3 * delta ** 3),
            "global_extra_diamond_bound_from_sweep": 2 * N * opnorm(U - V),
        })
        assert exact_bounds["max_entangled_unhalved_trace_error"] <= 2 * math.pi ** 2 * r * r * v / N + 1e-10
        assert strang_bounds["max_entangled_unhalved_trace_error"] <= exact_bounds["choi_dual_diamond_upper"] + 2 * N * opnorm(U - V) + 1e-10

    result = {
        "d": d, "r": r, "k": k,
        "first_moment_residual": opnorm(h - h_formula),
        "second_moment_residual": opnorm(M - M_formula),
        "M_norm": opnorm(M),
        "M_norm_formula": k + k * (k - 1) / r,
        "variance_norm": v,
        "variance_norm_formula": v_formula,
        "local_checks": local,
        "global_runs": global_runs,
    }
    assert result["first_moment_residual"] < 2e-12
    assert result["second_moment_residual"] < 3e-12
    assert abs(opnorm(M) - result["M_norm_formula"]) < 5e-12
    assert abs(v - v_formula) < 5e-12
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=pathlib.Path, default=HERE / "results.json",
                        help="Write the finite-matrix report to this JSON file.")
    args = parser.parse_args()
    cases = [(2, 1, 1), (2, 1, 2), (2, 1, 3), (3, 1, 1), (3, 1, 2), (3, 2, 1), (3, 2, 2)]
    results = [run_case(*case) for case in cases]
    converse = check_converse_geometry()
    report = {
        "scope": "Seven small instances; random complex source orientations; exact dense matrices; no SDP solver available.",
        "error_convention": "Unhalved diamond/trace norms.",
        "numpy": np.__version__, "scipy": scipy.__version__,
        "seed": 113207,
        "status": "passed",
        "results": results,
        "converse_geometry": converse,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print("PASS: 7 cases; moment identities, exact variance, 21 local compression/leakage bounds, and 21 global batch runs.")
    print("No diamond SDP or interval arithmetic was used. Valid Choi upper formulas are evaluated numerically; Choi trace error probes a maximally entangled input.")
    print("PASS: four rotated-support fidelity and amplified-orthogonality checks.")
    print("d r k | max M residual | variance | N=32,128,512 global Choi trace errors (collective / Strang)")
    for x in results:
        errors = [f"{v['collective']['max_entangled_unhalved_trace_error']:.5g}/{v['strang']['max_entangled_unhalved_trace_error']:.5g}" for v in x["global_runs"]]
        print(x["d"], x["r"], x["k"], f"{x['second_moment_residual']:.2e}", f"{x['variance_norm']:.8g}", ", ".join(errors))


if __name__ == "__main__":
    main()

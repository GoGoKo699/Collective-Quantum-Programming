#!/usr/bin/env python3
"""Finite matrix checks for the ordinary-reflection classification reduction.

The universal claims are analytic. These checks use exact finite-dimensional
unitary routing, including a maximally entangled input and a reference, rather
than replacing the ordinary channel by a controlled unknown oracle.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

RNG = np.random.default_rng(20261108)
TOL = 2e-11


def random_projector(dim: int, rank: int) -> np.ndarray:
    z = RNG.normal(size=(dim, rank)) + 1j * RNG.normal(size=(dim, rank))
    u, _ = np.linalg.qr(z)
    return u @ u.conj().T


def apply_axis(state: np.ndarray, op: np.ndarray, axis: int) -> np.ndarray:
    return np.moveaxis(np.tensordot(op, state, axes=(1, axis)), 0, axis)


def insert_known(psi: np.ndarray, d: int, k: int, a: int) -> np.ndarray:
    # Order: C, T_1,...,T_k, B, Z. B and T_2,...,T_k start in |a>.
    out = np.zeros((2,) + (d,) * k + (d, psi.shape[-1]), complex)
    index = (slice(None), slice(None)) + (a,) * (k - 1) + (a, slice(None))
    out[index] = psi
    return out


def route(state: np.ndarray, reflection: np.ndarray, k: int, lam: int) -> np.ndarray:
    # On C=0, route the unknown test to B and put known |a> in T_1.
    out = state.copy()
    out[0] = np.swapaxes(out[0], 0, k)
    # Exactly one ordinary R^{tensor k} invocation.
    for j in range(1, k + 1):
        out = apply_axis(out, reflection, j)
    restored = out.copy()
    restored[0] = np.swapaxes(out[0], 0, k)
    # Known phase correction diag(lam,1), no controlled unknown operation.
    restored[0] *= lam
    return restored


def effect_for_route(reflection: np.ndarray, k: int, a: int, lam: int) -> np.ndarray:
    d = len(reflection)
    columns = []
    for j in range(d):
        psi = np.zeros((2, d, 1), complex)
        psi[:, j, 0] = 1 / np.sqrt(2)
        y = route(insert_known(psi, d, k, a), reflection, k, lam)
        hadamard = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
        y = apply_axis(y, hadamard, 0)
        columns.append(y[1].reshape(-1))
    kraus_stack = np.stack(columns, axis=1)
    return kraus_stack.conj().T @ kraus_stack


def one_case(name: str, projector: np.ndarray, active: np.ndarray,
             q: np.ndarray, a: int, lam: int, k: int) -> dict:
    d = len(projector)
    reflection = np.eye(d) - 2 * projector
    a_vec = np.eye(d)[:, a]
    eig_residual = np.linalg.norm(reflection @ a_vec - lam * a_vec)
    # Full maximally entangled reference for C tensor T_1, of dimension 2d.
    psi = np.zeros((2, d, 2 * d), complex)
    for c in range(2):
        for j in range(d):
            psi[c, j, c * d + j] = 1 / np.sqrt(2 * d)
    actual = route(insert_known(psi, d, k, a), reflection, k, lam)
    wanted = psi.copy()
    wanted[1] = reflection @ wanted[1]
    expected = (lam ** (k - 1)) * insert_known(wanted, d, k, a)
    reference_residual = np.linalg.norm(actual - expected)

    # A second reference-entangled random input tests coherent control too.
    rand = RNG.normal(size=psi.shape) + 1j * RNG.normal(size=psi.shape)
    rand /= np.linalg.norm(rand)
    rand_wanted = rand.copy()
    rand_wanted[1] = reflection @ rand_wanted[1]
    random_residual = np.linalg.norm(
        route(insert_known(rand, d, k, a), reflection, k, lam)
        - lam ** (k - 1) * insert_known(rand_wanted, d, k, a))

    m_ideal = active.conj().T @ effect_for_route(reflection, k, a, lam) @ active
    ideal_effect_residual = np.linalg.norm(m_ideal - q, ord=2)

    # A diagnostic noise channel: opposite active reflection, with the SAME
    # known eigenphase on |a>. Its ordinary channel is maximally distant.
    # This is an error-accounting fixture, not a claimed specimen processor.
    wrong_projector = projector + active @ (np.eye(len(q)) - 2 * q) @ active.conj().T
    wrong_reflection = np.eye(d) - 2 * wrong_projector
    p = 0.037
    eps = 2 * p  # Unhalved diamond distance, exactly, by the witness below.
    m_wrong = active.conj().T @ effect_for_route(wrong_reflection, k, a, lam) @ active
    m_noisy = (1 - p) * m_ideal + p * m_wrong
    m_expected = (1 - p) * q + p * (np.eye(len(q)) - q)
    noisy_effect_residual = np.linalg.norm(m_noisy - m_expected, ord=2)
    operator_error = np.linalg.norm(m_noisy - q, ord=2)
    # |a> and any active basis vector see opposite relative phases.
    witness = (a_vec + active[:, 0]) / np.sqrt(2)
    overlap = np.vdot(reflection @ witness, wrong_reflection @ witness)
    witness_distance = 2 * p * np.sqrt(max(0.0, 1 - abs(overlap) ** 2))
    dc = len(q)
    rank = int(round(np.trace(q).real))
    contrast = (1 - rank / dc) / 2
    risk = (np.trace((q / rank) @ (np.eye(dc) - m_noisy))
            + np.trace(m_noisy) / dc).real / 2
    oracle_risk = rank / (2 * dc)
    excess = risk - oracle_risk
    contrast_identity_residual = abs(excess - contrast * eps)
    checks = [eig_residual, reference_residual, random_residual,
              ideal_effect_residual, noisy_effect_residual,
              abs(operator_error - eps / 2),
              abs(witness_distance - eps), contrast_identity_residual]
    if max(checks) > TOL:
        raise AssertionError((name, k, checks))
    return {
        "case": name, "program_dimension": d,
        "program_rank": int(round(np.trace(projector).real)),
        "classification_dimension": dc, "classification_rank": rank,
        "batch_size": k, "known_eigenvalue": lam,
        "reference_dimension": 2 * d,
        "known_eigenvector_residual": float(eig_residual),
        "full_choi_routing_residual": float(reference_residual),
        "random_entangled_routing_residual": float(random_residual),
        "ideal_effect_residual": float(ideal_effect_residual),
        "noisy_effect_residual": float(noisy_effect_residual),
        "unhalved_diamond_error": eps,
        "diamond_witness_trace_norm": float(witness_distance),
        "effect_operator_error": float(operator_error),
        "classification_contrast": float(contrast),
        "classification_excess_risk": float(excess),
        "contrast_normalized_excess": float(excess / contrast),
        "contrast_bound_saturation_residual": float(contrast_identity_residual),
        "passed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("transfer_results.json"),
                        help="write the actual matrix diagnostics as JSON")
    arguments = parser.parse_args()
    cases = []
    source_checks = []
    flag_checks = []
    # Pure rank, smallest occupied endpoint, and high rank with small contrast.
    # All Q ranks are one below their own dimension. In the filled family this
    # makes the programming rank exactly D-1, the vacuum route's missing case.
    for dc, s in ((2, 1), (3, 2), (5, 4)):
        q = random_projector(dc, s)
        dimension = dc + 1
        active = np.eye(dimension)[:, :dc]
        vac_p = active @ q @ active.conj().T
        filled_p = vac_p.copy()
        filled_p[dc, dc] = 1
        flag_active = np.eye(2 * dc)[:, dc:]
        flag_p = flag_active @ q @ flag_active.conj().T
        flag_reflection = np.eye(2 * dc) - 2 * flag_p
        direct_flag_target = np.zeros((2 * dc, 2 * dc), complex)
        direct_flag_target[:dc, :dc] = np.eye(dc)
        direct_flag_target[dc:, dc:] = np.eye(dc) - 2 * q
        flag_residual = np.linalg.norm(flag_reflection - direct_flag_target, ord=2)
        if flag_residual > TOL:
            raise AssertionError("Direct flagged controlled-reflection identity failed")
        flag_checks.append({"classification_dimension": dc,
                            "classification_rank": s,
                            "program_dimension": 2 * dc,
                            "direct_control_identity_residual": float(flag_residual)})
        for k in (1, 2, 3):
            cases.append(one_case("known_vacuum", vac_p, active, q, dc, 1, k))
            cases.append(one_case("known_filled", filled_p, active, q, dc, -1, k))
            cases.append(one_case("flagged_projector", flag_p, flag_active, q, 0, 1, k))

        # Each local channel consumes at most one unknown Q/s copy. Independent
        # local choices, including all four two-slot branches, must produce an
        # iid P/r program, not a mixture with a single shared latent choice.
        r = s + 1
        keep = (s / r) * (vac_p / s)
        known = np.zeros_like(vac_p)
        known[dc, dc] = 1 / r
        source_mixture = keep + known
        target = filled_p / r
        mixture_residual = np.linalg.norm(source_mixture - target, ord=2)
        two_slot_mixture = (np.kron(keep, keep) + np.kron(keep, known)
                            + np.kron(known, keep) + np.kron(known, known))
        iid_residual = np.linalg.norm(two_slot_mixture - np.kron(target, target), ord=2)
        if max(mixture_residual, iid_residual) > TOL:
            raise AssertionError("Occupied-anchor independent source mixture failed")
        source_checks.append({"classification_dimension": dc,
                              "classification_rank": s,
                              "program_dimension": dimension,
                              "program_rank": r,
                              "source_mixture_residual": float(mixture_residual),
                              "two_slot_iid_mixture_residual": float(iid_residual)})
    result = {
        "numpy_version": np.__version__, "seed": 20261108,
        "tolerance": TOL, "cases_checked": len(cases),
        "cases": cases, "direct_flagged_checks": flag_checks,
        "filled_source_checks": source_checks,
        "source_budget_contract": "N output program slots use at most N unknown Q/s copies; no expected-budget conversion",
        "noise_fixture_scope": "The saturating diagnostic channels check error conversion; they are not claimed specimen-constrained processors.",
        "limitations": "Finite matrix checks support routing and error conventions; universal lower bounds and arbitrary-reference claims follow analytically.",
        "passed": True,
    }
    arguments.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"passed": True, "cases_checked": len(cases),
                      "maximum_routing_residual": max(c["full_choi_routing_residual"] for c in cases),
                      "output": str(arguments.output)}))


if __name__ == "__main__":
    main()

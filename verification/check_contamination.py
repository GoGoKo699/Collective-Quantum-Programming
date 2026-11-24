"""Deterministic finite checks of contaminated recognition and programming.

These checks cover finite instances of the analytic statements. In particular,
sampled reference inputs and a Choi input are not a diamond-norm certificate.
"""

from itertools import product
from math import asin, pi, sin, sqrt

import numpy as np
from scipy.linalg import expm


ATOL = 2e-11
RNG = np.random.default_rng(20261124)


def projectors(frame):
    return frame @ frame.conj().T


def random_frame(dimension, rank):
    gaussian = RNG.standard_normal((dimension, rank))
    gaussian = gaussian + 1j * RNG.standard_normal((dimension, rank))
    return np.linalg.qr(gaussian)[0]


def random_density(dimension):
    gaussian = RNG.standard_normal((dimension, dimension))
    gaussian = gaussian + 1j * RNG.standard_normal((dimension, dimension))
    matrix = gaussian @ gaussian.conj().T
    return matrix / np.trace(matrix)


def positive_part(matrix):
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.maximum(values, 0)) @ vectors.conj().T


def trace_norm(matrix):
    return np.linalg.svd(matrix, compute_uv=False).sum()


def density_of(state):
    return np.outer(state, state.conj())


def kronecker_power(matrix, copies):
    result = matrix
    for _ in range(copies - 1):
        result = np.kron(result, matrix)
    return result


def check_compatibility():
    count = 0
    max_sine_residual = 0.0
    max_trace_residual = 0.0
    for dimension, rank in [(2, 1), (3, 2), (4, 2), (6, 1), (6, 4), (8, 4)]:
        for _ in range(8):
            p_frame = random_frame(dimension, rank)
            q_frame = random_frame(dimension, rank)
            p = projectors(p_frame)
            q = projectors(q_frame)
            # Singular values of the cross-subspace leakage are principal sines.
            sines = np.linalg.svd((np.eye(dimension) - p) @ q_frame,
                                  compute_uv=False)
            max_sine_residual = max(max_sine_residual,
                                    abs(trace_norm(p - q) - 2 * sines.sum()))
            boundary = 1 / (1 + sines.sum() / rank)
            for a in [0.95 * boundary, boundary, (1 + boundary) / 2]:
                clean_p, clean_q = (a / rank) * p, (a / rank) * q
                difference = clean_p - clean_q
                proposal = clean_q + positive_part(difference)
                identity = np.eye(dimension)
                values, vectors = np.linalg.eigh(difference)
                separator = projectors(vectors[:, values > ATOL])
                dual_trace = np.trace(separator @ clean_p
                                      + (identity - separator) @ clean_q).real
                primal_trace = np.trace(proposal).real
                predicted_trace = a * (1 + sines.sum() / rank)
                max_trace_residual = max(max_trace_residual,
                                         abs(primal_trace - dual_trace),
                                         abs(predicted_trace - dual_trace))
                assert np.linalg.eigvalsh(proposal - clean_p).min() >= -ATOL
                assert np.linalg.eigvalsh(proposal - clean_q).min() >= -ATOL
                if a <= boundary:
                    rho = proposal + max(0, 1 - primal_trace) * identity / dimension
                    for clean in (clean_p, clean_q):
                        noise = (rho - clean) / (1 - a)
                        assert abs(np.trace(noise) - 1) < ATOL
                        assert np.linalg.eigvalsh(noise).min() >= -ATOL
                else:
                    # Every simultaneous PSD upper bound has trace >= dual_trace.
                    assert dual_trace > 1 + ATOL
                count += 1
    assert max_sine_residual < ATOL
    assert max_trace_residual < ATOL
    print(f"Compatibility: {count} cases, sine residual {max_sine_residual:.3g}, "
          f"primal-dual trace residual {max_trace_residual:.3g}")


def check_reflection_distinguishability():
    max_residual = 0.0
    count = 0
    for dimension, rank, copies in [(2, 1, 1), (2, 1, 3), (3, 1, 2),
                                    (4, 2, 2), (4, 3, 2), (6, 5, 1)]:
        basis = np.eye(dimension, dtype=complex)
        p = projectors(basis[:, :rank])
        first, vacant = basis[:, 0], basis[:, rank]
        positive = (first + 1j * vacant) / sqrt(2)
        negative = (first - 1j * vacant) / sqrt(2)
        gamma = (kronecker_power(positive, copies)
                 + kronecker_power(negative, copies)) / sqrt(2)
        reflection_p = np.eye(dimension) - 2 * p
        for budget in [0, 0.03, 0.12, 0.35, 0.7, 1.4]:
            theta = min(asin(min(1, budget)), pi / (4 * copies))
            q_frame = basis[:, :rank].copy()
            q_frame[:, 0] = np.cos(theta) * first + sin(theta) * vacant
            reflection_q = np.eye(dimension) - 2 * projectors(q_frame)
            out_p = kronecker_power(reflection_p, copies) @ gamma
            out_q = kronecker_power(reflection_q, copies) @ gamma
            distance = trace_norm(density_of(out_p) - density_of(out_q))
            max_residual = max(max_residual, abs(distance - 2 * sin(2 * copies * theta)))
            count += 1
    assert max_residual < ATOL
    print(f"Reflection distinguishability: {count} batches, residual {max_residual:.3g}")


def check_classification_identity():
    max_residual = 0.0
    count = 0
    for rank in [1, 2, 3, 5]:
        dimension = 2 * rank
        identity = np.eye(dimension)
        for a in [0.2, 0.5, 0.725, 0.999]:
            for _ in range(6):
                p = projectors(random_frame(dimension, rank))
                noise = random_density(dimension)
                rho = (a / rank) * p + (1 - a) * noise
                unitary = expm((-1j * pi * rank / a) * rho)
                exact = identity - 2 * p
                effect = (identity - (unitary + unitary.conj().T) / 2) / 2
                error = (1 - np.trace(effect @ p).real / rank
                         + np.trace(effect).real / dimension) / 2
                frobenius_loss = np.linalg.norm(unitary - exact, 'fro') ** 2 / (16 * rank)
                max_residual = max(max_residual, abs(error - 1 / 4 - frobenius_loss))
                x = rank * (1 - a) / a
                assert frobenius_loss <= min(pi ** 2 * x ** 2, 2 * pi * x, 8 * rank) / (16 * rank) + ATOL
                count += 1
    assert max_residual < ATOL
    print(f"Balanced classification: {count} states, loss residual {max_residual:.3g}")


def check_balanced_pilot():
    dimension, rank = 4, 2
    rho = np.diag([3 / 8, 3 / 8, 1 / 8, 1 / 8])
    identity = np.eye(dimension)
    first, second, third, fourth = identity.T
    top = projectors(identity[:, :rank])
    angle = asin(1 / 4)
    candidates = []
    for phases in product([1, -1, 1j, -1j], repeat=2):
        frame = np.column_stack((np.cos(angle) * first + phases[0] * sin(angle) * third,
                                 np.cos(angle) * second + phases[1] * sin(angle) * fourth))
        p = projectors(frame)
        candidates.append(p)
        assert np.linalg.eigvalsh(rho - p / 3).min() >= -ATOL
        assert abs(np.linalg.eigvalsh(frame.conj().T @ np.linalg.solve(rho, frame)).max()
                   - 3) < ATOL
        risk = (1 - np.trace(top @ p).real / rank + np.trace(top).real / dimension) / 2
        assert abs(risk - 9 / 32) < ATOL

    # Phase-averaging yields an explicit least-favorable distribution.
    mean_clean = np.mean(candidates, axis=0) / rank
    mean_risk = (1 - trace_norm(mean_clean - identity / dimension) / 2) / 2
    assert abs(mean_risk - 9 / 32) < ATOL
    reflected_plus = identity - 2 * candidates[0]
    reflected_minus = identity - 2 * candidates[5]
    probe = first.astype(complex)
    gate_distance = trace_norm(density_of(reflected_plus @ probe)
                               - density_of(reflected_minus @ probe))
    assert abs(gate_distance / 2 - 7 * sqrt(15) / 32) < ATOL
    print(f"Balanced pilot: risk {mean_risk:.9f}, diamond floor {gate_distance / 2:.9f}")


def swap_operator(dimension, systems, first, second):
    identity = np.eye(dimension ** systems)
    tensor = identity.reshape((dimension,) * (2 * systems))
    return tensor.swapaxes(first, second).reshape(identity.shape)


def check_reference_collision():
    data_dimension = 4
    program_dimension = 2
    identity = np.eye(data_dimension)
    swap_sum = swap_operator(2, 3, 0, 2) + swap_operator(2, 3, 1, 2)
    data_swap = swap_operator(2, 2, 0, 1)
    max_fraction = 0.0
    count = 0
    for _ in range(5):
        rho = random_density(program_dimension)
        values, vectors = np.linalg.eigh(rho)
        h = np.kron(rho, np.eye(2)) + np.kron(np.eye(2), rho)
        moment = 2 * identity + h @ data_swap
        variance = np.linalg.eigvalsh(moment - h @ h).max()
        env_basis_rotation = np.kron(identity, vectors)
        mean = np.eye(data_dimension).reshape(-1) / sqrt(data_dimension)
        inputs = [mean, *(random_frame(data_dimension ** 2, 1)[:, 0] for _ in range(8))]
        for time in [0.03, 0.15, 0.3]:
            full = expm(-1j * time * swap_sum) @ env_basis_rotation
            full = full.reshape(data_dimension, program_dimension, data_dimension,
                                program_dimension)
            kraus = [sqrt(values[source]) * full[:, target, :, source]
                     for source, target in product(range(program_dimension), repeat=2)]
            ideal = np.kron(expm(-1j * time * h), identity)
            kraus_ref = [np.kron(operator, identity) for operator in kraus]
            bound = 2 * time ** 2 * variance
            assert bound <= 2 * time ** 2 * (2 + 2 * values.max()) + ATOL
            for state in inputs:
                output = sum(density_of(operator @ state) for operator in kraus_ref)
                exact = density_of(ideal @ state)
                distance = trace_norm(output - exact)
                assert distance <= bound + ATOL
                max_fraction = max(max_fraction, distance / bound)
                count += 1
    print(f"Reference-assisted collisions: {count} probes including Choi inputs, "
          f"largest observed error/bound {max_fraction:.6f}")


if __name__ == '__main__':
    check_compatibility()
    check_reflection_distinguishability()
    check_classification_identity()
    check_balanced_pilot()
    check_reference_collision()

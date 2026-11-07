# Reproduce the finite checks

For the separate comparison of GitHub's displayed mathematics with its committed source, see [hosted mathematics](hosted/README.md). That check and its screenshots concern rendering, not the validity of the proofs or the numerical bounds below.

Run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/verify.py --output verification/results.json
```

The checked environment used NumPy 2.3.5 and SciPy 1.17.0. The fixed random seed is 113207. The complete machine-readable output is [results.json](results.json). The script uses explicit finite matrices; no unknown-Hamiltonian oracle or diamond-norm SDP solver is assumed.

## What the calculation tests

Seven instances are included:

```text
(d,r,k) = (2,1,1), (2,1,2), (2,1,3), (3,1,1),
          (3,1,2), (3,2,1), (3,2,2).
```

Each projector has a complex orientation obtained by QR factorization. Independent tensor-permutation matrices construct the program-target swaps. Partial contractions of those matrices are compared with the formulas for $`h`$, $`M`$ and $`\|M-h^2\|_\infty`$ in the [construction](../science/parallel_program.md). The maximum first/second-moment residual in the stored run is below $`1.8\times10^{-15}`$; the maximum variance discrepancy is below $`9\times10^{-16}`$.

At each of $`\delta=0.03,0.12,0.4`$, the script checks both terms in the [reduced-unitary proof](../science/collision_bound.md): the compressed propagator error and the leakage effect. These are 21 local checks. The finite matrices satisfy the analytical upper bounds within the stated floating-point tolerances.

For $`N=32,128,512`$, the script builds the complete Kraus superoperator and raises it to the Nth power. It compares both exact collective collisions and the symmetric pair-swap implementation with the full tensor-power reflection channel. All errors use the unhalved convention.

| $`d`$ | $`r`$ | $`k`$ | $`N=32`$ exact / sweep | $`N=128`$ exact / sweep | $`N=512`$ exact / sweep |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0.328180 / 0.328180 | 0.090094 / 0.090094 | 0.023079 / 0.023079 |
| 2 | 1 | 2 | 0.582753 / 0.582424 | 0.174501 / 0.174494 | 0.045782 / 0.045782 |
| 2 | 1 | 3 | 0.775909 / 0.775155 | 0.252808 / 0.252786 | 0.068054 / 0.068054 |
| 3 | 1 | 1 | 0.399883 / 0.399883 | 0.110466 / 0.110466 | 0.028342 / 0.028342 |
| 3 | 1 | 2 | 0.704372 / 0.703938 | 0.213511 / 0.213501 | 0.056192 / 0.056192 |
| 3 | 2 | 1 | 1.227954 / 1.227954 | 0.448641 / 0.448641 | 0.124585 / 0.124585 |
| 3 | 2 | 2 | 1.631609 / 1.630372 | 0.793089 / 0.792972 | 0.247078 / 0.247075 |

The table gives the normalized Choi trace norm of the channel difference, equivalently the output trace norm on a maximally entangled target/reference input. It is a lower bound on diamond error, not the exact diamond norm. The JSON also records a valid Choi-dual upper formula and the compression/leakage upper formula, evaluated numerically. Floating-point evaluation is not an interval-arithmetic certificate.

Four further checks construct two rotated supports directly, evaluate their root fidelity from positive matrices, and verify orthogonality after the known-reference reflection and GHZ phase-amplification circuit. They test the geometry used in the [converse](../science/converse.md). The all-processor lower bound follows from the analytical discrimination argument.

## Verification boundary

The tests support the matrix identities, normalization, entangled-reference example, repeated-channel implementation and converse geometry in the listed dimensions. The universal variance lemma, all-dimensional theorem, Strang remainder, optimality and resource accounting are proved in the scientific pages. The tests do not establish priority, experimental performance, or the optimal small-batch cost. A passing numerical suite does not replace review of those proofs.

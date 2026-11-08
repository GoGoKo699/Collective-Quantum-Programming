# Reproduce the finite checks

For the separate comparison of GitHub's displayed mathematics with its committed source, see [hosted mathematics](hosted/README.md). That check and its screenshots concern rendering, not the validity of the proofs or the numerical bounds below.

Run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/verify.py --output verification/results.json
OPENBLAS_NUM_THREADS=1 python3 verification/verify_transfer.py
```

The checked environment used NumPy 2.3.5 and SciPy 1.17.0. The collision/converse suite uses fixed random seed 113207 and writes [results.json](results.json). The anchored-transfer suite uses seed 20261108 and writes [transfer_results.json](transfer_results.json); its `--output PATH` option changes that destination. Both scripts use explicit finite matrices; no unknown-Hamiltonian oracle or diamond-norm SDP solver is assumed.

## What the calculation tests

Seven instances are included:

```text
(d,r,k) = (2,1,1), (2,1,2), (2,1,3), (3,1,1),
          (3,1,2), (3,2,1), (3,2,2).
```

Each projector has a complex orientation obtained by QR factorization. Independent tensor-permutation matrices construct the program-target swaps. Partial contractions of those matrices are compared with the formulas for $`h`$, $`M`$ and $`\Vert M-h^2\Vert_\infty`$ in the [construction](../science/parallel_program.md). The maximum first/second-moment residual in the stored run is below $`1.8\times10^{-15}`$; the maximum variance discrepancy is below $`9\times10^{-16}`$.

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

## Anchored classification transfer

[verify_transfer.py](verify_transfer.py) checks the circuit and error conventions used in the [classification transfer](../science/classification_transfer.md). There are 27 routing cases: classification dimension and rank $`(d,s)=(2,1),(3,2),(5,4)`$, each with a vacuum, occupied, and flagged embedding, at each batch size $`k=1,2,3`$.

| Embedding | Programming register | Checked boundary |
|---|---|---|
| Known vacuum | $`D=d+1`$, rank $`r=s`$ | Includes a rank-one program and high classification rank |
| Known occupied direction | $`D=d+1`$, rank $`r=s+1`$ | All listed instances have $`r=D-1`$, including the smallest nontrivial case $`D=3,r=2`$ |
| Flagged projector | $`D=2d`$, rank $`r=s`$ | Direct block identity and routed channel with its exact doubled dimension |

The check constructs controlled swaps, invokes the ordinary tensor-power reflection once, and checks the returned routing ancilla and fillers. It compares the complete output on a maximally entangled control/test input and its reference of dimension $`2D`$, then on a second random reference-entangled input. The stored routing residual is zero at the reported floating precision. The maximum ideal-effect residual is below $`1.7\times10^{-15}`$.

For each occupied embedding, the script checks the exact source-mixture identity and all four independent two-slot branches against the desired product program. This checks independence as well as the single-copy state. The hard budget follows from the analytical copy-local channel: each output slot consumes at most one supplied specimen, including branches that discard it. No expected-budget or postselection claim is inferred from the numerical output.

A diagnostic mixture of two maximally distinguishable ordinary channels has exactly unhalved diamond error $`\epsilon=0.074`$, certified here by an explicit orthogonal-output witness and the maximum possible channel distance. Its induced binary effect saturates $`\Vert M-Q\Vert_\infty=\epsilon/2`$ and excess risk $`E=A_{d,s}\epsilon`$. The stored risk-identity residual is below $`2.6\times10^{-16}`$. This fixture tests the factor of two and contrast normalization; it is not a claimed implementation from a finite specimen program. The ordinary-to-controlled conversion still relies on the known anchor sector.

The universal diamond contraction, all-rank Q2 converse, integer lower-bound implication, and the absence of an additional direct-sum factor in $`k`$ are analytical statements. These finite cases do not numerically prove them or establish an optimal intermediate-batch law.

## Verification boundary

The tests support the matrix identities, normalization, entangled-reference examples, repeated-channel implementation, anchored routing and converse geometry in the listed dimensions. The universal variance lemma, all-dimensional theorem, Strang remainder, optimality and resource accounting are proved in the scientific pages. The tests do not establish priority, experimental performance, or the optimal intermediate-batch cost. A passing numerical suite does not replace review of those proofs.

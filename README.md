# Collective Quantum Programming

How many copies of an unknown quantum state are needed to program the same reflection on an entire batch of inputs? This repository studies a flat-rank program state, $`\rho_P=P/r`$, where $`P`$ is an unknown rank-$`r`$ projector on $`\mathbb C^d`$. The desired operation is the ordinary channel of $`(I-2P)^{\otimes k}`$ on $`k`$ jointly available data registers. Accuracy is measured in the unhalved diamond norm for the complete batch, including inputs entangled across registers and with a reference.

## Run the reflection batch

1. Supply the data registers and independent program specimens. For clean specimens, group the targets into sets no larger than the known program rank. Keep each group's targets available together. Use the [finite-gate allocation](science/resources.md#4-group-size-finite-gates-and-the-final-error) to set its specimen count, step angle and rotation precision from the batch error tolerance.
2. Bring in one fresh specimen. Apply a half-angle partial swap with each target in order up to the last, a full-angle partial swap with the last, then the same half-angle swaps in reverse order. Discard that specimen and repeat with the next until the group has used its allocation. For each [partial swap](science/resources.md#1-a-partial-swap-with-returned-work), start with a zero work qubit, apply Hadamard, controlled register swap and Hadamard, rotate the work qubit about Z at twice the requested swap angle, then undo the first three gates. Ideal rotations return the work qubit to zero. Finite synthesis includes its return error in the joint tolerance.
3. Return the data registers with the reflection applied to the stated joint accuracy, including correlations with an external reference. The processor uses no measurement, success flag, feedforward or retry. The [resource counts](science/resources.md#5-copy-gate-and-memory-counts) charge specimens and their preparation, pair gates, rotation synthesis and storage for both streamed and early specimens.

For contaminated programs, use the [separate allocation](science/contaminated_reflections.md#specimens-gates-and-synthesis) for a joint sweep across all targets. It uses the known clean fraction and applies when the contamination bias fits the stated tolerance. The [two-target example](learning/TUTORIAL.md#3-one-concrete-two-target-example) shows how the resulting reflections act on an entangled input.

## Main result for clean specimens

Let $`N_*(d,r,k,\epsilon)`$ be the smallest hard specimen budget of a deterministic, unconditional processor that achieves error at most $`\epsilon`$ uniformly over all rank-$`r`$ projectors. For $`1\le r\lt d`$, $`k\ge1`$ and $`0\lt \epsilon\le1/8`$,

```math
\frac{9}{8\pi^2}\frac{\max\{r^2,rk^2\}}{\epsilon}
\le N_*(d,r,k,\epsilon)
\le \left\lceil\frac{4\pi^2rk(r+k-1)}{\epsilon}\right\rceil.
```

The displayed constructive constant allows exact known rotation gates. A finite universal gate set achieves the same specimen order with its synthesis error and gate cost charged in [the resource account](science/resources.md).

The single-target order is matched for every nontrivial rank and dimension:

```math
N_*(d,r,1,\epsilon)=\Theta\!\left(\frac{r^2}{\epsilon}\right).
```

When $`k\ge r`$, the bounds match in order:

```math
N_*(d,r,k,\epsilon)=\Theta\!\left(\frac{rk^2}{\epsilon}\right).
```

Processing each target with a separate density matrix exponentiation routine at error $`\epsilon/k`$ uses $`O(r^2k^2/\epsilon)`$ specimens. A short collective collision lets one specimen interact with several targets before it is discarded. Evaluating the interaction variance on the actual flat-rank state gives the improved cost $`O((r^2k+rk^2)/\epsilon)`$. Thus the large-batch construction saves a factor of order $`r`$ relative to that explicit baseline. The lower bound applies to every processor in the stated model.

The collective interaction itself is an instance of Hermitian-preserving map exponentiation. The account combines the rank-sensitive batch analysis and matching large-batch converse with an exact classification-to-programming converse that closes the single-target order, and an implementation with explicit resources. [Related work](references/RELATED_WORK.md) identifies the inherited methods and separates nearby tasks and access models.

## Relation to flat-rank classification

[Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits) proves the classification precision converse used here. Its all-rank finite-sample theorem, transferred through a known vacuum or occupied direction, forces the rank-squared programming cost. The [transfer proof](science/classification_transfer.md) preserves the exact dimensions, hard specimen budget and unhalved diamond promise. A known eigenstate supplies the relative phase; generic controlled access to the ordinary reflection is not assumed. The classification theorem remains authoritative in that repository, and this repository develops its programming consequence.

## Contaminated specimens and classical records

If the training density is $`\rho=aP/r+(1-a)\sigma`$ with known clean fraction $`a`$ and an arbitrary fixed contaminant $`\sigma`$, the [contaminated-programming theorem](science/contaminated_reflections.md) adds an irreducible error of order $`\min\{1,kr(1-a)/a\}`$. It matches finite-copy error orders for one target and for $`k\ge r`$. Two distinct supports can produce the same training density, yet their reflections act differently on a coherent batch. For clean single-target programming at $`r\le d/2`$, keeping only a classical record after training requires $`\Theta(rd/\epsilon)`$ copies, versus $`\Theta(r^2/\epsilon)`$ with coherent retention.

[Quantum Training Contamination](https://github.com/GoGoKo699/Quantum-Training-Contamination) derives the recognition limit for the same rank-one contaminated source. Its [flat-rank extension](https://github.com/GoGoKo699/Quantum-Training-Contamination/blob/main/science/flat_rank_training.md) and the [classification account](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/main/science/contaminated_training.md) follow the one-test risk. At fixed rank-one contamination that limiting recognition risk decreases with dimension, while the corresponding reflection error has a dimension-independent floor. The [programming account](science/contaminated_reflections.md#an-ordinary-channel-can-supply-a-classifier) explains the one-way reduction and where the two criteria differ.

## Read the account

| Question | Page |
|---|---|
| What is supplied, promised and counted? | [Model and theorem](science/model.md) |
| Why does the actual program variance control a collision? | [Reduced-channel variance bound](science/collision_bound.md) |
| How do shared specimens implement the reflection batch? | [Collective construction](science/parallel_program.md) |
| Why does every processor pay the quadratic batch cost? | [Pair-discrimination converse](science/converse.md) |
| Why is the single-target rank-squared cost optimal? | [Classification-to-programming converse](science/classification_transfer.md) |
| What changes with contaminated specimens or classical-only storage? | [Contaminated reflection theorem and classical-record programming](science/contaminated_reflections.md) |
| What gates, precision, memory and preparation costs are required? | [Resources](science/resources.md) |
| What does the gain mean, and where does it stop? | [Interpretation](science/interpretation.md) |
| Which claims are inherited, and which comparisons are relevant? | [Related work and bibliography](references/RELATED_WORK.md) |
| Which finite-dimensional identities and channels were checked? | [Reproduction guide](verification/README.md) |

The [science index](science/README.md) gives the proof dependencies. Each argument has one authoritative page.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source bridge](learning/ANCHOR.md) selects the relevant chapters and translates the channel, fidelity and norm conventions used in the proofs.

The [30-milestone map](learning/MILESTONES.md) has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The first phase builds the complete programming contract from states, channels and distinguishability; the second connects the variance mechanism, implementation and two complementary converses to the optimal single-target and large-batch laws.

Use the [worked tutorial](learning/TUTORIAL.md) to follow that route through a two-target example, error accounting and the discrimination argument. The [LLM reading guide](llms.txt) maps questions to the authoritative science and learning pages.

## Scope and limitations

The clean component has known rank and a flat spectrum. Access consists of independent specimens. Preparation unitaries, their inverses, purifications and a classical eigenbasis are unavailable. The processor consumes its specimens, and the guarantee concerns one parallel batch with jointly available data.

For $`1\lt k\lt r`$, the bounds do not generally match: the lower is $`\Omega((r^2+rk^2)/\epsilon)`$ and the upper is $`O((r^2k+rk^2)/\epsilon)`$. Their remaining ratio is at most order $`\sqrt r`$. For $`r=d`$, the target is the identity channel and requires no specimens. The sample saving is not a claimed gate-count or wall-clock improvement: bounded-size groups use $`O(r^2k^2/\epsilon)`$ pair partial swaps, with additional dimension and rotation-synthesis costs stated explicitly.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/verify.py --output verification/results.json
OPENBLAS_NUM_THREADS=1 python3 verification/verify_transfer.py
OPENBLAS_NUM_THREADS=1 python3 verification/check_contamination.py
```

The checked-in [construction and pair-converse results](verification/results.json) and [transfer results](verification/transfer_results.json) contain the actual numerical output. The first suite covers swap moments, variance, entangled-reference channel examples, symmetric sweeps and the converse geometry in small dimensions. The transfer suite checks the anchored routes, exact source mixing and error normalization, including entangled references. The [contamination checks](verification/README.md#checks-for-contaminated-programs) cover compatible specimens, the phase witness and reference-assisted collision bounds. Floating-point checks support the implementation; the universal statements follow from the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

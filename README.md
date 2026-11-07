# Collective Quantum Programming

How many copies of an unknown quantum state are needed to program the same reflection on an entire batch of inputs? This repository studies a flat-rank program state, $`\rho_P=P/r`$, where $`P`$ is an unknown rank-$`r`$ projector on $`\mathbb C^d`$. The desired operation is the ordinary channel of $`(I-2P)^{\otimes k}`$ on $`k`$ jointly available data registers. Accuracy is measured in the unhalved diamond norm for the complete batch, including inputs entangled across registers and with a reference.

## Main result

Let $`N_*(d,r,k,\epsilon)`$ be the smallest hard specimen budget of a deterministic, unconditional processor that achieves error at most $`\epsilon`$ uniformly over all rank-$`r`$ projectors. For $`1\le r\lt d`$, $`k\ge1`$ and $`0\lt \epsilon\le1/8`$,

```math
\frac{9}{8\pi^2}\frac{rk^2}{\epsilon}
\le N_*(d,r,k,\epsilon)
\le \left\lceil\frac{4\pi^2rk(r+k-1)}{\epsilon}\right\rceil.
```

The displayed constructive constant allows exact known rotation gates. A finite universal gate set achieves the same specimen order with its synthesis error and gate cost charged in [the resource account](science/resources.md).

When $`k\ge r`$, the bounds match in order:

```math
N_*(d,r,k,\epsilon)=\Theta\!\left(\frac{rk^2}{\epsilon}\right).
```

Processing each target with a separate density matrix exponentiation routine at error $`\epsilon/k`$ uses $`O(r^2k^2/\epsilon)`$ specimens. A short collective collision lets one specimen interact with several targets before it is discarded. Evaluating the interaction variance on the actual flat-rank state gives the improved cost $`O((r^2k+rk^2)/\epsilon)`$. Thus the large-batch construction saves a factor of order $`r`$ relative to that explicit baseline. The lower bound applies to every processor in the stated model.

The collective interaction itself is an instance of Hermitian-preserving map exponentiation. The contribution developed here is the rank-sensitive batch analysis, its matching converse for $`k\ge r`$, and an implementation with explicit resources. [Related work](references/RELATED_WORK.md) identifies the inherited methods and separates nearby tasks and access models.

## Read the account

| Question | Page |
|---|---|
| What is supplied, promised and counted? | [Model and theorem](science/model.md) |
| Why does the actual program variance control a collision? | [Reduced-channel variance bound](science/collision_bound.md) |
| How do shared specimens implement the reflection batch? | [Collective construction](science/parallel_program.md) |
| Why can no deterministic processor use fewer specimens in the large-batch regime? | [Converse](science/converse.md) |
| What gates, precision, memory and preparation costs are required? | [Resources](science/resources.md) |
| What does the gain mean, and where does it stop? | [Interpretation](science/interpretation.md) |
| Which claims are inherited, and which comparisons are relevant? | [Related work and bibliography](references/RELATED_WORK.md) |
| Which finite-dimensional identities and channels were checked? | [Reproduction guide](verification/README.md) |

The [science index](science/README.md) gives the proof dependencies. Each argument has one authoritative page.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source bridge](learning/ANCHOR.md) selects the relevant chapters and translates the channel, fidelity and norm conventions used in the proofs.

The [30-milestone map](learning/MILESTONES.md) has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The first phase builds the complete programming contract from states, channels and distinguishability; the second connects the variance mechanism, implementation and converse to the optimal large-batch law.

Use the [worked tutorial](learning/TUTORIAL.md) to follow that route through a two-target example, error accounting and the discrimination argument. The [LLM reading guide](llms.txt) maps questions to the authoritative science and learning pages.

## Scope and limitations

The rank is known and the spectrum is exactly flat. Access consists of independent specimens of $`P/r`$; a preparation unitary, its inverse, a purification oracle and a classical eigenbasis are not supplied. Specimens are consumed. The guarantee concerns a parallel batch and does not provide a reusable oracle for future adaptive requests.

For $`k\lt r`$, the upper and lower bounds do not generally match. For $`r=d`$, the target is the identity channel and requires no specimens. The sample saving is not a claimed gate-count or wall-clock improvement: bounded-size groups use $`O(r^2k^2/\epsilon)`$ pair partial swaps, with additional dimension and rotation-synthesis costs stated explicitly.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/verify.py --output verification/results.json
```

The checked-in [results](verification/results.json) contain the actual numerical output. The tests cover swap moments, variance, entangled-reference channel examples, symmetric sweeps and the converse geometry in small dimensions. Floating-point checks support the implementation; the universal statements follow from the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

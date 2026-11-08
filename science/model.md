# Programming a parallel reflection channel

A quantum program consists of independent specimens of an unknown mixed state. The processor consumes these specimens to apply the same reflection to a batch of data registers. Accuracy refers to the channel on the entire batch, including its action on inputs entangled with an external reference.

## Source, processor, and output

Let $`d\ge 2`$, $`1\le r\lt d`$, and $`k\ge 1`$ be integers. The single-register Hilbert space is $`\mathcal H=\mathbb C^d`$, and the data space is $`A=\mathcal H^{\otimes k}`$. The unknown parameter is an orthogonal projector $`P`$ on $`\mathcal H`$ with rank $`r`$. One source specimen is the state

```math
\rho_P=\frac{P}{r}.
```

The dimension, rank, batch size, and requested accuracy are supplied classically. The support of $`P`$ has no supplied classical description. The source provides independent copies of $`\rho_P`$, conditional on the same fixed $`P`$. It does not provide a purification, eigenvector labels, a preparation unitary, its inverse, or controlled access to such a unitary.

The reflection and its target channel are

```math
R_P=I_{\mathcal H}-2P,\qquad
\mathcal R_P^{(k)}(X)=R_P^{\otimes k}X R_P^{\otimes k}.
```

This is an ordinary unitary channel. A controlled reflection, which makes the unitary's global phase observable, is a different target.

For a nonnegative integer $`N`$, a processor is a completely positive, trace-preserving map

```math
\mathcal C:\mathsf L\!\left(A\otimes\mathcal H^{\otimes N}\right)
\longrightarrow\mathsf L(A).
```

Here $`\mathsf L(B)`$ denotes the linear operators on a Hilbert space $`B`$. The map $`\mathcal C`$ may depend on the public parameters but is independent of $`P`$. It may use known ancillas, joint operations, measurements, classical randomness, and feedforward. All outcomes are included in the returned channel. There is no uncharged postselection or conditional success guarantee.

Supplying the program produces the data channel

```math
\widetilde{\mathcal R}_P(X)
=\mathcal C\!\left(X\otimes\rho_P^{\otimes N}\right).
```

The hard source budget is $`N`$ specimens. A processor may discard unused specimens, and there is no requirement to return a program or catalyst. The data output comprises the same $`k`$ registers.

## Joint accuracy

For an operator $`X`$, write $`\Vert X\Vert_1=\mathrm{Tr}\,\sqrt{X^\dagger X}`$ and let $`\Vert X\Vert_\infty`$ denote its operator norm. The error convention is the **unhalved diamond norm**. For the difference $`\Delta`$ of two channels on $`A`$,

```math
\Vert\Delta\Vert_\diamond
=\sup_{\omega\in\mathsf D(A\otimes Z)}
\left\Vert(\Delta\otimes\mathrm{id}_Z)(\omega)\right\Vert_1,
\qquad \dim Z=\dim A=d^k.
```

The set $`\mathsf D(B)`$ contains the density operators on $`B`$. The reference $`Z`$ is inaccessible to the processor. This expression includes arbitrary entanglement among the data registers and between the data and reference. A bound on each output marginal would be weaker.

A processor is $`\epsilon`$-accurate if

```math
\sup_{P:\,P^2=P=P^\dagger,\ \mathrm{rank}\,P=r}
\left\Vert\widetilde{\mathcal R}_P-\mathcal R_P^{(k)}\right\Vert_\diamond
\le\epsilon.
```

Let $`N_*(d,r,k,\epsilon)`$ be the smallest hard specimen budget for which such a processor exists. This definition allows arbitrary known operations; their implementation cost is accounted for separately in [resources.md](resources.md). Source preparation, storage, and gate synthesis are not part of an implicit free loading oracle.

## The copy-complexity theorem

**Theorem.** For every integer $`d\ge2`$, $`1\le r\lt d`$, $`k\ge1`$, and every $`0\lt \epsilon\le1/8`$,

```math
\frac{9}{8\pi^2}\frac{\max\{r^2,rk^2\}}{\epsilon}
\le N_*(d,r,k,\epsilon)
\le
\left\lceil\frac{4\pi^2rk(r+k-1)}{\epsilon}\right\rceil.
```

The upper bound is realized by deterministic collisions with fresh program specimens and known pair partial swaps. Its displayed constant treats known one-qubit rotations as exact. A finite gate set gives the same asymptotic specimen law with an explicit synthesis budget in [resources.md](resources.md).

The [collision bound](collision_bound.md) controls the full reduced channel through a compressed operator variance. The [parallel construction](parallel_program.md) evaluates that variance for the swap interaction and obtains the upper bound. The [pair converse](converse.md) gives the $`rk^2/\epsilon`$ lower term. The [classification transfer](classification_transfer.md) supplies the rank-squared term through an anchored reduction with the same hard budget and unhalved diamond error. Both apply to every processor in the model, including processors that first estimate a classical description of the support.

At $`k=1`$, the upper and lower orders match uniformly for every $`1\le r\lt d`$:

```math
N_*(d,r,1,\epsilon)=\Theta\!\left(\frac{r^2}{\epsilon}\right).
```

When $`k\ge r`$, the theorem gives dimension-independent constants on both sides:

```math
\frac{9}{8\pi^2}\frac{rk^2}{\epsilon}
\le N_*(d,r,k,\epsilon)
\le (8\pi^2+1)\frac{rk^2}{\epsilon}.
```

Thus

```math
N_*(d,r,k,\epsilon)=\Theta\!\left(\frac{rk^2}{\epsilon}\right)
\qquad (k\ge r, 0\lt \epsilon\le1/8).
```

For $`1\lt k\lt r`$, the theorem gives lower order $`\Omega((r^2+rk^2)/\epsilon)`$ and upper order $`O((r^2k+rk^2)/\epsilon)`$. Their ratio is within universal constants of $`\min\{k,r/k\}`$, at most order $`\sqrt r`$. No complete optimal law in that intermediate regime is asserted. The upper construction itself applies throughout $`0\lt \epsilon\le1`$.

## Availability and endpoints

The collective interaction requires joint access to the data registers in each processed block. All registers may arrive together, or they may be processed in blocks that are jointly available. The theorem does not provide a device that accepts arbitrary sequential adaptive requests whose later input states do not yet exist. Its diamond guarantee permits arbitrary reference systems, but does not remove this availability requirement.

The excluded endpoint $`r=d`$ is trivial. Then $`P=I_{\mathcal H}`$ is known and $`R_P=-I_{\mathcal H}`$, so the ordinary target channel is the identity and needs zero specimens. The converse therefore requires the nonempty complement $`r\lt d`$.

The swap interaction is inherited from Hermitian-preserving map exponentiation. The pair converse adapts established sample-to-query discrimination arguments; the rank-squared converse transfers the all-rank finite-sample theorem of Quantum Classification Rank Limits. The precise relation to HME, ordinary DME, and multipartite collision simulation is recorded in [RELATED_WORK.md](../references/RELATED_WORK.md).

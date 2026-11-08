# Classification converse transferred to ordinary reflections

A channel that programs a reflection accurately enough must also support a good classification decision. The transfer needs a phase reference: an ordinary reflection channel does not, by itself, specify a controlled reflection. A known kernel or occupied direction supplies that reference in a restricted family of projectors. This page proves the resulting rank-squared converse and combines it with the [pair-discrimination converse](converse.md).

## Statement and dimensions

This page writes $`D`$ for the programming dimension, called $`d`$ in [the model](model.md), and reserves $`d`$ for a classification test's dimension. The program rank remains $`r`$; a classification projector $`Q`$ has rank $`s`$. All programming errors below are **unhalved diamond errors**, and $`N`$ is a hard specimen budget of a deterministic, unconditional processor.

**Transferred converse.** For every $`k\ge1`$ and $`0\lt\epsilon\le1/2`$,

```math
N_*(D,r,k,\epsilon)\ge
\begin{cases}
\left\lceil r^2(\epsilon^{-1}-1)\right\rceil,
& D\ge r+2,\\[4pt]
\left\lceil(r-1)^2(\epsilon^{-1}-1)\right\rceil,
& D=r+1,\quad r\ge2.
\end{cases}
```

For the remaining $`(D,r)=(2,1)`$ case, use the existing [pair converse](converse.md). Together, the converses imply, for every $`1\le r\lt D`$, $`k\ge1`$ and $`0\lt\epsilon\le1/8`$,

```math
N_*(D,r,k,\epsilon)
\ge\frac{9}{8\pi^2}
\frac{\max\{r^2,rk^2\}}{\epsilon}.
```

In particular, the [constructive upper bound](parallel_program.md) and this converse give

```math
N_*(D,r,1,\epsilon)=\Theta\!\left(\frac{r^2}{\epsilon}\right)
\qquad(1\le r\lt D,\quad0\lt\epsilon\le1/8),
```

with constants independent of the dimension and rank.

The imported result is the all-rank finite-sample statement of [Quantum Classification Rank Limits, Theorem Q2](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/632fa8921e16b17dd5905b2e4f8d7f79d1570186/science/quantum_precision.md). That project owns the classification theorem; this page owns the anchored channel reduction and its programming consequence.

## The classification input to the proof

The classification experiment supplies $`N`$ independent training copies of $`Q/s`$, then one test. With equal priors, the test is drawn either from $`Q/s`$ or from the known background $`I_d/d`$. The learner may retain the training systems and make any joint measurement after the test arrives. No fresh post-test examples, purification or preparation oracle is supplied.

The known-projector error and available advantage are

```math
R_* =\frac{s}{2d},\qquad
A_{d,s}=\frac{1-s/d}{2}\gt0,
\qquad 1\le s\lt d.
```

Let $`E_{\mathrm Q}(N;d,s)`$ be the smallest uniform excess risk over $`R_*`$, and write $`N_{\mathrm Q}(d,s,\delta)`$ for the smallest hard training budget attaining excess at most $`\delta`$. Q2 proves the all-rank finite-sample lower bound

```math
E_{\mathrm Q}(N;d,s)\ge A_{d,s}
\begin{cases}
1-\dfrac{\sqrt N}{2s},&0\le N\le s^2,\\[6pt]
\dfrac{s^2}{N+s^2},&N\ge s^2.
\end{cases}
```

Its convenient $`s\le d/2`$ corollary is not the input needed here. Retaining the factor $`A_{d,s}`$ makes the reduction valid even when the classification contrast is small.

## A known eigenstate turns routing into control

Consider the known orthogonal decomposition

```math
\mathcal H_D=\mathbb C|v\rangle\oplus W,
\qquad \dim W=d=D-1,
```

and the restricted projector family

```math
P=a|v\rangle\langle v|\oplus Q,
\qquad a\in\{0,1\},\qquad s=r-a.
```

Here $`a`$, $`|v\rangle`$ and the embedding of $`W`$ are fixed independently of the unknown $`Q`$. Write

```math
R_P=\lambda|v\rangle\langle v|\oplus R_Q,
\qquad \lambda=1-2a\in\{+1,-1\},\qquad R_Q=I_d-2Q.
```

A universal programming processor must work on this restricted family. The restriction is used by the lower-bound experiment; it does not supply the processor with an eigenbasis or change its universal promise.

Initialize the programmer's data register $`A`$ in $`|v\rangle`$. Let a separate $`D`$-dimensional register $`B`$ hold the later test in the embedded subspace $`W`$, and introduce a known control qubit $`C`$. Apply the known controlled swap

```math
W_{\mathrm{route}}
=|0\rangle\langle0|_C\otimes I_{AB}
+|1\rangle\langle1|_C\otimes\mathrm{SWAP}_{AB},
```

invoke the ordinary reflection channel on $`A`$, then undo the controlled swap. For every $`|\psi\rangle\in W`$, the ideal action is

```math
\begin{aligned}
|0\rangle_C|v\rangle_A|\psi\rangle_B
&\longmapsto\lambda|0\rangle_C|v\rangle_A|\psi\rangle_B,\\
|1\rangle_C|v\rangle_A|\psi\rangle_B
&\longmapsto|1\rangle_C|v\rangle_A R_Q|\psi\rangle_B.
\end{aligned}
```

The known control phase $`D_\lambda=\lambda|0\rangle\langle0|+|1\rangle\langle1|`$ then gives the controlled reflection

```math
U_Q=|0\rangle\langle0|\otimes I_d
+|1\rangle\langle1|\otimes R_Q,
```

while returning $`A`$ to $`|v\rangle`$. For $`\lambda=-1`$, a control $`Z`$ differs from $`D_\lambda`$ only by an irrelevant global sign.

The same ordinary channel is invoked on both routing branches. The construction never controls the unknown processor or an unknown preparation unitary. A global phase on the representative $`R_P`$ multiplies both branches equally. Initialization, routing, phase correction and discarding $`A`$ are known channels independent of $`Q`$. Thus a programming error at most $`\epsilon`$ produces a controlled-channel error at most $`\epsilon`$ by diamond-norm contraction. This statement retains arbitrary reference entanglement; the stabilized diamond norm in the model already provides the needed arbitrary-reference guarantee.

## From channel error to relative classification risk

Prepare $`C`$ in $`|+\rangle`$, apply the routed channel and measure $`C`$ in the $`X`$ basis. Predict the source class on outcome $`-`$. The ideal test effect is $`Q`$. Let $`M_Q`$ be the actual binary effect after every program and processor outcome is averaged.

For every density operator $`\theta`$ on the original $`d`$-dimensional test space, binary measurement of the two normalized output states gives

```math
\left|\mathrm{Tr}[(M_Q-Q)\theta]\right|\le\frac\epsilon2.
```

Maximizing the absolute expectation of the Hermitian difference over input states gives

```math
\Vert M_Q-Q\Vert_\infty\le\frac\epsilon2.
```

The factor of one-half comes from converting the unhalved trace norm to a probability difference. No support-preserving promise about the approximate output is needed: the original test is embedded by a known isometry, and the control measurement defines a valid effect on that original space.

The exact excess-risk identity is

```math
R(M_Q,Q)-R_*
=\frac12\mathrm{Tr}\!\left[
(Q-M_Q)\left(\frac Qs-\frac{I_d}{d}\right)\right].
```

Since

```math
\left\Vert\frac Qs-\frac{I_d}{d}\right\Vert_1
=2(1-s/d)=4A_{d,s},
```

trace/operator-norm duality gives the relative risk promise

```math
0\le R(M_Q,Q)-R_*
\le\frac12\Vert Q-M_Q\Vert_\infty
\left\Vert\frac Qs-\frac{I_d}{d}\right\Vert_1
\le A_{d,s}\epsilon.
```

The background remains exactly $`I_d/d`$ on $`W`$, rather than $`I_D/D`$. The classifier uses only the supplied training copies, all of which arrive before its single later test. Its error bound is uniform in $`Q`$, so Q2 applies to the classifier's minimax risk.

For $`0\lt\epsilon\le1/2`$, Q2's first branch excludes $`N\lt s^2`$. Its second branch therefore implies

```math
A_{d,s}\frac{s^2}{N+s^2}\le A_{d,s}\epsilon,
\qquad
N\ge\left\lceil s^2(\epsilon^{-1}-1)\right\rceil.
```

The positive contrast cancels exactly. Bounding the excess only by $`\epsilon/2`$ would lose this consequence when $`s/d`$ is close to one.

## Exact source reductions and the endpoint

### Known vacuum: $`D\ge r+2`$

Take $`a=0`$, so $`s=r`$ and $`d=D-1\gt r`$. Embedding each training copy $`Q/r`$ into $`W`$ gives one specimen $`P/r`$ exactly. Hence a programmer with hard budget $`N`$ supplies a classifier with the same hard budget and

```math
N_*(D,r,1,\epsilon)
\ge N_{\mathrm Q}(D-1,r,A_{D-1,r}\epsilon)
\ge\left\lceil r^2(\epsilon^{-1}-1)\right\rceil.
```

### Known occupied direction: $`D=r+1`$, $`r\ge2`$

A vacuum restriction would make the remaining projector full rank, with zero classification contrast. Instead take $`a=1`$, $`d=r`$ and $`s=r-1\ge1`$. Let $`V:W\to\mathcal H_D`$ be the known embedding. The channel

```math
\Lambda(X)
=\frac1r\mathrm{Tr}(X)|v\rangle\langle v|
+\frac{s}{r}VXV^\dagger
```

is completely positive and trace preserving, and satisfies $`\Lambda(Q/s)=P/r`$. Physically, keep and embed each input specimen with probability $`s/r`$; otherwise discard it and prepare $`|v\rangle`$. Independent choices in the $`N`$ slots give exactly $`(P/r)^{\otimes N}`$ from $`N`$ supplied copies of $`Q/s`$.

Every slot uses at most one unknown specimen. This is an unconditional hard-budget reduction, with no postselection, expected-budget substitution or eigenvector label. Routing through the known eigenvalue $`-1`$ and correcting the control phase gives

```math
N_*(r+1,r,1,\epsilon)
\ge N_{\mathrm Q}(r,r-1,A_{r,r-1}\epsilon)
\ge\left\lceil(r-1)^2(\epsilon^{-1}-1)\right\rceil.
```

When $`D=2,r=1`$, neither anchored restriction leaves a nontrivial classification problem. The [pair converse](converse.md) gives the required $`\Omega(1/\epsilon)`$ lower bound there.

### Flagged alternative: programming dimension $`2d`$

For any classification projector $`Q`$ of rank $`s\lt d`$, append a known flag and define

```math
\widehat P=|1\rangle\langle1|\otimes Q
\quad\text{on }\mathbb C^2\otimes\mathbb C^d.
```

Its rank is $`s`$, one program specimen is exactly $`|1\rangle\langle1|\otimes Q/s`$, and its ordinary reflection is $`U_Q`$ itself. Thus

```math
N_*(2d,s,1,\epsilon)
\ge N_{\mathrm Q}(d,s,A_{d,s}\epsilon)
\ge\left\lceil s^2(\epsilon^{-1}-1)\right\rceil.
```

Flagging doubles the programming dimension. The direct-sum vacuum route uses dimension $`d+1`$ and the explicit routing ancilla. Neither is a generic same-dimension conversion of an ordinary reflection channel into a controlled one.

At balanced rank $`D=2r`$, the complementary projector gives $`R_{I-P}=-R_P`$, so its ordinary channel is identical. Without a phase reference, that channel cannot determine which support is to be accepted. The anchored restrictions fix the relative action and legitimately avoid this obstruction in a minimax converse. For $`r\ge2`$, the balanced-rank vacuum family still has $`D-1\gt r`$.

## Batch padding, constants and the remaining gap

Initialize the other $`k-1`$ data inputs of a batch processor to any fixed known states and discard their outputs. The ideal target is a tensor product, so this known pre- and postprocessing leaves exactly one ordinary reflection. Diamond contraction preserves the same $`D,r,N,\epsilon`$. It costs no additional program specimens and requires no special eigenstate for the discarded inputs. The transferred single-target lower bound therefore applies to every $`k\ge1`$.

For $`\epsilon\le1/8`$, the vacuum lower bound is at least $`(7/8)r^2/\epsilon`$. In codimension one and $`r\ge2`$, use $`(r-1)^2\ge r^2/4`$ to obtain at least $`(7/32)r^2/\epsilon`$. Both constants exceed $`9/(8\pi^2)`$. Combining with the pair lower bound, including its $`(2,1)`$ case, proves the displayed uniform maximum bound.

Together with the construction, this gives

```math
\Omega\!\left(\frac{r^2+rk^2}{\epsilon}\right)
\le N_*(D,r,k,\epsilon)
\le O\!\left(\frac{r^2k+rk^2}{\epsilon}\right).
```

The sum in the lower order is equivalent within a factor of two to its maximum. At $`k=1`$ and at $`k\ge r`$, the orders match. For $`1\lt k\lt r`$, the ratio of these rate bounds is within universal constants of $`\min\{k,r/k\}`$, reaching order $`\sqrt r`$ near $`k\asymp\sqrt r`$. This describes the remaining bounds, not a proved separation between the true optimum and the upper construction.

The single-test classification theorem does not supply an additional factor $`k`$ multiplying $`r^2/\epsilon`$. Summing $`k`$ marginal risks also multiplies the allowed total loss by $`k`$ and yields no such gain. A matching intermediate-batch converse would require another argument. These reductions also do not produce a reusable processor for arbitrary adaptive future inputs.

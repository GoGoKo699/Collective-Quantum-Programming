# Circuits, accuracy and resources

The processor uses copies of $`\rho_P=P/r`$ to implement $`R_P^{\otimes k}`$, where $`R_P=I-2P`$, $`1\le r\lt d`$ and $`0\lt \epsilon\le1/8`$. The rank $`r`$, the dimension $`d`$ and the requested error are known. The projector is supplied only through its copies. This page implements the [collective construction](parallel_program.md) using ordinary gates and accounts for the error introduced by that implementation.

Targets in the same group must be available together. Different groups may be processed successively, and the input may be entangled across groups and with an external reference. The promised output is the complete parallel channel. These resources do not provide an oracle that accepts arbitrary future adaptive requests.

## 1. A partial swap with returned work

Let $`S`$ swap two registers, each containing $`n=\lceil\log_2d\rceil`$ qubits. The required gate is

```math
U_\alpha=e^{-i\alpha S}.
```

Since $`S^2=I`$, its eigenvalues are $`s=\pm1`$. Introduce one work qubit $`a`$ in $`|0\rangle`$ and define

```math
C_S=|0\rangle\langle0|_a\otimes I
    +|1\rangle\langle1|_a\otimes S,
\qquad
W_S=(H_a\otimes I)C_S(H_a\otimes I),
```

where $`H_a`$ is the Hadamard gate. For an eigenvector $`|\psi_s\rangle`$ of $`S`$,

```math
W_S\bigl(|0\rangle_a|\psi_s\rangle\bigr)
=\left|\frac{1-s}{2}\right\rangle_a|\psi_s\rangle.
```

With the convention $`R_z(\theta)=\mathrm{diag}(e^{-i\theta/2},e^{i\theta/2})`$, the circuit

```math
W_S\bigl(R_z(2\alpha)_a\otimes I\bigr)W_S
```

therefore acts as

```math
|0\rangle_a|\psi\rangle
\longmapsto
|0\rangle_a e^{-i\alpha S}|\psi\rangle.
```

The work qubit returns exactly to $`|0\rangle`$ and is uncorrelated with the two registers. Linearity gives the same statement for arbitrary mixed inputs and reference entanglement. It can be reused throughout the ideal circuit.

A controlled register swap is the product of $`n`$ controlled swaps of corresponding qubit pairs. Each such three-qubit gate has an exact constant-size Clifford+T implementation. For example, a controlled swap can be written as two CNOT gates surrounding one Toffoli gate. Thus one partial swap uses two controlled register swaps, four Hadamard gates and one variable-angle rotation. Its cost is $`O(n)`$ fixed-size gates and one variable rotation, with one work qubit.

When $`d`$ is not a power of two, all input states occupy the specified $`d`$-dimensional subspace of the padded register. The full register swap preserves the tensor product of those subspaces. Padding does not replace the supplied state by a state of a different rank or dimension.

## 2. A symmetric sweep implements the collective collision

Consider a group of $`b`$ targets and one fresh program register. Write $`S_j`$ for the swap between the program and target $`j`$, and set

```math
H_b=\sum_{j=1}^{b}S_j.
```

The collective collision would apply $`e^{-i\delta H_b}`$. It is implemented by the symmetric product

```math
T_b(\delta)
=e^{-i\delta S_1/2}\cdots e^{-i\delta S_{b-1}/2}
 e^{-i\delta S_b}
 e^{-i\delta S_{b-1}/2}\cdots e^{-i\delta S_1/2}.
```

This sweep contains $`2b-1`$ pair partial swaps. For $`b=1`$, it is the exact collision. The sweep uses the same program register throughout; that register is discarded after the sweep.

### An error bound for every step size

The operator-norm estimate

```math
\left\Vert T_b(\delta)-e^{-i\delta H_b}\right\Vert_\infty
\le \frac{b^3|\delta|^3}{3}
```

holds for every real $`\delta`$. To prove it, first observe that

```math
T_b(0)=I,
\qquad
T_b'(0)=-iH_b,
\qquad
T_b''(0)=-H_b^2.
```

The first derivative follows by differentiating the factors. The palindromic order gives $`T_b(\delta)T_b(-\delta)=I`$; expanding this identity to second order gives the second derivative.

Every factor is unitary, every swap has norm one, and the sum of the absolute generator weights in the product is $`b`$. The Leibniz expansion therefore bounds the norm of its third derivative by $`b^3`$, at every real argument. The exact exponential has the same derivative bound because $`\Vert H_b\Vert_\infty\le b`$. Both functions have identical Taylor terms through second order. Applying the integral remainder to each gives the displayed $`b^3|\delta|^3/3`$ estimate.

For unitaries $`U,V`$,

```math
\Vert\mathrm{Ad}_U-\mathrm{Ad}_V\Vert_\diamond
\le 2\Vert U-V\Vert_\infty.
```

Preparing and discarding a program register are channel contractions. Consequently, replacing one exact collective collision by its symmetric sweep changes the resulting data channel by at most $`2b^3|\delta|^3/3`$ in unhalved diamond norm. Symmetry removes the second-order product error that a first-order sweep would introduce.

## 3. One group, with a complete error budget

The [collision bound](collision_bound.md) gives the ideal reduced-channel error for $`N`$ fresh programs, each interacting for $`\delta=\pi r/N`$:

```math
\left\Vert\Phi_{\pi r/N}^{N}
      -\mathrm{Ad}_{R_P^{\otimes b}}\right\Vert_\diamond
\le \frac{2\pi^2r^2v_b}{N},
```

where

```math
v_b
=\max_{m\in\{0,\ldots,b\}}
 \left[b+\frac{(b-1)m}{r}-\frac{m^2}{r^2}\right]
\le b+\frac{b(b-1)}r.
```

Replacing every collision by a symmetric sweep and telescoping over the $`N`$ steps yields

```math
\left\Vert\widetilde\Phi_{b,N}
      -\mathrm{Ad}_{R_P^{\otimes b}}\right\Vert_\diamond
\le
\frac{2\pi^2 r b(r+b-1)}{N}
+\frac{2\pi^3r^3b^3}{3N^2}.
```

The first term is the program-induced error. The second is the implementation error of the collective interaction. Both bounds are nonasymptotic.

For a group error allowance $`0\lt \eta\le1`$, choose

```math
N_b(\eta)
=\left\lceil\frac{4\pi^2 r b(r+b-1)}\eta\right\rceil.
```

The first error term is at most $`\eta/2`$. The second obeys

```math
\frac{2\pi^3r^3b^3}{3N_b(\eta)^2}
\le \frac{\eta^2}{24\pi}
     \frac{rb}{(r+b-1)^2}
\le \frac{\eta^2}{24\pi}.
```

Here $`r+b-1\ge\max(r,b)\ge\sqrt{rb}`$ for positive integers $`r,b`$. Thus the total group error is less than $`\eta`$. No additional assumption on $`\delta`$ is needed.

## 4. Group size, finite gates and the final error

Take

```math
q=\left\lceil\frac kr\right\rceil,
\qquad
1\le b_j\le r,
\qquad
\sum_{j=1}^{q}b_j=k.
```

For example, use groups of size $`r`$ followed by the remaining targets. Set $`b=\min(k,r)`$, the largest possible group size. To leave room for rotation synthesis, give every group the allowance

```math
\eta=\frac{\epsilon}{2q},
\qquad
N_j=
\left\lceil
\frac{8\pi^2 q r b_j(r+b_j-1)}{\epsilon}
\right\rceil,
\qquad
\delta_j=\frac{\pi r}{N_j}.
```

The groups use independent program copies. Their errors add to at most $`\epsilon/2`$, even for data entangled across groups, because diamond norm controls the channel with all remaining systems retained as references.

Let

```math
N_{\mathrm{tot}}=\sum_{j=1}^{q}N_j,
\qquad
L=\sum_{j=1}^{q}(2b_j-1)N_j
```

be the numbers of program copies and partial-swap gadgets. There is one variable rotation in each gadget. Approximate each rotation to operator norm

```math
\zeta=\frac{\epsilon}{4L},
```

up to an irrelevant global phase. Exact surrounding gates preserve that error, so each gadget contributes at most $`2\zeta`$ in diamond norm. A telescoping bound for the complete circuit gives at most $`2L\zeta=\epsilon/2`$ of synthesis error. Together with the program and sweep errors,

```math
\left\Vert\mathcal C_P
 -\mathrm{Ad}_{R_P^{\otimes k}}\right\Vert_\diamond
\le\epsilon.
```

The synthesis estimate can retain the work qubit at the output. Ideal rotations return it exactly. With approximate finite gates, its return to $`|0\rangle`$, its decoupling from the data, and the data-channel accuracy hold jointly within the same complete-channel error budget. Exact work return is therefore asserted in the ideal-rotation model; approximate synthesis does not silently inherit an exact-return promise. The theorem requires no measurement, postselection or success flag.

For a fixed universal gate set such as Clifford+T, the [Solovay–Kitaev construction of Dawson and Nielsen](https://arxiv.org/abs/quant-ph/0505030) gives a conservative $`\mathrm{polylog}(L/\epsilon)`$ synthesis cost per variable rotation. Fixed controlled swaps have exact constant-size decompositions at the qubit level. The resulting total gate bound is

```math
O\!\left(
L\left[n+\mathrm{polylog}\!\left(\frac L\epsilon\right)\right]
\right).
```

The polylogarithmic exponent depends on the chosen synthesis procedure. The estimate includes the precision needed by the full circuit and does not assume exact arbitrary-angle rotations in the finite-gate model.

## 5. Copy, gate and memory counts

The explicit copy allocation obeys

```math
N_{\mathrm{tot}}
\le
\frac{8\pi^2 q r}{\epsilon}
\sum_{j=1}^{q}b_j(r+b_j-1)+q
\le
\frac{8\pi^2 q r k(r+b-1)}{\epsilon}+q.
```

For $`k\le r`$, there is one group. For $`k>r`$, use $`qr\le k+r-1`$ and $`r+b-1=2r-1\le2r`$. In both cases,

```math
N_{\mathrm{tot}}
\le
\frac{16\pi^2 r k(r+k-1)}{\epsilon}+q
=O\!\left(\frac{r^2k+rk^2}{\epsilon}\right).
```

In the matched regime $`k\ge r`$, this gives

```math
N_{\mathrm{tot}}
\le \frac{32\pi^2rk^2}{\epsilon}+q
=O\!\left(\frac{rk^2}{\epsilon}\right).
```

The [converse](converse.md) establishes the same sample order in this regime. The gate count satisfies

```math
L\le(2b-1)N_{\mathrm{tot}}
=O\!\left(\frac{r^2k^2}{\epsilon}\right)
```

for all $`k\ge1`$. When $`k\le r`$, use $`b=k`$ and $`N_{\mathrm{tot}}=O(r^2k/\epsilon)`$. When $`k\ge r`$, use $`b=r`$ and the matched copy bound.

| Resource | Explicit serial implementation |
|---|---|
| Program states consumed | $`N_{\mathrm{tot}}`$ copies of $`P/r`$ |
| Data systems returned | $`k`$ registers of $`n`$ qubits |
| Pair partial-swap gadgets | $`L=\sum_j(2b_j-1)N_j`$ |
| Variable rotations | $`L`$ |
| Gates with ideal rotations | $`O(Ln)`$ |
| Gates from a fixed universal set | $`O(L[n+\mathrm{polylog}(L/\epsilon)])`$ |
| Work in addition to data and the active program | One qubit, with the return accuracy specified above |
| Registers actively participating in one group | At most $`(b+1)n+1`$ qubits |
| Total retained quantum state with streamed programs | $`(k+1)n+1`$ qubits |
| Peak storage if all programs arrive before the data | $`(N_{\mathrm{tot}}+k)n+1`$ qubits |
| Source preparation cost | $`N_{\mathrm{tot}}C_{\mathrm{prep}}`$, if one copy costs $`C_{\mathrm{prep}}`$ |

The streamed count assumes the source can supply fresh independent copies during execution. It is an alternative delivery schedule, not a consequence of discarding used copies. If training ends before the targets arrive, the unused program copies must remain stored. The data-storage count includes inactive groups, since their inputs can be entangled with the group currently being processed.

Every controlled swap acts on explicitly selected registers. The construction assumes no QRAM, coherent lookup oracle, unknown preparation unitary or inverse preparation. A hardware geometry may add routing cost to the displayed gate count. Serializing the listed gates always gives a depth bound of the same order as their count; no architecture-independent depth or runtime advantage is asserted.

## 6. What the sample saving compares

Ordinary density matrix exponentiation implements one support reflection at copy cost $`O(r^2/\eta)`$. Implementing the $`k`$ reflections separately with $`\eta=\epsilon/k`$ therefore gives the explicit benchmark

```math
N_{\mathrm{independent\ DME}}
=O\!\left(\frac{r^2k^2}{\epsilon}\right).
```

For $`k\ge r`$, the grouped collective construction reduces this copy count by a factor of order $`r`$, while retaining its pair-gate order. This comparison concerns these stated constructions. The proof does not give an optimal lower bound for every processor that acts independently on targets or for every classical-estimation method.

The collective swap Hamiltonian is the [Hermitian-preserving map exponentiation interaction](../references/RELATED_WORK.md) for $`\rho\mapsto\sum_j\rho_j`$. The rank-sensitive collision analysis supplies its improved sample bound here. The source-preparation saving can matter when examples are expensive or must be retained, but it does not by itself establish an overall runtime saving. The output consists of $`k`$ data systems, and the full preparation, gate, storage and accuracy costs remain part of the comparison.

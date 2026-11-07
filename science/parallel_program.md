# The parallel program and its copy bound

Let $`P`$ be an unknown rank-$`r`$ orthogonal projector on $`\mathcal H=\mathbb C^d`$, with $`1\le r<d`$. One program specimen is $`\rho=P/r`$. There are $`k\ge1`$ data registers $`A_1,\ldots,A_k`$, each isomorphic to $`\mathcal H`$, and one fresh program register $`a`$. The data space is $`A=A_1\otimes\cdots\otimes A_k`$.

## The interaction and its moments

Write $`S_{a,j}`$ for the swap of the program with data register $`j`$, and $`S_{i,j}`$ for a swap between two data registers. All these are known Hermitian unitaries. The collective interaction is

```math
H_* = \sum_{j=1}^k S_{a,j}.
```

For a single-register operator $`B`$, let $`B_j`$ denote $`B`$ acting on $`A_j`$ and the identity on the other data registers. The Hamiltonian $`H_*`$ is the HME interaction for the linear Hermitian-preserving map $`\mathcal N(B)=\sum_jB_j`$. The HME construction, including earlier moment-sensitive refinements, is credited in [RELATED_WORK.md](../references/RELATED_WORK.md).

Use the data-first tensor order and the program expectation

```math
\mathcal E_\rho(Y)
=\operatorname{Tr}_a\!\left[(I_A\otimes\rho)Y\right]
```

defined in [collision_bound.md](collision_bound.md). The swap identities are

```math
\mathcal E_\rho(S_{a,j})=\rho_j,\qquad
\mathcal E_\rho(S_{a,i}S_{a,j})=\rho_jS_{i,j}\quad(i\ne j).
```

The order in the second identity matters. Operators act from right to left: the program first swaps with register $`j`$, then with register $`i`$. After the program expectation, the resulting operator maps $`|x\rangle_i|y\rangle_j`$ to $`|y\rangle_i\otimes\rho|x\rangle_j`$. This is $`\rho_jS_{i,j}`$. Reversing the two swaps gives $`\rho_iS_{i,j}`$.

Thus the first and second program moments are

```math
h=\mathcal E_\rho(H_*)=\sum_{j=1}^k\rho_j,
```

```math
M=\mathcal E_\rho(H_*^2)
=kI_A+\sum_{1\le i<j\le k}(\rho_i+\rho_j)S_{i,j}.
```

The pair factor $`\rho_i+\rho_j`$ commutes with $`S_{i,j}`$. Since $`\|\rho\|_\infty=1/r`$, the triangle inequality gives $`\|M\|_\infty\le k+k(k-1)/r`$. Equality is attained on $`|v\rangle^{\otimes k}`$ for any unit vector $`|v\rangle`$ in the range of $`P`$. Therefore

```math
\|M\|_\infty=k+\frac{k(k-1)}{r}.
```

## Exact variance

Define the support-count operator

```math
C_P=\sum_{j=1}^k P_j.
```

Its eigenvalues are the integers $`m=0,\ldots,k`$, and $`h=C_P/r`$. Every pair term in $`M`$ commutes with $`C_P`$. The positivity of $`P_i+P_j`$ and its commutation with the involution $`S_{i,j}`$ imply

```math
(P_i+P_j)S_{i,j}\le P_i+P_j.
```

Summing over all pairs yields the operator inequality

```math
M-h^2
\le kI_A+\frac{k-1}{r}C_P-\frac{1}{r^2}C_P^2.
```

The left side is positive by the collision lemma. In the sector with support count $`m`$, it is therefore bounded above by

```math
\left(k+\frac{(k-1)m}{r}-\frac{m^2}{r^2}\right)I_A.
```

Every sector bound is attained. Choose unit vectors $`|v\rangle\in\operatorname{ran}P`$ and $`|w\rangle\in\ker P`$. For a subset $`T\subseteq\{1,\ldots,k\}`$, define $`|x_j(T)\rangle=|v\rangle`$ when $`j\in T`$ and $`|x_j(T)\rangle=|w\rangle`$ otherwise. The normalized symmetric vector

```math
|D_{k,m}\rangle
=\binom{k}{m}^{-1/2}
\sum_{T:\,|T|=m}\bigotimes_{j=1}^k|x_j(T)\rangle
```

satisfies $`C_P|D_{k,m}\rangle=m|D_{k,m}\rangle`$ and $`S_{i,j}|D_{k,m}\rangle=|D_{k,m}\rangle`$ for every pair. It attains equality in the summed inequality above. The exact variance is consequently

```math
v_{r,k}:=\|M-h^2\|_\infty
=\max_{m\in\{0,\ldots,k\}}
\left(k+\frac{(k-1)m}{r}-\frac{m^2}{r^2}\right).
```

In particular,

```math
v_{r,k}\le k+\frac{k(k-1)}{r}.
```

The value is independent of the ambient dimension as long as both the range and kernel of $`P`$ are nonempty.

## Fresh collisions implement the product channel

For real $`\delta`$, one exact collective collision is

```math
\Phi_\delta(X)
=\operatorname{Tr}_a\!\left[
e^{-i\delta H_*}(X\otimes\rho)e^{i\delta H_*}
\right].
```

The intended one-step channel is $`\mathcal U_\delta(X)=e^{-i\delta h}Xe^{i\delta h}`$. The [variance lemma](collision_bound.md) gives

```math
\|\Phi_\delta-\mathcal U_\delta\|_\diamond
\le2\delta^2v_{r,k}.
```

Take $`N\ge1`$ fresh specimens, let $`t`$ be the total intended evolution time, and set $`\delta=t/N`$. After each collision, discard its program register. Independence of the fresh specimens gives the data channel $`\Phi_\delta^N`$. The data may acquire correlations during each collision; the diamond bound already includes them.

Telescoping the two channel products and using diamond norm one for every channel gives

```math
\|\Phi_{t/N}^N-\mathcal U_{t/N}^N\|_\diamond
\le N\|\Phi_{t/N}-\mathcal U_{t/N}\|_\diamond
\le\frac{2t^2v_{r,k}}{N}.
```

The embedded operators $`\rho_j`$ commute, so

```math
e^{-ith}=\bigotimes_{j=1}^k e^{-it\rho}.
```

At $`t=\pi r`$, each factor is $`e^{-i\pi P}=I-2P=R_P`$. Therefore

```math
\|\Phi_{\pi r/N}^N-\mathcal R_P^{(k)}\|_\diamond
\le\frac{2\pi^2r^2v_{r,k}}{N}
\le\frac{2\pi^2rk(r+k-1)}{N}.
```

This is one uniform guarantee for the joint output channel. It does not require a product input or separate marginal error estimates.

## Known pair gates and an explicit upper bound

The collective exponential is implemented by a symmetric sweep of known pair partial swaps. The sweep has $`2k-1`$ pair gates. Its operator error is at most $`k^3|\delta|^3/3`$; the full derivative-remainder argument and elementary-gate realization are in [resources.md](resources.md). This symmetric collision architecture has precedents in multipartite collision simulation, including [Cattaneo et al.](../references/RELATED_WORK.md).

Let $`\widehat\Phi_\delta`$ denote the collision channel obtained from this sweep, with its program discarded. Unitary-channel distance is at most twice the operator distance, and preparing or discarding a program cannot increase it. Over $`N`$ specimens at $`\delta=\pi r/N`$,

```math
\|\widehat\Phi_{\pi r/N}^N-\mathcal R_P^{(k)}\|_\diamond
\le\frac{2\pi^2rk(r+k-1)}{N}
+\frac{2\pi^3r^3k^3}{3N^2}.
```

For $`0<\epsilon\le1`$, choose

```math
N=\left\lceil\frac{4\pi^2rk(r+k-1)}{\epsilon}\right\rceil.
```

The first error term is at most $`\epsilon/2`$. The second is at most

```math
\frac{\epsilon^2}{24\pi}
\frac{rk}{(r+k-1)^2}
\le\frac{\epsilon^2}{24\pi}.
```

The last inequality holds because $`r+k-1\ge\max(r,k)\ge\sqrt{rk}`$. The total is less than $`\epsilon`$, proving the upper bound in [model.md](model.md). Known rotations are exact in this expression; the finite-precision implementation has an explicit separate error allocation in [resources.md](resources.md).

## Batching preserves the specimen order

Processing at most $`r`$ data registers with each shared program avoids an unnecessary large-block gate cost. Set $`q=\lceil k/r\rceil`$ and partition the data into $`q`$ groups of positive sizes $`b_1,\ldots,b_q`$ with $`b_j\le r`$ and $`\sum_jb_j=k`$. Every group size is at most $`b=\min(k,r)`$. Assign the ideal-rotation error $`\epsilon/q`$ to each group and use fresh specimens independently between groups. The group copy counts are

```math
N_j=\left\lceil
\frac{4\pi^2q r b_j(r+b_j-1)}{\epsilon}
\right\rceil.
```

The tensor product of these group channels is within $`\epsilon`$ of the full target channel by diamond-norm telescoping. This remains true when the input is entangled across groups.

Keeping the integer ceilings explicit gives

```math
N_{\mathrm{tot}}=\sum_{j=1}^qN_j
\le\frac{4\pi^2qr}{\epsilon}
\sum_{j=1}^q b_j(r+b_j-1)+q
\le\frac{4\pi^2q r k(r+b-1)}{\epsilon}+q.
```

For $`k<r`$, there is one group. For $`k\ge r`$, use $`qr\le k+r-1`$ and $`r+b-1=2r-1\le2r`$. Together these cases imply

```math
N_{\mathrm{tot}}
\le\frac{8\pi^2rk(r+k-1)}{\epsilon}+q.
```

Thus the copy order is $`O((r^2k+rk^2)/\epsilon)`$ for all positive $`k`$ and $`O(rk^2/\epsilon)`$ when $`k\ge r`$. The finite-gate construction uses group error $`\epsilon/(2q)`$ before synthesis, which doubles the coefficient in the displayed copy-count formula and reserves the remaining error for implementing the known rotations. Full gate, storage, source-preparation, and synthesis charges are given in [resources.md](resources.md).

The data registers within a group must be jointly available. Reusing a specimen during its short collision does not provide a returned catalyst or an online oracle for future adaptive inputs.

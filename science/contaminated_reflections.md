# Reflection programming from contaminated specimens

The program now consists of independent copies of

```math
\rho=\frac{a}{r}P+\eta\sigma,
\qquad
\eta=1-a,\qquad u=\frac{r\eta}{a},
```

where the rank $`1\le r\lt D`$ and the clean fraction $`0\lt a\le1`$ are known. The unknown contaminant $`\sigma`$ is a density operator, fixed in each instance. The target is the ordinary channel of the **clean** reflection $`R_P=I-2P`$ on $`k\ge1`$ jointly available data registers. The [clean model](model.md) defines the hard budget and the unhalved joint diamond norm. All $`N`$ specimens are supplied before the data arrive. The output averages over the processor's internal outcomes and includes its action on inputs entangled with a reference.

Let $`\Gamma_N(D,r,k,a)`$ be the smallest uniform channel error over all deterministic processors in this model. For $`N\ge1`$, uniformly in the other parameters,

```math
\begin{aligned}
\Gamma_N &\ge c\min\left\{1,ku+\frac{r^2+rk^2}{N}\right\},\\
\Gamma_N &\le C\min\left\{1,ku+\frac{r^2k+rk^2}{N}\right\},
\end{aligned}
```

where $`c,C\gt0`$ are universal constants. The bounds match in order for $`k=1`$ and $`k\ge r`$. The same intermediate-batch gap as in the clean model remains for $`1\lt k\lt r`$. In the matched regimes, a target error $`0\lt\epsilon\le1/8`$ requires the clean copy order, and that order also suffices when $`ku\le\epsilon/(4\pi)`$. The exact compatible-pair bound below can rule out an accuracy independently of $`N`$. These results leave open the copy cost at a vanishing margin above the optimal error floor.

## When two supports give the same program

Compatibility with $`P`$ means $`\rho\succeq (a/r)P`$. For equal-rank projectors $`P,Q`$ with principal angles $`\theta_i`$, a common density operator exists exactly when

```math
\sum_i\sin\theta_i\le u.
```

Indeed, write $`A=(a/r)P`$ and $`B=(a/r)Q`$. Any $`X`$ that dominates both satisfies $`\Vert A-B\Vert_1\le\mathrm{Tr}(X-A)+\mathrm{Tr}(X-B)`$. The operator $`B+(A-B)_+`$ dominates both and attains the resulting trace lower bound $`a+\Vert A-B\Vert_1/2`$. If its trace is at most one, add positive slack to complete it to a density operator. The principal-plane decomposition of $`P-Q`$ has the eigenvalue pairs $`\pm\sin\theta_i`$ for nonzero angles. This gives the stated condition, including $`a=1`$ where compatibility requires $`P=Q`$.

The relative reflection $`R_PR_Q`$ has eigenphases $`\pm2\theta_i`$ in the principal planes, and phase zero on any unchanged sector. Put $`\alpha=\arcsin(\min\{1,u\})`$. The eigenphases of its $`k`$-fold product have representatives in $`[-2k\alpha,2k\alpha]`$. If $`2k\alpha\le\pi/2`$, their convex hull has real part at least $`\cos(2k\alpha)`$. To convert this to channel distance, take an arbitrary pure data-reference input. The overlap of the two pure outputs is an expectation of the relative unitary, so belongs to that convex hull. The trace norm of their difference is $`2\sqrt{1-|\text{overlap}|^2}`$. Convexity extends the same upper bound to mixed inputs. For larger phases, the diamond distance is at most two.

The upper bound on pair distance is attained. Let the supports share $`r-1`$ directions and rotate the remaining direction by $`\min\{\alpha,\pi/(4k)\}`$. This pair is compatible by the criterion above. Use the equal superposition of the two extreme-phase tensor eigenvectors as the batch input. The overlap is the cosine of the corresponding half-width, which vanishes once the rotation reaches $`\pi/(4k)`$. Thus the maximum diamond separation of compatible targets is exactly $`2\sin(\min\{2k\alpha,\pi/2\})`$. This witness also works for a qubit, where complementary rays would instead give the same ordinary channel.

Both compatible instances supply $`\rho^{\otimes N}`$, so the processor returns the same channel on them. The triangle inequality forces

```math
\Gamma_N\ge\sin\!\left(\min\{2k\alpha,\pi/2\}\right).
```

Independently, the choice $`\sigma=P/r`$ recovers the clean program for every $`a`$. The [clean converses](model.md#the-copy-complexity-theorem) therefore give the second lower bound

```math
\Gamma_N\ge\min\left\{\frac18,\frac{9}{8\pi^2}\frac{\max\{r^2,rk^2\}}{N}\right\}.
```

The maximum of these two lower bounds has order $`\min\{1,ku+(r^2+rk^2)/N\}`$.

## Attaining the error order with collective swaps

Use the [same collective interaction](parallel_program.md) $`H_*`$ with one fresh program specimen at each step, and total evolution time $`t=\pi r/a`$. The exact first and second swap moments continue to hold for a general $`\rho`$. Write $`h=\sum_j\rho_j`$. Since $`(\rho_i+\rho_j)S_{i,j}\preceq\rho_i+\rho_j`$, the positive variance operator satisfies $`M-h^2\preceq kI+(k-1)h-h^2`$. Every eigenvalue $`s`$ of $`h`$ is a sum of $`k`$ eigenvalues of $`\rho`$. Symmetrizing a product of the corresponding eigenvectors preserves $`s`$ and attains equality in this operator bound on that vector. In particular, the scalar variance is bounded by

```math
v\le k+k(k-1)\Vert\rho\Vert_\infty\le k+k(k-1)(a/r+\eta)=:V.
```

From the [reduced-channel variance lemma](collision_bound.md), $`N`$ exact collisions at duration $`t/N`$ simulate the ordinary channel of $`U^{\otimes k}`$ to diamond error at most $`2t^2V/N`$, where $`U=e^{-i\pi(P+u\sigma)}`$. For comparison with the clean reflection, center $`\sigma`$ by subtracting $`I/2`$, which changes only the global phase of $`U`$. Duhamel's formula bounds the centered single-register operator error by $`\pi u/2`$. Passing to channels and telescoping over the parallel targets gives the additional diamond error $`\pi ku`$.

When $`ku\le1`$, we have $`a\ge1/2`$ and $`a/r+\eta\le2/r`$. Thus the variance term scales as $`(r^2k+rk^2)/N`$. The universal error cap of two covers the remaining regime and small $`N`$. [Wei et al.](https://arxiv.org/abs/2308.07956) already give perturbation bounds for the supplied states in Hermitian-preserving map exponentiation. Here the shared-swap variance retains the rank-sensitive copy term, and the compatible-pair converse makes the contamination dependence a minimax obstruction.

### Specimens, gates, and synthesis

Replace each exact collision by the [symmetric sweep](resources.md#2-a-symmetric-sweep-implements-the-collective-collision) with $`2k-1`$ known pair partial swaps. Its total additional diamond error is at most $`2t^3k^3/(3N^2)`$. If $`ku\le\epsilon/(4\pi)`$, choose

```math
N\ge\left\lceil
\max\left\{\frac{8t^2V}{\epsilon},
\sqrt{\frac{8t^3k^3}{3\epsilon}}\right\}
\right\rceil.
```

This allocates at most $`\epsilon/4`$ each to the contamination bias, exact collisions and sweep error. Synthesize each partial-swap rotation to operator error at most $`\epsilon/[8N(2k-1)]`$ to reserve the remaining channel error, including the work qubit, for synthesis. The square-root term is within the same copy order because $`r^3k^3\le[rk(r+k)]^2/4`$. There are $`N(2k-1)`$ pair partial swaps. For $`D=2^n`$, storing all early specimens requires $`Nn`$ qubits in addition to the data and work registers. One collision accesses $`k`$ data registers and one program register, with one work qubit using the stated gadget. Source preparation costs $`N`$ times the cost of one supplied contaminated specimen. Pair gates and finite-gate overhead use the same implementation as the [clean resource account](resources.md). The construction consumes its specimens and requires joint target access.

### The weak-contamination error floor

For $`u\lt1`$, the top $`r`$ eigenspace $`Q`$ of $`\rho`$ has a positive gap at the cut of at least $`a/r-\eta`$. In a principal plane of $`P,Q`$, let $`e_i`$ lie in $`Q`$ and $`f_i`$ in its orthogonal complement. The off-diagonal entry of $`\rho`$ vanishes, giving

```math
\sin(2\theta_i)=2u|\langle e_i|\sigma|f_i\rangle|.
```

The angles start at zero along the gapped path $`(a/r)P+s\eta\sigma`$, $`0\le s\le1`$. None reaches $`\pi/4`$: at that angle the same off-diagonal equation would force $`1\le su`$ because a positive trace-one matrix has $`|\langle e_i|\sigma|f_i\rangle|\le1/2`$. Hence $`\theta_i\le\arcsin(u)/2`$. When $`k\arcsin(u)\le\pi/2`$, reflecting about $`Q`$ gives error at most $`2\sin(k\arcsin u)`$ by the same spectral-arc argument. Uniform finite-dimensional tomography followed by top-subspace estimation approaches that bound as $`N\to\infty`$ at fixed $`D,r,k,a`$, since the gap is uniform over admissible instances.

The minimax error decreases with $`N`$ and has a limit. Its order is $`\min\{1,ku\}`$, and the small-$`ku`$ expansion of the lower and upper bounds gives the same leading term $`2ku[1+O((ku)^2)]`$. This limit concerns channel reconstruction. [Quantum Training Contamination](https://github.com/GoGoKo699/Quantum-Training-Contamination) obtains a different consequence for one clean test against a maximally mixed background. For rank one at fixed $`0\lt a\lt1`$, its optimal limiting recognition risk is of order $`d^{-1/2}`$ as the test dimension grows.

## An ordinary channel can supply a classifier

Consider rank one on a known hyperplane of dimension $`d=D-1\ge2`$ with a known vacuum direction orthogonal to it. Embed each contaminated training specimen into the hyperplane. The clean projector and contaminant both embed in the same way, so the fraction $`a`$ and every copy are preserved. One call to the ordinary processor, wrapped in the [known-eigenstate routing circuit](classification_transfer.md#a-known-eigenstate-turns-routing-into-control), induces a test effect with operator-norm error at most $`\epsilon/2`$ from the clean projector. The recognition background remains $`I_d/d`$ on the hyperplane. The contrast identity then bounds recognition excess by $`(1-1/d)\epsilon/2`$. If starting with a programmed batch, fixed inputs and discarded outputs on the extra registers give the same guarantee on one register.

[The exact recognition floor](https://github.com/GoGoKo699/Quantum-Training-Contamination/blob/c1b011f516a8b9d15b2674ed5d8d9bccc506f155/science/precision_floor.md) gives $`\epsilon\ge q_d(a)/(1-1/d)`$ for $`1/d\lt a\le1`$, where $`q_d(a)/2`$ is the recognition excess. For $`a\le1/d`$, the recognition error is $`1/2`$ and the bound is $`\epsilon\ge1`$. At fixed contamination the first bound tends to zero with increasing dimension, whereas the direct compatible-channel bound is dimension-independent. Channel accuracy tests every input and its reference, and the routed binary experiment tests one decision against a diffuse background. The route requires the known eigenstate and consumes one ordinary invocation. [The flat-rank recognition extension](https://github.com/GoGoKo699/Quantum-Training-Contamination/blob/main/science/flat_rank_training.md) and [its classification account](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/main/science/contaminated_training.md) give the corresponding training-risk statements.

## When only a classical record survives training

A classical-record programmer makes an arbitrary collective measurement of the $`N`$ specimens before the data arrive, discards every source-dependent quantum register and uses the recorded outcome to choose any data channel. The recorded outcomes are averaged before comparing the output channel with its ideal target. At singleton batch size and $`0\lt\epsilon\le1/8`$, this model requires $`\Omega(rD/\epsilon)`$ copies for all nontrivial ranks, including under contamination. Clean training at $`r\le D/2`$ has a matching upper bound. This yields the clean $`\Theta(D/r)`$ copy ratio relative to coherent retention in that rank range.

### Converse from the classical classifier

Choose the clean subfamily $`\sigma=P/r`$. The [existing routing](classification_transfer.md#exact-source-reductions-and-the-endpoint) transfers a classical-record programmer to a classifier with the same access order. Its copy-local source map acts before the classical measurement. The test-side routing and readout use the record and the later input. In classifier dimension $`d`$ with rank $`s`$, the excess is at most $`A_{d,s}\epsilon`$, where $`A_{d,s}=(1-s/d)/2`$.

[Theorem C3.1](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/997088928d85e363fbbed1a913d6fd9284ba643f/science/classical_compilation.md#theorem-c3-uniform-classical-precision) bounds excess divided by $`A_{d,s}`$ from below by $`d/(d+N/s+2\sqrt N)`$. Because $`2\sqrt N\le N/s+s\le N/s+d`$, the contrast cancels and

```math
N\ge\frac{sd}{2}(\epsilon^{-1}-2)\ge\frac{3sd}{8\epsilon}.
```

The vacuum route has $`(d,s)=(D-1,r)`$ if $`D\ge r+2`$. The occupied route has $`(d,s)=(D-1,r-1)`$ if $`D=r+1`$ and $`r\ge2`$. In that route, each input specimen is independently replaced by the known occupied direction with probability $`1/r`$, before the classical measurement. The remaining $`(D,r)=(2,1)`$ case follows in order from the clean pair converse.

### Constructive clean upper bound

For clean programs, apply the [O'Donnell–Wright collective tomography measurement](https://arxiv.org/html/1508.01907v2) to the $`N`$ early specimens. Let $`Q`$ be the top $`r`$ projector of the Hermitian estimate. Running the measurement after a common Haar-random basis rotation and undoing it on the classical record makes the projector distribution covariant. This random basis choice uses known operations and zero additional source specimens. The scaled closest-projector property and the expected squared Frobenius guarantee give

```math
L:=\mathbb E[r-\mathrm{Tr}(PQ)]\le\frac{2r^2(4D-3)}{N}.
```

The record selects $`R_Q`$ as the gate. Put $`\Delta=Q-P`$. The law of $`Q`$ at $`P`$ is invariant under every unitary that preserves $`P`$. Consequently $`\mathbb E\Delta`$ and $`\mathbb E\Delta^2`$ are scalar on each of the two blocks. The block traces of $`\mathbb E\Delta`$ are $`-L,L`$, and both block traces of $`\mathbb E\Delta^2`$ are $`L`$. Thus each operator norm equals $`L/\min(r,D-r)`$. On expanding the channel of $`R_Q=R_P-2\Delta`$, the two linear terms have combined diamond norm at most $`4\Vert\mathbb E\Delta\Vert_\infty`$. The quadratic term is completely positive and has diamond norm $`4\Vert\mathbb E\Delta^2\Vert_\infty`$. The unconditional diamond error is therefore at most $`8L/\min(r,D-r)`$, or $`O(rD/N)`$ for $`r\le D/2`$. This uses averaging of the channel itself. The bound does not impose a separate accuracy promise on each realized estimate, and the tomography and synthesized reflection can have substantial gate and classical computation costs.

### Matching contaminated upper bound for rank one

For $`r=k=1`$ and $`u\lt1/2`$, use the true top eigenprojector $`Q`$ of $`\rho`$ as an analysis benchmark. Its spectral gap $`g_0`$ is at least $`a-\eta\ge1/3`$ and its ideal reflection is within diamond error $`2u`$ of the clean one by the principal-angle estimate. With $`\widehat Q`$ the top ray of the tomography estimate $`\widehat\rho`$, spectral optimality gives

```math
\frac{g_0}{2}\Vert\widehat Q-Q\Vert_F^2
\le\mathrm{Tr}[\rho(Q-\widehat Q)]
\le\Vert\widehat\rho-\rho\Vert_F\Vert\widehat Q-Q\Vert_F.
```

Haar symmetrization implies invariance under the stabilizer of $`\rho`$, including the sign between $`Q`$ and its orthogonal complement. The mean $`\Delta=\widehat Q-Q`$ and mean square are block diagonal. Here $`\mathbb E\Delta`$ has a negative first and positive second block, and both blocks of $`\mathbb E\Delta^2`$ are positive. The magnitude of each block trace is $`\mathbb E[1-\mathrm{Tr}(Q\widehat Q)]\le 2(4D-3)/(Ng_0^2)`$. This bounds both operator norms even without rotational symmetry inside the complement. The same channel expansion then gives error $`O(D/N+u)`$. The cap of two covers $`u\ge1/2`$. Combined with the two lower bounds, the rank-one classical-record error is $`\Theta(\min\{1,u+D/N\})`$. In particular, $`\Theta(D/\epsilon)`$ copies suffice and are necessary when $`u\le\epsilon/4`$ and $`0\lt\epsilon\le1/8`$. A matching upper bound for contaminated higher-rank classical-record programming remains open.

[Schoute et al.](https://arxiv.org/abs/2411.03648v2) already analyze the clean pure-state measure-and-reflect construction. [Li et al., Section S5](https://arxiv.org/html/2605.21457v2#S5) prove a lower bound against all classical-first density-matrix exponentiation of a pure program at fixed time, including reflection at time $`\pi`$. The C3 transfer gives the uniform rank dependence for unlabeled flat mixed programs. The contaminated result concerns reflection about the latent clean component of the supplied state.

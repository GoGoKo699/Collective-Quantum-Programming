# A converse for every deterministic processor

Two nearby support projectors give program states that are difficult to distinguish. Their relative reflections nevertheless accumulate a detectable phase on an entangled batch. Repeating an accurate processor converts its channel guarantee into a discrimination experiment and forces a lower bound on the number of source specimens.

The reduction adapts the sample-to-query discrimination method used in rigorous sample-based Hamiltonian simulation, in particular [Go et al.](../references/RELATED_WORK.md). The family of flat-rank programs and the tensor-power phase accumulation determine the rank and batch-size dependence here.

## Statement

Let $`d\ge2`$, $`1\le r\lt d`$, $`k\ge1`$, and $`0\lt \epsilon\le1/8`$. Suppose a fixed deterministic processor with a hard budget of $`N`$ specimens of $`\rho_P=P/r`$ implements the ordinary channel $`\mathcal R_P^{(k)}`$ with unhalved diamond error at most $`\epsilon`$, uniformly over all rank-$`r`$ projectors $`P`$. The model includes arbitrary joint operations, ancillas, measurement feedforward, and entangled data inputs, as defined in [model.md](model.md).

**Theorem.** Every such processor satisfies

```math
N\ge\frac{9}{8\pi^2}\frac{rk^2}{\epsilon}.
```

## A nearby pair of program states

Fix an orthonormal basis $`|e_1\rangle,\ldots,|e_d\rangle`$ of $`\mathcal H=\mathbb C^d`$. For an angle $`0\le\theta\le\pi/2`$, define

```math
P_0=\sum_{j=1}^r|e_j\rangle\langle e_j|,\qquad
|v_\theta\rangle=\cos\theta\,|e_1\rangle
+\sin\theta\,|e_{r+1}\rangle,
```

```math
P_\theta=|v_\theta\rangle\langle v_\theta|
+\sum_{j=2}^r|e_j\rangle\langle e_j|.
```

The second sum is empty when $`r=1`$. Both projectors have rank $`r`$; the direction $`|e_{r+1}\rangle`$ exists because $`r\lt d`$. Write $`\rho_0=P_0/r`$ and $`\rho_\theta=P_\theta/r`$.

For states $`\alpha`$ and $`\beta`$, define the root fidelity and trace distance by

```math
f(\alpha,\beta)=\Vert\sqrt\alpha\sqrt\beta\Vert_1,\qquad
T(\alpha,\beta)=\frac12\Vert\alpha-\beta\Vert_1.
```

The nonzero singular values of $`P_0P_\theta`$ are $`r-1`$ copies of one and one value $`\cos\theta`$. Therefore the exact single-specimen root fidelity is

```math
f:=f(\rho_0,\rho_\theta)
=\frac{r-1+\cos\theta}{r}.
```

Root fidelity is multiplicative on tensor products. For any nonnegative integer $`L`$, the fidelity bound on trace distance gives

```math
T(\rho_0^{\otimes L},\rho_\theta^{\otimes L})
\le\sqrt{1-f^{2L}}
\le\sqrt{2L(1-f)}
\le\sqrt{\frac{L\theta^2}{r}}.
```

The middle inequality uses $`1-x^{2L}\le2L(1-x)`$ for $`0\le x\le1`$. The last uses $`1-\cos\theta\le\theta^2/2`$.

## The relative reflection accumulates phase

Let $`R_0=I-2P_0`$ and $`R_\theta=I-2P_\theta`$. The known comparison gate $`R_0`$ can be applied without any source specimen. On the two-dimensional span of $`|e_1\rangle`$ and $`|e_{r+1}\rangle`$, define the fixed orthonormal vectors

```math
|v_+\rangle=\frac{|e_1\rangle+i|e_{r+1}\rangle}{\sqrt2},\qquad
|v_-\rangle=\frac{|e_1\rangle-i|e_{r+1}\rangle}{\sqrt2}.
```

Direct multiplication of the two reflections yields

```math
R_0R_\theta|v_+\rangle=e^{2i\theta}|v_+\rangle,\qquad
R_0R_\theta|v_-\rangle=e^{-2i\theta}|v_-\rangle.
```

Prepare the fixed entangled batch

```math
|\Gamma\rangle
=\frac{|v_+\rangle^{\otimes k}+|v_-\rangle^{\otimes k}}{\sqrt2}.
```

After each invocation of the hypothetical processor, apply the known gate $`R_0^{\otimes k}`$. Under the $`P_0`$ hypothesis, one ideal processor invocation followed by this gate is the identity. Under the $`P_\theta`$ hypothesis, one ideal invocation applies $`(R_0R_\theta)^{\otimes k}`$.

Choose the number of invocations and the angle as

```math
m=\left\lfloor\frac{1}{4\epsilon}\right\rfloor,\qquad
\theta=\frac{\pi}{4km}.
```

The error range ensures $`m\ge2`$, so $`\theta\le\pi/8`$ lies in the required interval. After $`m`$ ideal invocations under $`P_\theta`$, the batch is

```math
|\Gamma_\theta\rangle
=\frac{e^{2ikm\theta}|v_+\rangle^{\otimes k}
+e^{-2ikm\theta}|v_-\rangle^{\otimes k}}{\sqrt2}.
```

Its overlap with the unchanged batch under $`P_0`$ is $`\langle\Gamma|\Gamma_\theta\rangle=\cos(2km\theta)=0`$. The two ideal outputs are therefore orthogonal.

This experiment needs ordinary reflections and a known comparison gate. It does not require a controlled unknown reflection or a supplied vacuum sector.

## Processor error and data processing

Each invocation receives $`N`$ fresh program specimens and uses a fresh implementation of the same processor. The total hard budget is $`Nm`$. Let $`\omega_0`$ and $`\omega_\theta`$ be the actual final data states, and let $`\gamma_0`$ and $`\gamma_\theta`$ be the corresponding ideal pure states. Diamond-norm telescoping gives, under either hypothesis,

```math
T(\omega_0,\gamma_0)\le\frac{m\epsilon}{2},\qquad
T(\omega_\theta,\gamma_\theta)\le\frac{m\epsilon}{2}.
```

The factors of one-half arise because the processor error uses the unhalved diamond norm, while $`T`$ is the conventional half trace norm. Since the ideal outputs are orthogonal, the triangle inequality gives

```math
T(\omega_0,\omega_\theta)
\ge1-m\epsilon\ge\frac34.
```

The entire repeated experiment is one hypothesis-independent CPTP map of the $`Nm`$ program specimens and the fixed initial batch. Its known comparison gates, internal measurements, classical records, and discarded systems do not alter trace-distance contractivity. Hence

```math
\frac34
\le T(\omega_0,\omega_\theta)
\le T(\rho_0^{\otimes Nm},\rho_\theta^{\otimes Nm})
\le\sqrt{\frac{Nm\theta^2}{r}}.
```

Substituting $`\theta=\pi/(4km)`$ and squaring yields

```math
N\ge\frac{9rk^2m}{\pi^2}.
```

Finally, $`1/(4\epsilon)\ge2`$ implies $`m\ge1/(8\epsilon)`$. Therefore

```math
N\ge\frac{9}{8\pi^2}\frac{rk^2}{\epsilon},
```

as claimed.

## Scope of the conclusion

The proof uses a hard specimen budget and an unconditional channel guarantee. It makes no restriction on the processor's internal measurement strategy or on whether its stored description is quantum or classical. A success-conditioned channel or an expected-copy budget would require a different statement.

All $`k`$ data registers are available during every invocation in the discrimination experiment. Repeating this parallel processor does not establish a construction for arbitrary sequential adaptive requests. The lower bound holds for every positive $`k`$, and matches the [upper bound](parallel_program.md) when $`k\ge r`$. It leaves the optimal dependence for $`k\lt r`$ unresolved.

# From Watrous to collective quantum programming

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. Use the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) and its **standard-layout manuscript**. Section, definition, theorem, and page numbers below refer to that manuscript's printed numbering, not the PDF viewer's page count. The author provides the manuscript for personal use; the links here point to that source.

Watrous supplies the language of states, reduced channels, fidelity, and reference-assisted distinguishability. This project uses that language to ask how many copies of an unknown state $`P/r`$ are needed to apply $`I-2P`$ to a batch of data registers. The [milestone map](MILESTONES.md) organizes the project's dependencies. The sections below supply the source-to-project translation without requiring the whole textbook as a preliminary assignment.

## Relevant parts of the source

| Foundation | Location in the standard manuscript | Use in this project |
|---|---|---|
| Tensor products, operators, and positive order | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §§1.1.1–1.1.2; tensor products on p. 6, projectors on p. 18, positive order on p. 21 | Separate program, data, and reference registers; interpret the unknown support projector. |
| Spectral decomposition and operator norms | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §1.1.3; Theorem 1.3 on p. 25, Schatten norms on pp. 32–34 | Turn the flat spectrum into a reflection and distinguish operator error from channel error. |
| States, reductions, and purifications | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.1.1–2.1.3, pp. 58–71; Definition 2.5 on p. 62 | Describe the mixed specimens and use a purification as an analytical representation. |
| Physical maps and their representations | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.2.1–2.2.2, pp. 72–90; Theorem 2.22 on p. 82 and Corollary 2.27 on p. 89 | Express a collision as an isometry followed by discarding an environment; identify its Kraus contributions. |
| Measurement effects and readout | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §2.3.1, pp. 100–101; Definition 2.34 | Turn the routed control readout into a binary effect and compare its risk with the known-support effect. |
| State discrimination and fidelity | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.1 and §§3.2.1–3.2.3; Definition 3.11 on p. 139, Proposition 3.16 on p. 143, Theorem 3.33 on p. 161 | Compare nearby programs, combine independent specimens, and bound their distinguishability. |
| Channel distance and composition | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §§3.3.2–3.3.3, pp. 166–184; Definition 3.43 on p. 170 and Proposition 3.48 on p. 174 | Keep the error valid with arbitrary reference entanglement and accumulate it through a circuit. |

These are foundations for the local arguments. The compressed-variance estimate, flat-program moment evaluation, parallel sample law, anchored classification transfer, and concrete gate budget are derived in the scientific pages linked below. The transfer uses the classification project's research-level precision theorem, rather than a textbook theorem about unknown projectors.

## Notation and normalization

| Watrous's convention | Convention used here |
|---|---|
| A vector $`u`$, its outer product $`uu^*`$, and an adjoint $`X^*`$ | $`\lvert u\rangle`$, $`\lvert u\rangle\langle u\rvert`$, and $`X^\dagger`$. These are changes of notation. |
| $`\mathrm L(\mathcal X)`$ and $`\mathrm D(\mathcal X)`$ | $`\mathsf L(A)`$ and $`\mathsf D(A)`$: operators and density operators on the indicated space. |
| A projection $`\Pi`$ onto a subspace | $`P`$ is the unknown support projector; $`\rho_P=P/r`$ is the supplied state. |
| Schatten norms $`\Vert X\Vert_1`$ and $`\Vert X\Vert_\infty`$ | The same trace and operator norms. The subscript identifies which norm is used. |
| Fidelity $`F(\rho,\sigma)`$ in Definition 3.11 | Root fidelity $`f(\rho,\sigma)=\Vert\sqrt\rho\sqrt\sigma\Vert_1`$. Thus $`F=f`$, not $`f^2`$. |
| Completely bounded trace norm $`\lvert\!\lvert\!\lvert\Phi\rvert\!\rvert\!\rvert_1`$ in Definition 3.43 | Diamond norm $`\Vert\Phi\Vert_\diamond`$, with no factor of one-half. |

The [model](../science/model.md) measures channel error by the unhalved diamond norm, while the [converse](../science/converse.md) writes state trace distance as $`T(\rho,\sigma)=\frac12\Vert\rho-\sigma\Vert_1`$. Consequently, for any input-reference state $`\omega`$,

```math
\Vert\Phi-\Psi\Vert_\diamond\le\epsilon
\quad\Longrightarrow\quad
T\!\left((\Phi\otimes\mathrm{id})(\omega),
         (\Psi\otimes\mathrm{id})(\omega)\right)
\le\frac{\epsilon}{2}.
```

Theorem 3.33 uses Watrous's root fidelity. In the local notation its upper trace-distance bound is $`T(\rho,\sigma)\le\sqrt{1-f(\rho,\sigma)^2}`$. These two normalization choices account for the factors of two in the converse.

## From states and channels to the program model

The textbook's compound registers let the entire batch be treated as one data system $`A=(\mathbb C^d)^{\otimes k}`$. A reference is a further system retained while the processor acts on $`A`$. The joint criterion therefore permits data entangled both within the batch and with that reference.

The project adds a specific source restriction: $`P`$ is unknown, its rank is known, and only independent copies of $`P/r`$ are supplied. Writing a density operator or a purification in a proof does not provide a physical preparation oracle. The [model](../science/model.md) states the actual access, chronology, hard specimen budget, and unconditional output requirement. Spectral calculus then explains the target: $`e^{-i\pi r\rho_P}=e^{-i\pi P}=I-2P`$.

## From channel representations to the variance bound

Corollary 2.27 identifies channels with isometric evolutions followed by a partial trace. For the [collision proof](../science/collision_bound.md), an analytical purification $`|s\rangle`$ of the mixed program gives an isometry $`V|x\rangle=|x\rangle|s\rangle`$. Extending the physical interaction by the identity on the purifying register gives $`\widehat H`$. The physical source still supplies only the mixed specimen.

The project compresses the interaction $`\widehat H`$ through this isometry. Its first two moments are $`h=V^\dagger\widehat H V`$ and $`M=V^\dagger\widehat H^2V`$. The positive operator

```math
M-h^2
=V^\dagger\widehat H(I-VV^\dagger)\widehat H V
```

measures coupling out of the fixed-program subspace. This is the bridge from channel representation to the local variance estimate. The proof separates the Kraus contribution that remains in that subspace from a completely positive leakage contribution. Both contribute at second order, giving $`\Vert\Phi_\tau-\mathcal U_\tau\Vert_\diamond\le2\tau^2\Vert M-h^2\Vert_\infty`$ for collision duration $`\tau`$. Here $`\Phi_\tau`$ is the reduced collision channel and $`\mathcal U_\tau`$ is the unitary channel generated by $`h`$. The interaction-picture estimate and its constant are supplied by the project, rather than by the representation theorem alone.

## From a shared specimen to the parallel law

The [parallel construction](../science/parallel_program.md) uses one fresh program register $`a`$ in the interaction $`H_* = \sum_j S_{a,j}`$, where $`S_{a,j}`$ swaps that register with target $`j`$. The program state is $`\rho=P/r`$, and the register is discarded after the collision. Its mean is $`h=\sum_j\rho_j`$, where $`\rho_j`$ acts as $`\rho`$ on target $`j`$ and as the identity on the other targets. The intended evolution therefore factors into the same operation on every target. The second moment contains cross terms whose norm is controlled by $`\Vert\rho\Vert_\infty=1/r`$. Evaluating those terms is the project-specific step that improves the copy count.

Proposition 3.48 supplies the composition rule needed to accumulate the collision errors. Its use is reference-stable: other targets can remain part of the reference while one group is processed. Fresh specimens give repeated copies of the same reduced channel; independent groups give a product of group channels. The resulting $`O((r^2k+rk^2)/\epsilon)`$ bound concerns the complete parallel output. Joint availability of the targets within a group remains part of the construction.

## From fidelity to the unrestricted converse

Proposition 3.16 and Theorem 3.33 convert a single-specimen root fidelity $`f`$ into the bound

```math
T(\rho_0^{\otimes L},\rho_\theta^{\otimes L})
\le\sqrt{1-f^{2L}}.
```

The [converse](../science/converse.md) supplies the nearby supports: one support direction is rotated into the complement, giving $`f=(r-1+\cos\theta)/r`$. It also supplies the discrimination experiment. A known comparison reflection and an entangled batch turn repeated ideal invocations into orthogonal outputs.

Channel composition bounds the error of the implemented experiment, while trace-distance contractivity limits what any processing of the source specimens can distinguish. Comparing these two bounds forces $`N=\Omega(rk^2/\epsilon)`$. The argument permits arbitrary deterministic processors because the complete experiment is a channel of the supplied programs. The rotated family and phase amplification specialize the research-level fidelity/query reduction to this task; they are not textbook results about a general unknown projector.

## From a classification converse to single-target optimality

Watrous's binary discrimination and channel-distance tools also connect programming to a different task. The [classification transfer](../science/classification_transfer.md) uses the all-rank finite-sample precision theorem [Q2 of Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/632fa8921e16b17dd5905b2e4f8d7f79d1570186/science/quantum_precision.md). That theorem is a research input owned by the classification account; the operational reduction and its programming consequence are developed here.

To keep the dimension conversion visible, call the programming dimension $`D`$ and the classification dimension $`d`$. First restrict to $`P=0_v\oplus Q`$ on $`\mathbb C|v\rangle\oplus\mathbb C^d`$, with $`D=d+1`$ and $`Q`$ of rank $`s=r\lt d`$. Every $`Q/r`$ training specimen embeds as one $`P/r`$ program. A controlled known swap routes either the later test or the known vacuum $`v`$ through the same ordinary reflection channel. Undoing the swap returns the vacuum in the ideal circuit and gives controlled $`R_Q`$ on the test. This is a known circuit around one ordinary-channel invocation, not control of an unknown black box. Preparing and discarding registers contract diamond distance, so the error remains $`\epsilon`$ with references and the hard budget remains $`N`$.

The control readout induces an effect $`M_Q`$ with $`\Vert M_Q-Q\Vert_\infty\le\epsilon/2`$. Binary discrimination retains the exact signed contrast between the class state and background:

```math
\begin{aligned}
R(M_Q,Q)-R_*
&=\frac12\operatorname{Tr}\left[(Q-M_Q)
\left(\frac Qs-\frac{I_d}{d}\right)\right]\\
&\le A_{d,s}\epsilon,
\qquad A_{d,s}=\frac{1-s/d}{2}.
\end{aligned}
```

Here $`R_*=s/(2d)`$ is the known-projector error and $`I_d/d`$ is the background on the classification space. The norm identity $`\Vert Q/s-I_d/d\Vert_1=4A_{d,s}`$ explains the last bound. Q2's precision lower bound has the same factor $`A_{d,s}`$. Its small-budget branch excludes $`N\lt s^2`$ for $`\epsilon\le1/2`$; its precision branch then gives

```math
A_{d,s}\epsilon\ge A_{d,s}\frac{s^2}{N+s^2}
\quad\Longrightarrow\quad
N\ge\left\lceil s^2(\epsilon^{-1}-1)\right\rceil.
```

The contrast cancels even when $`s/d`$ approaches one. Using only an absolute risk bound would miss this consequence.

If $`D=r+1`$ and $`r\ge2`$, fix a known occupied direction instead: $`P=|v\rangle\langle v|\oplus Q`$, with $`d=r`$ and $`s=r-1`$. Independently discard each supplied $`Q/s`$ copy and prepare $`v`$ with probability $`1/r`$, or embed it with probability $`s/r`$. This known channel produces exactly $`(P/r)^{\otimes N}`$ from a hard $`N`$-copy input. The vacuum's phase $`+1`$ is replaced by the known phase $`-1`$, corrected by a known control $`Z`$. The same argument yields the lower bound with $`s=r-1`$. The remaining $`(D,r)=(2,1)`$ case uses the pair converse above.

These cases and the construction close $`N_*(D,r,1,\epsilon)=\Theta(r^2/\epsilon)`$ for every $`1\le r\lt D`$ and $`0\lt\epsilon\le1/8`$. A batch can be padded down to one target with fixed extra inputs and discarded extra outputs, preserving $`N`$ and $`\epsilon`$. Combined with the pair converse, this gives the lower order $`(r^2+rk^2)/\epsilon`$, while the upper remains $`(r^2k+rk^2)/\epsilon`$. No additional factor $`k`$ follows from the single-test theorem. This remaining intermediate-batch gap is part of the result's scope.

## From channel accuracy to finite gates

The norm inequalities in §1.1.3 and the composition rule in Proposition 3.48 connect an implementation error to the promised output error. The [resource account](../science/resources.md) makes this connection explicit through $`\Vert\mathrm{Ad}_U-\mathrm{Ad}_V\Vert_\diamond\le2\Vert U-V\Vert_\infty`$, then allocates error among collisions, symmetric sweeps, and rotation synthesis.

The controlled-swap gadget, its returned work qubit, the sweep remainder, and the gate counts are developed in that account. Finite-gate synthesis uses the attributed Dawson–Nielsen result. Ideal rotations return the work qubit exactly; approximate synthesis controls its return jointly with the data-channel error. Source preparation and storage remain separately charged resources.

## Textbook foundations and research dependencies

Watrous is the single educational anchor. The [related-work account](../references/RELATED_WORK.md) retains the primary research dependencies: HME supplies the collective interaction and earlier moment-sensitive analysis, Go et al. supply the fidelity/query-discrimination method, Cattaneo et al. supply a relevant collective-collision architecture, and Dawson and Nielsen supply finite-gate compilation. The scientific pages establish matching specimen orders for $`k=1`$ and for $`k\ge r`$, uniformly over integers $`1\le r\lt d`$ and $`0\lt \epsilon\le1/8`$. The classification precision theorem supplies the transferred rank-squared converse; the pair-discrimination argument supplies the quadratic batch converse. Their exact model and constants remain the authoritative statements.

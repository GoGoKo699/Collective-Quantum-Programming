# Related work and contribution

A source supplies independent copies of $`\rho_P=P/r`$, where $`P`$ is an unknown rank-$`r`$ projector on $`\mathbb C^d`$ and $`1\le r\lt d`$. The task is to apply the ordinary reflection $`R_P=I-2P`$ to $`k`$ jointly available data registers. Accuracy is measured by the diamond norm of the complete output channel, including data entangled across registers and with a reference.

The collective construction gives

```math
N=O\!\left(\frac{r^2k+rk^2}{\varepsilon}\right)
```

program copies. A converse for arbitrary deterministic processors gives $`N=\Omega(rk^2/\varepsilon)`$. Consequently, for $`k\ge r`$ and $`0\lt \varepsilon\le1/8`$, the optimal sample cost is

```math
N_*(d,r,k,\varepsilon)
=\Theta\!\left(\frac{rk^2}{\varepsilon}\right).
```

The contribution is this rank-dependent parallel programming law and its resource realization. Its construction and converse build on sample-based simulation, Hermitian-preserving map exponentiation, collision models, and quantum-program discrimination. The distinctions below identify where those foundations enter and what the parallel law adds. Bibliographic metadata and version-specific references are collected in [references.bib](references.bib).

## Density matrix exponentiation

[Lloyd, Mohseni, and Rebentrost (2014)](https://doi.org/10.1038/nphys3029) introduced density matrix exponentiation: copies of an unknown state $`\rho`$ generate an approximation to $`e^{-it\rho}`$. [Kimmel et al. (2017)](https://doi.org/10.1038/s41534-017-0013-7) studied its optimal sample complexity and extensions to Hermitian polynomials of several program states. [Go et al. (2025), arXiv v3](https://arxiv.org/html/2412.02134v3) provide a rigorous nonasymptotic analysis in diamond distance, including explicit upper and lower bounds.

For $`\rho_P=P/r`$, evolution for time $`t=\pi r`$ gives $`e^{-it\rho_P}=R_P`$. Applying ordinary DME independently to $`k`$ targets, with error $`\varepsilon/k`$ per target, therefore uses $`O(r^2k^2/\varepsilon)`$ copies. This is the explicit independent-DME baseline. The collective law improves its copy count by a factor of order $`r`$ when $`k\ge r`$. The comparison concerns these constructions; it does not establish a lower bound on every processor constrained to operate its targets independently.

## HME supplies the collective interaction

[Wei et al. (2024)](https://doi.org/10.1038/s41534-024-00949-z) introduced Hermitian-preserving map exponentiation (HME). For a Hermitian-preserving linear map $`\mathcal N`$, their processor uses the interaction $`H=\mathrm{Choi}(\mathcal N)^{T_{\mathrm{in}}}`$ to simulate $`e^{-it\mathcal N(\rho)}`$. Taking $`\mathcal N(\rho)=\sum_{j=1}^k\rho_j`$ gives exactly

```math
H_\star=\sum_{j=1}^k\mathrm{SWAP}_{a,j},
```

where $`a`$ is the program register. Thus HME already supplies the interaction used here. Its generic $`O(t^2\Vert H\Vert_\infty^2/\varepsilon)`$ sample bound gives $`O(r^2k^2/\varepsilon)`$ for this choice.

State-sensitive improvements also have a direct HME precedent. Appendix C.2, Proposition 3 and Lemma 6 of the [2023 preprint, v1](https://arxiv.org/html/2308.07956v1#A3.SS2), improve the partial-transpose simulation bound from a quadratic to a linear factor in the transposed subsystem dimension. That analysis controls mixed higher moments and retains a marginal-state operator norm. The refinement here evaluates the compressed variance of $`H_\star`$ for $`P/r`$, producing the different dependence $`r^2k+rk^2`$. It uses this established approach to obtain the parallel programming law.

[Quantum Dynamic Programming](https://doi.org/10.1103/PhysRevLett.134.180602) also uses quantum states as programs for subsequent transformations. Its [v2 supplementary section II.2](https://arxiv.org/html/2403.09187v2) allows different program and output dimensions and imports the general HME norm bound. Its recursion-depth and memory tradeoff provides a broader computational setting for these processors.

## The converse uses program distinguishability

The lower bound compares two rank-$`r`$ projectors whose supports differ by a rotation of one direction. Their flat program states remain close, while repeated programmed reflections, interleaved with a known comparison reflection, amplify the rotation into a distinguishable phase. Diamond-norm accuracy controls the error of this discrimination procedure.

This proof follows the fidelity-versus-query-discrimination method in [Go et al., Lemma 7, v3](https://arxiv.org/html/2412.02134v3#S5.SS1). The task-specific step is the fixed-spectrum pair and its amplification across $`k`$ targets, which gives $`\Omega(rk^2/\varepsilon)`$. The general worst-case Hamiltonian-simulation theorem permits varying spectra and does not by substitution give this flat-program law. Go et al.'s Appendix E also refines controlled DME for an eigenstate input in quantum principal component analysis; that input-specific estimate has a different scope from a joint channel bound uniform over all target states.

## Collective collisions and gate implementation

A fresh ancilla interacting with several systems before being discarded is an established collision-model architecture. [Cattaneo et al. (2023)](https://doi.org/10.1103/PRXQuantum.4.010324), especially section III A and Appendix B of [arXiv v2](https://arxiv.org/pdf/2201.11597v2), use common ancillas and symmetric second-order interaction sweeps to simulate collective dissipative dynamics.

The implementation here specializes that architecture to partial swaps and charges the finite sweep error. Batching targets into groups of size at most $`r`$ retains the $`O(rk^2/\varepsilon)`$ sample order for $`k\ge r`$ while using $`O(r^2k^2/\varepsilon)`$ pair interactions, the same leading order as the independent-DME construction. Standard finite-gate compilation adds a polylogarithmic synthesis overhead; [Dawson and Nielsen (2006)](https://arxiv.org/abs/quant-ph/0505030v2) give a suitable conservative guarantee. The sample saving does not by itself imply a reduction in total interaction time.

## Programmable reflections and coherent inference

[Schoute et al., *Quantum Programmable Reflections*, v2 (2026)](https://arxiv.org/abs/2411.03648v2), study one data-register reflection programmed by identical pure states. Their Theorem 2.8 optimizes a specified class of processors built from unitary linear combinations of permutations. Here the program is mixed, its rank is a resource parameter, and the output is a globally accurate channel on several data registers. Pure-state programming is the $`r=1`$ boundary, where the collective sample law remains quadratic in $`k`$.

[Li et al., *An Exponential Sample-Complexity Advantage for Coherent Quantum Inference*, v2 (2026)](https://arxiv.org/html/2605.21457v2), establish coherent-processing advantages for several quantum-output tasks. Their many-output results include purity amplification and random purification or cloning; section S5 treats DME on an auxiliary target. Those results motivate retaining specimens coherently. The result here determines the joint reflection-channel cost as rank and output number vary; it does not supply a universal comparison against classical compilers.

Approximate program recycling is also established. [Yang, Renner, and Chiribella (2020; arXiv v3, 2021)](https://arxiv.org/abs/2007.10363v3) relate universal programming, estimation, and repeated program use. Their optimized resource is program dimension, with general encoded programs. The present source instead fixes the encoding to iid copies of $`P/r`$ and asks for their minimum count under a global output criterion.

## Relation to flat-subspace classification

[Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/tree/632fa8921e16b17dd5905b2e4f8d7f79d1570186) studies the same flat training source followed by one test from either $`P/r`$ or the known background $`I/d`$. At the cited revision, its [precision theorem](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/632fa8921e16b17dd5905b2e4f8d7f79d1570186/science/quantum_precision.md) gives $`\Theta(r^2/\varepsilon)`$ coherent training copies for excess classification risk, uniformly for $`1\le r\le d/2`$ and $`0\lt \varepsilon\le1/8`$. Its [construction](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/632fa8921e16b17dd5905b2e4f8d7f79d1570186/science/constructions.md) already uses a controlled support reflection.

That single-test rank law and attaining reflection construction are antecedents. The present result supplies a coherent channel on $`k`$ data registers, identifies the sample saving from collective programming, and proves the optimal order when $`k\ge r`$. Its upper bound requires all targets in each batch to be available together. A processor accepting an arbitrary sequence of adaptive future inputs is a separate task, and a matching sample law throughout $`k\lt r`$ is not established here.

# A worked route through the batch law

A source can prepare specimens of a state whose supporting subspace is unknown. We want those specimens to control a coherent operation on other quantum systems. The operation is simple to describe: reverse the phase inside that subspace and preserve the phase outside it. The resource question is how many specimens a whole batch of inputs consumes.

Follow this route alongside the [30 milestones](MILESTONES.md). The [Watrous bridge](ANCHOR.md) identifies the relevant sections of the single educational anchor, *The Theory of Quantum Information* (2018), and translates its notation. The scientific pages linked below contain the full statements and proofs.

## 1. From a specimen to an operation

**Milestones [M01–M06](MILESTONES.md#m01).** Let $`P`$ be an orthogonal projector of known rank $`r`$ on a $`d`$-dimensional register. A specimen has density operator $`\rho_P=P/r`$. It assigns equal weight to every direction in the range of $`P`$, and zero weight to its orthogonal complement. Its trace is one because $`\mathrm{Tr}\,P=r`$.

The desired unitary is $`R_P=I-2P`$. A vector in the range of $`P`$ acquires phase $`-1`$; a vector in the complement acquires phase $`+1`$. The ordinary channel acts on a density operator $`X`$ as $`X\mapsto R_PXR_P`$. A common phase on the entire vector cancels in this expression, while a relative phase between its components can change the state.

The processor receives $`N`$ independent specimens of the same unknown $`P/r`$ and $`k`$ data registers. It may perform joint operations, use ancillas, measure and use the measurement records. Its complete output, averaged over all internal outcomes, must be accurate. A channel representation that introduces a purification helps prove this property; it does not supply an extra physical resource to the processor. The [model](../science/model.md) states the access and output contract.

## 2. Why the guarantee is about the whole batch

**Milestones [M07–M12](MILESTONES.md#m07).** The data registers may be entangled with each other and with an external system retained by someone else. A correct processor must preserve the promised operation on these correlations as well as on each register separately. The sample bounds below assume $`1\le r\lt d`$, $`k\ge1`$ and $`0\lt \epsilon\le1/8`$.

Write $`\mathcal E_{P,N}`$ for its implemented batch channel and $`\mathcal R_P^{(k)}`$ for the ideal channel of $`R_P^{\otimes k}`$. The requirement is

```math
\sup_{\mathrm{rank}\,P=r}
\Vert\mathcal E_{P,N}-\mathcal R_P^{(k)}\Vert_\diamond
\le\epsilon.
```

The diamond norm allows an arbitrary reference at the input. This project uses its unhalved convention. Therefore, for any particular input-reference state, the conventional trace distance between the two outputs is at most $`\epsilon/2`$. This conversion matters in the lower bound.

The input resource is a hard budget of independent specimens. Knowing $`r`$ does not reveal the support basis, and a formula for $`P/r`$ does not provide a preparation unitary or its inverse. All $`k`$ data registers are available for the parallel task. The construction may divide them into groups, but each group's members must be present together.

## 3. One concrete two-target example

**Milestones [M13–M15](MILESTONES.md#m13).** Take $`d=3`$, $`r=2`$ and $`k=2`$. For explaining the action, choose coordinates in which

```math
P=\mathrm{diag}(1,1,0),\qquad
\rho_P=\mathrm{diag}(1/2,1/2,0),\qquad
R_P=\mathrm{diag}(-1,-1,1).
```

The implementation is not supplied these coordinates. Its gates are swaps, which work for every orientation of the unknown support.

For the entangled data state $`|\psi\rangle=(|00\rangle+|12\rangle)/\sqrt2`$ in the basis $`|0\rangle,|1\rangle,|2\rangle`$, the two-target reflection gives

```math
R_P^{\otimes2}|\psi\rangle
=\frac{|00\rangle-|12\rangle}{\sqrt2}.
```

The component with both targets in the support acquires two minus signs. The component with only the first target in the support acquires one. Their relative sign changes, and the output is orthogonal to the input. This is one illustrative input; the theorem must control every input and reference.

Let $`S_{a,j}`$ swap the program register $`a`$ with target $`j`$. One collective collision uses the known interaction $`H_*=S_{a,1}+S_{a,2}`$. Averaging over the specimen gives the effective data Hamiltonian

```math
h=\rho_{P,1}+\rho_{P,2},\qquad
e^{-i\pi r h}=R_P^{\otimes2}.
```

Here $`\rho_{P,j}`$ acts on target $`j`$ and as the identity on the other target. The two terms commute. Each eigenvalue $`1/r`$ therefore acquires phase $`e^{-i\pi}=-1`$ after time $`\pi r`$.

A finite collision also fluctuates around this mean action. Define $`M`$ as the program expectation of $`H_*^2`$ and $`v=\Vert M-h^2\Vert_\infty`$. In an analytical purification, this variance measures the coupling out of the subspace in which the purified environment remains fixed.

## 4. Turning local error into a specimen count

**Milestones [M16–M20](MILESTONES.md#m16).** The [collision lemma](../science/collision_bound.md) proves, for every real collision duration $`\delta`$,

```math
\Vert\Phi_\delta-\mathrm{Ad}_{e^{-i\delta h}}\Vert_\diamond
\le2\delta^2v.
```

The proof uses an analytical purification and divides the joint evolution into its projection onto the fixed-environment subspace and its orthogonal contribution. After removing the intended mean evolution, the compressed change vanishes to first order; the leakage probability is also quadratic. Both terms are bounded in a way that retains an arbitrary reference. This is why the inequality controls the whole reduced channel, beyond a formal expansion of its first derivative.

For our two-target example, the [exact variance formula](../science/parallel_program.md#exact-variance) becomes

```math
v_{2,2}=\max_{m\in\{0,1,2\}}
\left(2+\frac m2-\frac{m^2}{4}\right)
=\frac94.
```

The integer $`m`$ counts data factors lying in the support sector. The values are $`2`$, $`9/4`$ and $`2`$. This calculation shows how the actual program state enters the bound; replacing it by the interaction norm alone would lose that information.

Use a fresh specimen for each of $`N`$ collisions and set $`\delta=\pi r/N`$. Channel errors add under composition, so the total collision contribution is at most

```math
N\,(2\delta^2v)=\frac{2\pi^2r^2v}{N}.
```

For the example above this is $`18\pi^2/N`$. For general $`r,k`$, the proved inequality $`v\le k+k(k-1)/r`$ gives the order $`(r^2k+rk^2)/N`$. Sharing a specimen introduces target correlations, but the same global error bound already accounts for them.

The collective exponential also needs implementation. A symmetric sweep of known pair partial swaps matches it through second order. The [resource proof](../science/resources.md#2-a-symmetric-sweep-implements-the-collective-collision) bounds the remainder for every step size. Including that error, exact known rotations give the explicit sufficient budget

```math
N=\left\lceil\frac{4\pi^2rk(r+k-1)}{\epsilon}\right\rceil.
```

The variance estimate controls the source-induced error. The sweep estimate separately controls how the known interaction is implemented. Combining both is necessary for this constructive bound.

## 5. Real gates and the size of a group

**Milestones [M21–M22](MILESTONES.md#m21).** When $`k`$ is much larger than $`r`$, one need not make every specimen touch every target. Split the targets into $`q=\lceil k/r\rceil`$ groups, each of size at most $`r`$. Allocate the channel error across all groups, retaining other targets as references while a group is processed. The [finite-gate allocation](../science/resources.md#4-group-size-finite-gates-and-the-final-error) reserves half of the final error for the group constructions and half for rotation synthesis.

The pair-gate construction from [M19](MILESTONES.md#m19) implements a partial swap $`e^{-i\alpha S}`$ by coherently recording the swap eigenvalue in one work qubit, applying a known phase rotation, and uncomputing that record. Ideal rotations return the work qubit exactly. Finite-gate synthesis gives a small joint error, including the work qubit; comparing the complete gadget unitaries permits that same work qubit to be reused.

This preserves the sample order and uses $`O(r^2k^2/\epsilon)`$ pair partial swaps. A register occupies $`\lceil\log_2d\rceil`$ qubits, and synthesizing the rotations has an additional precision cost. Source preparation and storage also matter: specimens supplied throughout execution can be streamed, while specimens supplied only before the data arrive must be retained. The [resource account](../science/resources.md#5-copy-gate-and-memory-counts) separates these quantities.

## 6. Why every processor pays a quadratic batch cost

**Milestones [M23–M26](MILESTONES.md#m23).** For a lower bound, compare two possible sources. Start from a rank-$`r`$ support and rotate just one support direction through angle $`\theta`$ into its complement. The resulting flat states have root fidelity

```math
f(\rho_0,\rho_\theta)=\frac{r-1+\cos\theta}{r}.
```

For small $`\theta`$, the sources are very similar. Tensor-product fidelity and the trace-distance bound from Watrous imply that $`Nm`$ specimens obey

```math
T(\rho_0^{\otimes Nm},\rho_\theta^{\otimes Nm})
\le\sqrt{\frac{Nm\theta^2}{r}}.
```

Now suppose an accurate $`N`$-specimen processor is available. After each use, apply a known comparison reflection corresponding to the first support. Under that source the ideal combined operation is the identity. Under the rotated source it is a rotation with eigenphases $`\pm2\theta`$ in a two-dimensional subspace.

An entangled superposition of $`k`$ copies of the two eigenvectors multiplies their relative phase by $`k`$. Repeating the experiment with $`m`$ fresh processor instances multiplies it by $`m`$. Choose

```math
m=\left\lfloor\frac1{4\epsilon}\right\rfloor,
\qquad \theta=\frac{\pi}{4km}.
```

The ideal final outputs are orthogonal. Under each source hypothesis, the actual output is within conventional trace distance $`m\epsilon/2`$ of its ideal output. Thus the two actual outputs have trace distance at least $`1-m\epsilon\ge3/4`$.

Yet the complete experiment is a fixed channel of the supplied program specimens. Such processing cannot increase their distinguishability. Comparing the last two bounds forces

```math
N\ge\frac{9}{8\pi^2}\frac{rk^2}{\epsilon}.
```

The [full converse](../science/converse.md) gives the basis vectors, phase calculation and constants. Its force comes from the unconditional channel guarantee and hard specimen budget, so it includes processors with internal measurements and feedforward. The known comparison reflection is not a controlled unknown operation.

## 7. A classifier closes the single-target cost

**Milestone [M27](MILESTONES.md#m27).** The pair converse measures how one rotating support direction affects a coherent batch. A different argument detects the rank-squared cost already present for a single target. Its statistical input is the classification project's all-rank theorem Q2; the [transfer proof](../science/classification_transfer.md) gives the full reduction and constants.

For a concrete vacuum example, take programming dimension $`D=4`$, rank $`r=2`$, and a known vector $`v`$ in the kernel. The unknown projector is $`P=0_v\oplus Q`$, where $`Q`$ has rank two in a three-dimensional space $`W`$. Each supplied classification specimen $`Q/2`$ embeds into the programmer as one specimen $`P/2`$. The classification test arrives later, from $`Q/2`$ or $`I_W/3`$ with equal priors. No new examples arrive after that test.

Initialize the programmer's data register in $`v`$. A control in $`|+\rangle`$ coherently routes either the test or $`v`$ through one ordinary reflection invocation, using controlled known swaps before and after it. Since $`R_Pv=v`$, one branch preserves the test and the other applies $`R_Q`$. The routing register returns to $`v`$ ideally. This circuit uses the ordinary channel on both branches; it assumes no controlled unknown oracle. Its known pre- and postprocessing preserve the hard budget $`N`$ and cannot increase the unhalved diamond error $`\epsilon`$.

A Hadamard readout of the control is ideally the support measurement $`Q`$. The actual effect $`M_Q`$ obeys $`\Vert M_Q-Q\Vert_\infty\le\epsilon/2`$. The classification oracle error is $`R_*=1/3`$, and its available advantage is $`A=(1-2/3)/2=1/6`$. Keeping that contrast gives

```math
\begin{aligned}
R(M_Q,Q)-R_*
&=\frac12\operatorname{Tr}\left[(Q-M_Q)
\left(\frac Q2-\frac{I_W}{3}\right)\right]\\
&\le A\epsilon.
\end{aligned}
```

Q2 says every classifier with $`N\ge4`$ has excess risk at least $`4A/(N+4)`$. Its small-budget branch rules out $`N\lt4`$ for the required tolerance when $`\epsilon\le1/2`$. Therefore

```math
A\epsilon\ge\frac{4A}{N+4}
\quad\Longrightarrow\quad
N\ge\left\lceil4(\epsilon^{-1}-1)\right\rceil.
```

The same calculation for classification dimension $`d=D-1`$ and rank $`s=r`$ gives $`N\ge\lceil r^2(\epsilon^{-1}-1)\rceil`$ whenever $`D\ge r+2`$. The factor $`A_{d,s}=(1-s/d)/2`$ cancels exactly, so no low-rank restriction is needed. The background remains $`I_d/d`$, not $`I_D/D`$.

The codimension-one endpoint needs another anchor. If $`D=r+1`$ and $`r\ge2`$, fix $`P=|v\rangle\langle v|\oplus Q`$ with $`Q`$ of rank $`s=r-1`$ in dimension $`d=r`$. From each supplied $`Q/s`$ copy, output $`v`$ with probability $`1/r`$ and otherwise embed the copy. These independent known channels produce exactly the required $`N`$ program copies and never use more than $`N`$ training copies. Routing through the known eigenvalue $`-1`$ and correcting its phase by a known control $`Z`$ gives the same argument with $`s=r-1`$. The pure qubit case uses the preceding pair converse. Thus the single-target order is $`\Theta(r^2/\epsilon)`$ uniformly for all nontrivial ranks and dimensions.

An alternative flagged construction makes the dimension increase explicit: for a rank-$`s`$ classification projector in dimension $`d`$, the projector $`|1\rangle\langle1|\otimes Q`$ has rank $`s`$ in dimension $`2d`$. Its ordinary reflection is controlled $`R_Q`$. Appending its known flag consumes one training copy per program copy. This is an enlarged-dimension reduction, not a generic same-dimension conversion from an ordinary unknown channel to its controlled version.

## 8. Putting the contribution together

**Milestones [M27–M30](MILESTONES.md#m27).** For $`1\le r\lt d`$ and $`0\lt \epsilon\le1/8`$, the upper order is $`(r^2k+rk^2)/\epsilon`$ and the lower order is $`(r^2+rk^2)/\epsilon`$. They match at $`k=1`$ and when $`k\ge r`$. For $`1\lt k\lt r`$ a gap remains, bounded in order by $`\min\{k,r/k\}`$ and largest near $`k\asymp\sqrt r`$. Padding a batch with fixed inputs and discarding extra outputs transfers the single-target lower bound unchanged; it does not multiply it by $`k`$.

Separate density matrix exponentiation at error $`\epsilon/k`$ per target uses $`O(r^2k^2/\epsilon)`$ specimens. The large-batch construction improves that explicit bound by a factor of order $`r`$. Its pair-gate order remains $`O(r^2k^2/\epsilon)`$, so a specimen saving alone does not establish a runtime saving. At $`r=d`$ the desired ordinary channel is already the identity and consumes no specimens.

HME supplies the collective interaction; previous work supplies moment-sensitive analysis, collision architectures and the fidelity/query method. The [related-work account](../references/RELATED_WORK.md) makes those dependencies explicit. The result here combines a rank-sensitive construction, the fidelity-based batch converse, the classification-derived single-target converse, and an implementation whose resources are charged. Q2 remains the classification project's statistical result; the anchored reduction explains its ordinary-channel programming consequence. The [scientific index](../science/README.md) gives the complete proof route, and the [finite checks](../verification/README.md) illustrate the matrix identities without replacing their proofs.

# Thirty milestones for Collective Quantum Programming

The project asks how independent specimens of an unknown flat state can program the same reflection on a jointly available batch. This map connects the mathematical objects, the physical input and output, the constructive upper bound, and the converse into one account. The [scientific model](../science/model.md) remains the authoritative statement of the task and theorem.

The allocation is **12 milestones in background/preliminaries** and **18 in narrative/innovation**. The background connects states, channel representations, distinguishability, and reference-stable error to the complete programming contract. The narrative needs more space because the variance mechanism, its gate implementation, and the independent discrimination argument must meet in the same resource theorem. Each phase ends by integrating its preceding components. The map covers the project's main understanding targets; detailed calculations remain in the linked proofs.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Section numbers below refer to the author's standard-layout manuscript. [ANCHOR.md](ANCHOR.md) supplies the notation bridge and distinguishes textbook foundations from the project's own derivations. References to HME, DME, collision simulation, and gate synthesis point separately to the project's [primary-source comparison](../references/RELATED_WORK.md).

Dependencies refer only to earlier milestone IDs. They describe mathematical and conceptual prerequisites. The symbols introduced along the route agree with the scientific account: $`d`$ is the register dimension, $`r`$ is the known program rank, $`k`$ is the number of data registers, $`N`$ is the hard specimen budget, and $`\epsilon`$ is the unhalved diamond-error allowance.

## Background/preliminaries: M01–M12

<a id="m01"></a>

### M01. States, support, and a flat spectrum

**Central question.** What information is fixed, and what remains unknown, in a state of the form $`\rho_P=P/r`$?

**Understanding target.** Interpret a density operator as a positive operator of trace one, a projector $`P`$ as a subspace, and $`r`$ as its dimension. Explain why $`P/r`$ has a known flat nonzero spectrum while its supporting subspace can remain unknown.

**Dependencies and story role.** None. This introduces the local object from which every program specimen is drawn.

**Conceptual connection.** The spectrum normalizes the source and sets a scale for its dynamics; knowing that spectrum does not supply the basis needed to describe the target operation classically.

**Sources.** Anchor: Watrous [§1.1.2][W1] and [§2.1.2][W2]. Project: [source, processor, and output](../science/model.md#source-processor-and-output).

<a id="m02"></a>

### M02. A reflection as a quantum channel

**Central question.** What does the reflection $`R_P=I-2P`$ do to a state, and which of its phases are observable?

**Understanding target.** Explain the opposite phases on the range and kernel of $`P`$, the channel $`X\mapsto R_PXR_P`$, and the cancellation of a global unitary phase. Distinguish this ordinary channel from a controlled reflection.

**Dependencies and story role.** [M01](#m01). This turns the unknown subspace into a concrete local operation before introducing a batch.

**Conceptual connection.** The same projector specifies both the supplied mixed state and the desired coherent action. The channel description also explains the zero-specimen endpoint when $`r=d`$.

**Sources.** Anchor: Watrous [§1.1.2][W1] and [§2.2.1][W2]. Project: [target channel](../science/model.md#source-processor-and-output) and [endpoints](../science/model.md#availability-and-endpoints).

<a id="m03"></a>

### M03. Composite registers, reductions, and references

**Central question.** What must be retained in the description when the program interacts with several possibly entangled targets?

**Understanding target.** Identify the data space $`A=(\mathbb C^d)^{\otimes k}`$, the program register, and an inaccessible reference $`Z`$. Explain tensor products, entanglement, and the partial trace used to discard a program without discarding the data correlations it created.

**Dependencies and story role.** [M01](#m01), [M02](#m02). This expands a local operation into the composite physical setting of the project.

**Conceptual connection.** Independent source specimens do not imply independent target outputs. Reduced dynamics must preserve the distinction between an environment that is discarded and a reference against which accuracy is evaluated.

**Sources.** Anchor: Watrous [§1.1.1][W1] and [§§2.1.1, 2.1.3][W2]. Project: [joint accuracy](../science/model.md#joint-accuracy) and [the collision channel](../science/collision_bound.md#lemma).

<a id="m04"></a>

### M04. Deterministic processors and quantum channels

**Central question.** How can one mathematical map include joint gates, measurements, classical randomness, and discarded systems?

**Understanding target.** Interpret a completely positive, trace-preserving map as the unconditional physical processor. Explain why complete positivity includes entangled inputs and why retaining all outcome branches differs from guaranteeing accuracy only after a successful postselection.

**Dependencies and story role.** [M02](#m02), [M03](#m03). This establishes the admissible operations and the object to which both bounds apply.

**Conceptual connection.** The upper bound constructs one allowed channel; the converse constrains every allowed channel. Internal measurement choices do not create an exception to a uniform unconditional guarantee.

**Sources.** Anchor: Watrous [§2.2.1][W2]. Project: [processor definition](../science/model.md#source-processor-and-output) and [converse scope](../science/converse.md#scope-of-the-conclusion).

<a id="m05"></a>

### M05. Purification and channel representations

**Central question.** How can a mixed program and its reduced channel be analyzed using a pure environment and an isometry?

**Understanding target.** Relate purification, Kraus operators, and an isometric dilation followed by a partial trace. Understand the proof isometry $`V`$ that appends a fixed purification, while keeping separate the mathematical representation and the physical program access actually supplied.

**Dependencies and story role.** [M03](#m03), [M04](#m04). This supplies a common representation for coherent evolution and its discarded-environment branches.

**Conceptual connection.** The collision proof separates a compressed Kraus operator from leakage. Introducing a purification for this argument does not grant the processor a purification oracle.

**Sources.** Anchor: Watrous [§2.1.3][W2] and [§2.2.2][W2]. Project: [conditional expectation and variance](../science/collision_bound.md#conditional-expectation-and-variance) and [channel decomposition](../science/collision_bound.md#proof).

<a id="m06"></a>

### M06. Operator norms and positive operator bounds

**Central question.** Which operator estimates can control a physical error without introducing a dimension factor?

**Understanding target.** Distinguish the operator norm $`\|\cdot\|_\infty`$ from the trace norm $`\|\cdot\|_1`$. Use positive-operator order, the largest eigenvalue of a positive operator, unitary invariance, and trace-norm product bounds to interpret compression and leakage estimates.

**Dependencies and story role.** [M01](#m01), [M05](#m05). This introduces the quantitative language used in both the local channel estimate and the exact variance calculation.

**Conceptual connection.** A bound on a compressed operator can remain much smaller than a bound on the full interaction. Positivity makes that difference usable in a channel estimate.

**Sources.** Anchor: Watrous [§§1.1.2–1.1.3][W1]. Project: [variance positivity](../science/collision_bound.md#conditional-expectation-and-variance) and [operator estimates in the proof](../science/collision_bound.md#proof).

<a id="m07"></a>

### M07. Trace distance and binary discrimination

**Central question.** How does distance between two states limit the ability to tell them apart?

**Understanding target.** Interpret $`T(\alpha,\beta)=\tfrac12\|\alpha-\beta\|_1`$ through optimal binary discrimination. Explain its contractivity under a fixed channel and keep its factor of one-half distinct from the project's unhalved channel-error convention.

**Dependencies and story role.** [M04](#m04), [M06](#m06). This gives an operational meaning to a state-distance bound.

**Conceptual connection.** A processor cannot turn nearly indistinguishable program states into easily distinguishable outputs unless enough specimens were supplied. This principle will constrain all possible implementations.

**Sources.** Anchor: Watrous [§3.1.1][W3]. Project: [program-state distances](../science/converse.md#a-nearby-pair-of-program-states) and [data processing](../science/converse.md#processor-error-and-data-processing).

<a id="m08"></a>

### M08. Fidelity and independent program copies

**Central question.** How can single-specimen overlap control the distinguishability of many independent specimens?

**Understanding target.** Use root fidelity $`f(\alpha,\beta)=\|\sqrt\alpha\sqrt\beta\|_1`$, its multiplicativity on tensor products, and the inequality $`T\le\sqrt{1-f^2}`$. Explain why the iid source promise permits a single-copy fidelity calculation to control the full program input.

**Dependencies and story role.** [M05](#m05), [M07](#m07). This turns local state overlap into a quantitative constraint on a source budget.

**Conceptual connection.** Watrous's fidelity convention is the unsquared quantity used here. Keeping that convention explicit prevents a factor-of-two error in the later small-angle estimate.

**Sources.** Anchor: Watrous [§3.2][W3], especially Definition 3.11, Proposition 3.16, and Theorem 3.33. Project: [the exact program fidelity](../science/converse.md#a-nearby-pair-of-program-states).

<a id="m09"></a>

### M09. The diamond norm and joint accuracy

**Central question.** What error criterion remains meaningful when the batch is entangled with another system?

**Understanding target.** Interpret the diamond norm as a channel distance optimized over joint input-reference states. Explain the unhalved convention and distinguish a guarantee for the complete $`k`$-register channel from guarantees for individual marginals.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M06](#m06), [M07](#m07). This upgrades state-level distinguishability to the accuracy criterion required by the project.

**Conceptual connection.** Correlations produced by a shared program are part of the error being bounded. The reference system makes the guarantee suitable for later use inside a larger computation.

**Sources.** Anchor: Watrous [§§3.3.2–3.3.3][W3]. Project: [joint accuracy](../science/model.md#joint-accuracy) and [the reduced-channel lemma](../science/collision_bound.md#lemma).

<a id="m10"></a>

### M10. Composition and a complete error budget

**Central question.** How do local channel errors bound the error of an entire circuit or a tensor product of channels?

**Understanding target.** Explain channel norm one, contractivity under preparation and discarding, and telescoping bounds that add individual errors. Apply the same principle to sequential collisions, separate data groups, and repeated processor calls with known intervening gates.

**Dependencies and story role.** [M04](#m04), [M09](#m09). This connects local estimates to full input-output guarantees.

**Conceptual connection.** The same stability property supports the constructive upper bound and the converse. An explicit budget records which approximation produces each part of the final error.

**Sources.** Anchor: Watrous [§3.3.2][W3], including Proposition 3.48. Project: [fresh-collision composition](../science/parallel_program.md#fresh-collisions-implement-the-product-channel) and [the full implementation budget](../science/resources.md#4-group-size-finite-gates-and-the-final-error).

<a id="m11"></a>

### M11. Specimen access and charged resources

**Central question.** What computational access is supplied by a specimen, and what additional resources must an implementation provide?

**Understanding target.** Distinguish copies of $`P/r`$ from a classical eigenbasis, a preparation unitary, its inverse, and a purification oracle. Separate a hard copy budget from an expected budget, and identify source preparation, storage, known gates, and synthesis precision as additional costs.

**Dependencies and story role.** [M04](#m04), [M05](#m05), [M10](#m10). This puts the information-theoretic channel model into its computational setting.

**Conceptual connection.** A mathematical channel representation does not supply free physical access to its dilation. The source contract determines which constructions and lower bounds are comparable.

**Sources.** Anchor: Watrous [§§2.2.1–2.2.2][W2] for channel inputs and representations. Project: [source access](../science/model.md#source-processor-and-output) and [copy, gate, and memory counts](../science/resources.md#5-copy-gate-and-memory-counts).

<a id="m12"></a>

### M12. The complete parallel programming task

**Central question.** What exactly is minimized, over which processors, and under which uniform guarantee?

**Understanding target.** Assemble known rank and exact flatness, iid source specimens, jointly available data, unconditional processing, a hard specimen budget, and uniform joint diamond accuracy into the definition of $`N_*(d,r,k,\epsilon)`$.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M04](#m04), [M08](#m08), [M09](#m09), [M10](#m10), [M11](#m11). This closes the background phase by joining its objects and tools into one operational problem.

**Conceptual connection.** The upper and lower arguments must address the same source, output channel, error convention, and availability requirement. Those quantifiers are part of the result.

**Sources.** Anchor: Watrous [§2.2.1][W2] and [§§3.3.2–3.3.3][W3]. Project: [the complete model](../science/model.md) and [proof dependencies](../science/README.md).

## Narrative/innovation: M13–M30

<a id="m13"></a>

### M13. The shared-swap interaction and its mean

**Central question.** How can one program specimen generate the intended action on several data registers?

**Understanding target.** Identify $`H_*=\sum_jS_{a,j}`$, where $`S_{a,j}`$ swaps program register $`a`$ with target $`j`$. Interpret the program-weighted partial trace $`\mathcal E_\rho`$ and its mean $`h=\mathcal E_\rho(H_*)=\sum_j\rho_j`$, where $`\rho_j`$ acts on target $`j`$.

**Dependencies and story role.** [M03](#m03), [M06](#m06), [M12](#m12). This introduces the local physical interaction underlying the construction.

**Conceptual connection.** HME supplies this interaction for the linear map $`B\mapsto\sum_jB_j`$. The project analyzes its actual program-dependent error; it does not introduce a new interaction framework.

**Sources.** Anchor: Watrous [§§2.1.3, 2.2.2][W2]. Project: [interaction and moments](../science/parallel_program.md#the-interaction-and-its-moments); primary attribution: [HME](../references/RELATED_WORK.md#hme-supplies-the-collective-interaction).

<a id="m14"></a>

### M14. Ordered swaps and the second program moment

**Central question.** Which correlations appear when the same specimen participates in two different target interactions?

**Understanding target.** Track the order in $`\mathcal E_\rho(S_{a,i}S_{a,j})=\rho_jS_{i,j}`$ and interpret the second moment $`M=\mathcal E_\rho(H_*^2)`$. Explain the separate single-swap and cross-target contributions to $`\|M\|_\infty=k+k(k-1)/r`$.

**Dependencies and story role.** [M06](#m06), [M13](#m13). This identifies the rank-dependent structure that a full interaction-norm bound would discard.

**Conceptual connection.** Shared specimens create correlated target noise. The factor $`1/r`$ enters through the actual mixed program and must be retained before bounding the resulting channel.

**Sources.** Anchor: Watrous [§1.1.2][W1] and [§2.1.3][W2]. Project: [ordered swap identities and second moment](../science/parallel_program.md#the-interaction-and-its-moments).

<a id="m15"></a>

### M15. Centering the program interaction

**Central question.** Which part of the joint interaction differs from the desired mean evolution?

**Understanding target.** Interpret the positive operator $`M-h^2`$ and its norm $`v=\|M-h^2\|_\infty`$. Use the purification isometry $`V`$ to relate this variance to coupling out of the fixed-environment subspace, and understand why subtracting the mean isolates the relevant fluctuation.

**Dependencies and story role.** [M05](#m05), [M06](#m06), [M13](#m13), [M14](#m14). This converts the raw moment calculation into the quantity that controls the error.

**Conceptual connection.** A variance bound keeps the supplied state's structure while allowing arbitrary data inputs. Its positivity follows from a dilation identity, without giving the implementation access to that purification.

**Sources.** Anchor: Watrous [§§1.1.2–1.1.3][W1] and [§§2.1.3, 2.2.2][W2]. Project: [conditional expectation and variance](../science/collision_bound.md#conditional-expectation-and-variance).

<a id="m16"></a>

### M16. Compression, leakage, and the collision bound

**Central question.** How does the centered fluctuation produce a nonasymptotic channel-error estimate?

**Understanding target.** Connect the compressed Kraus operator's deviation from the intended unitary with the remaining completely positive leakage map. Explain why the two contributions give $`\|\Phi_\delta-\mathcal U_\delta\|_\diamond\le2\delta^2v`$ for a collision of duration $`\delta`$, including every reference input.

**Dependencies and story role.** [M05](#m05), [M06](#m06), [M09](#m09), [M15](#m15). This completes the local analytical mechanism before specializing its variance.

**Conceptual connection.** The proof controls the full remainder through compression and leakage. The error estimate is therefore stronger than a formal second-order expansion with an unspecified remainder.

**Sources.** Anchor: Watrous [§2.2.2][W2] and [§3.3.2][W3]. Project: [the collision lemma](../science/collision_bound.md#lemma) and [its proof](../science/collision_bound.md#proof).

<a id="m17"></a>

### M17. Variance across sectors of fixed support count

**Central question.** Why can the exact worst-case variance be found without learning the orientation of the support?

**Understanding target.** Use $`C_P=\sum_jP_j`$ to separate sectors with $`m`$ targets in the support. Explain the sector upper bound and the symmetric vectors that attain it, giving $`v_{r,k}=\max_{0\le m\le k}[k+(k-1)m/r-m^2/r^2]`$ over integer $`m`$.

**Dependencies and story role.** [M01](#m01), [M06](#m06), [M14](#m14), [M15](#m15), [M16](#m16). This supplies the task-specific value needed by the local channel lemma.

**Conceptual connection.** Permutation symmetry and positive-operator order replace any need for a classical basis of $`P`$. A nonempty range and kernel provide the attaining vectors, explaining the condition $`r\lt d`$.

**Sources.** Anchor: Watrous [§§1.1.2–1.1.3][W1]. Project: [exact variance](../science/parallel_program.md#exact-variance).

<a id="m18"></a>

### M18. Fresh collisions produce the reflection batch

**Central question.** How does a small accurate collision become the desired complete batch operation?

**Understanding target.** Explain why fresh specimens give a composition of reduced channels, why $`t=\pi r`$ turns $`e^{-it\rho}`$ into $`R_P`$, and how diamond telescoping gives joint error at most $`2\pi^2r^2v_{r,k}/N`$ after $`N`$ collisions.

**Dependencies and story role.** [M02](#m02), [M10](#m10), [M13](#m13), [M16](#m16), [M17](#m17). This connects the local mechanism to an entire output channel.

**Conceptual connection.** The program states are fresh and independent, while the data remain coherent and may stay entangled throughout. The composition argument does not reset or factorize the targets.

**Sources.** Anchor: Watrous [§2.2.1][W2] and [§3.3.2][W3]. Project: [fresh collisions](../science/parallel_program.md#fresh-collisions-implement-the-product-channel).

<a id="m19"></a>

### M19. Symmetric sweeps from known pair gates

**Central question.** How is the collective interaction implemented without treating its exponential as a free operation?

**Understanding target.** Relate a partial swap to a known Hermitian-involution rotation. Explain the symmetric $`2k-1`$-gate sweep, the cancellation of its second-order product error, and the operator remainder at most $`k^3|\delta|^3/3`$.

**Dependencies and story role.** [M06](#m06), [M11](#m11), [M18](#m18). This replaces an abstract collective evolution by an explicit circuit.

**Conceptual connection.** A physically available implementation must preserve the variance gain. The symmetric sweep and its remainder estimate are supplied by the project, with the collision architecture attributed to prior work.

**Sources.** Anchor: Watrous [§1.1.3][W1] and [§2.2.1][W2] for norms and unitary channels. Project: [partial-swap gadget](../science/resources.md#1-a-partial-swap-with-returned-work), [symmetric sweep](../science/resources.md#2-a-symmetric-sweep-implements-the-collective-collision), and [implementation antecedents](../references/RELATED_WORK.md#collective-collisions-and-gate-implementation).

<a id="m20"></a>

### M20. An explicit uniform specimen upper bound

**Central question.** How many specimens suffice after both reduced-channel error and sweep error are included?

**Understanding target.** Combine the terms proportional to $`1/N`$ and $`1/N^2`$ and interpret the sufficient count $`N=\lceil4\pi^2rk(r+k-1)/\epsilon\rceil`$ for $`0\lt \epsilon\le1`$. Keep the integer budget and the exact-known-rotation convention visible.

**Dependencies and story role.** [M10](#m10), [M17](#m17), [M18](#m18), [M19](#m19). This completes the constructive specimen bound before optimizing its gate realization.

**Conceptual connection.** A finite, uniform choice of $`N`$ closes the passage from an infinitesimal collision picture to a deterministic channel with a specified accuracy.

**Sources.** Anchor: Watrous [§1.1.3][W1] and [§3.3.2][W3]. Project: [explicit upper bound](../science/parallel_program.md#known-pair-gates-and-an-explicit-upper-bound) and [one-group error budget](../science/resources.md#3-one-group-with-a-complete-error-budget).

<a id="m21"></a>

### M21. Batching without losing the sample order

**Central question.** How can smaller jointly processed groups retain the specimen saving while controlling the gate count?

**Understanding target.** Partition the $`k`$ targets into $`q=\lceil k/r\rceil`$ groups of size at most $`r`$. Explain why group errors add even on entangled inputs, why specimen counts retain order $`(r^2k+rk^2)/\epsilon`$, and why pair partial swaps have order $`r^2k^2/\epsilon`$.

**Dependencies and story role.** [M10](#m10), [M20](#m20). This turns the full-batch construction into an efficient explicit implementation.

**Conceptual connection.** Independent program supplies for different groups are compatible with entanglement across those groups because the error contract is a channel bound.

**Sources.** Anchor: Watrous [§3.3.2][W3]. Project: [batching](../science/parallel_program.md#batching-preserves-the-specimen-order) and [copy and gate counts](../science/resources.md#5-copy-gate-and-memory-counts).

<a id="m22"></a>

### M22. Finite precision, preparation, and storage

**Central question.** Which resources remain once a sufficient specimen count has been established?

**Understanding target.** Account for finite rotation synthesis, elementary gates, source preparation, data storage, and program storage. Distinguish exact work-qubit return with ideal rotations from approximate joint return after synthesis, and distinguish specimens stored before the targets arrive from specimens streamed during execution.

**Dependencies and story role.** [M11](#m11), [M19](#m19), [M21](#m21). This closes the constructive side with a complete physical resource interpretation.

**Conceptual connection.** The specimen law is compatible with explicit gate and memory charges. The anchor supplies channel-error composition; the gate-synthesis guarantee and delivery schedules are specified in the project and its primary references.

**Sources.** Anchor: Watrous [§2.2.2][W2] and [§3.3.2][W3]. Project: [finite-gate budget and joint work return](../science/resources.md#4-group-size-finite-gates-and-the-final-error), [storage and preparation](../science/resources.md#5-copy-gate-and-memory-counts), and [synthesis attribution](../references/RELATED_WORK.md#collective-collisions-and-gate-implementation).

<a id="m23"></a>

### M23. Nearby supports and program indistinguishability

**Central question.** Which pair of admissible supports makes every processor confront a source-information limitation?

**Understanding target.** Follow the pair $`P_0,P_\theta`$ obtained by rotating one support direction through an angle $`\theta`$ into the complement. Explain their root fidelity $`f=(r-1+\cos\theta)/r`$ and how tensor-product fidelity bounds the trace distance of their many-specimen programs.

**Dependencies and story role.** [M01](#m01), [M07](#m07), [M08](#m08), [M12](#m12). This begins the converse with a local pair inside the fixed-rank promise.

**Conceptual connection.** The spectrum remains fixed in both hypotheses. The lower bound uses uncertainty in the support, so a varying-spectrum worst-case theorem cannot replace this task-specific comparison.

**Sources.** Anchor: Watrous [§3.2][W3]. Project: [nearby program states](../science/converse.md#a-nearby-pair-of-program-states) and [discrimination-method attribution](../references/RELATED_WORK.md#the-converse-uses-program-distinguishability).

<a id="m24"></a>

### M24. Relative reflections and a two-dimensional rotation

**Central question.** How can ordinary reflection channels reveal the small rotation between the chosen supports?

**Understanding target.** Explain the eigenphases $`e^{\pm2i\theta}`$ of $`R_0R_\theta`$ on the distinguished two-dimensional plane, where $`R_0=I-2P_0`$. Identify the known comparison gate and the fixed eigenvectors used by the discrimination experiment.

**Dependencies and story role.** [M02](#m02), [M23](#m23). This converts a small support change into a coherent phase signal.

**Conceptual connection.** The comparison reflection is known because the proof chooses its two hypotheses. The reduction needs neither a controlled unknown reflection nor an extra supplied reference sector.

**Sources.** Anchor: Watrous [§1.1.2][W1] and [§2.2.1][W2]. Project: [relative-reflection geometry](../science/converse.md#the-relative-reflection-accumulates-phase).

<a id="m25"></a>

### M25. An entangled batch amplifies the phase

**Central question.** How does the same small rotation become more distinguishable when the operation acts on a coherent batch?

**Understanding target.** Interpret the superposition of the tensor powers of the two relative-reflection eigenvectors. Explain why one batch invocation produces relative phase $`4k\theta`$ and why the uniform joint-channel guarantee covers this input.

**Dependencies and story role.** [M03](#m03), [M09](#m09), [M24](#m24). This introduces the batch-size dependence of the converse.

**Conceptual connection.** The target operation can accumulate a coherent phase across the batch while the supplied program states remain close. The lower bound compares these two distinguishability scales.

**Sources.** Anchor: Watrous [§1.1.1][W1], [§3.1.1][W3], and [§3.3.3][W3]. Project: [entangled batch and phase accumulation](../science/converse.md#the-relative-reflection-accumulates-phase).

<a id="m26"></a>

### M26. Repetition and the unrestricted converse

**Central question.** How does a uniformly accurate processor force the inverse-accuracy specimen lower bound?

**Understanding target.** Join the hard $`N`$-copy budget per invocation, $`m=\lfloor1/(4\epsilon)\rfloor`$ repetitions, the choice $`\theta=\pi/(4km)`$, and diamond-error accumulation. Explain how orthogonal ideal outputs and trace-distance contractivity imply $`N\ge9rk^2/(8\pi^2\epsilon)`$ for $`0\lt \epsilon\le1/8`$.

**Dependencies and story role.** [M07](#m07), [M08](#m08), [M10](#m10), [M12](#m12), [M23](#m23), [M24](#m24), [M25](#m25). This closes the converse for every deterministic unconditional processor in the model.

**Conceptual connection.** The repeated experiment consumes $`Nm`$ specimens and uses one hypothesis-independent physical map. Internal measurements or a classically estimated program do not evade data processing.

**Sources.** Anchor: Watrous [§§3.1.1, 3.2, 3.3.2][W3]. Project: [processor error and data processing](../science/converse.md#processor-error-and-data-processing) and [converse scope](../science/converse.md#scope-of-the-conclusion).

<a id="m27"></a>

### M27. The matched large-batch theorem

**Central question.** In which parameter regime do the upper and lower constructions settle the specimen complexity?

**Understanding target.** Compare the upper dependence $`r^2k+rk^2`$ with the lower dependence $`rk^2`$. Explain why they match for $`k\ge r`$, uniformly in $`d>r`$ and for $`0\lt \epsilon\le1/8`$, and why finite-gate resource accounting preserves this specimen order.

**Dependencies and story role.** [M20](#m20), [M22](#m22), [M26](#m26). This joins the constructive and unrestricted arguments into the central theorem.

**Conceptual connection.** The statement $`N_*=\Theta(rk^2/\epsilon)`$ needs both achievability and impossibility under the same contract. Dimension-independent specimen constants do not remove dimension-dependent gate or storage costs.

**Sources.** Anchor: Watrous [§§3.1.1, 3.3.2–3.3.3][W3] for the two operational distance tools. Project: [the theorem](../science/model.md#the-copy-complexity-theorem) and [resource counts](../science/resources.md#5-copy-gate-and-memory-counts).

<a id="m28"></a>

### M28. The sample saving and its precise baseline

**Central question.** What established construction does collective programming improve, and which methods does it inherit?

**Understanding target.** Reconstruct the separate-DME budget $`O(r^2k^2/\epsilon)`$ from a per-target error $`\epsilon/k`$. Explain the factor-$`r`$ specimen improvement for $`k\ge r`$, the retained pair-gate order, and the distinction between this explicit comparison and a universal separation from independent or classical processors.

**Dependencies and story role.** [M10](#m10), [M21](#m21), [M22](#m22), [M27](#m27). This places the theorem in its computational and research context.

**Conceptual connection.** The contribution is a sharper rank-sensitive law within established HME and discrimination methods. Correct attribution is necessary to identify what the comparison actually establishes.

**Sources.** Anchor: Watrous [§3.3.2][W3] for error composition. Project: [comparison with separate DME](../science/interpretation.md#comparison-with-separate-dme), [resource comparison](../science/resources.md#6-what-the-sample-saving-compares), and [related work](../references/RELATED_WORK.md).

<a id="m29"></a>

### M29. Boundaries of the established result

**Central question.** Which changes in rank, output interface, or resource claim would require a different theorem?

**Understanding target.** Locate the unresolved $`k\lt r`$ regime, the trivial $`r=d`$ endpoint, the known-rank flat-spectrum promise, and the need for jointly available inputs within each group. Distinguish the proved channel from a controlled unknown gate, a returned catalyst, an online adaptive oracle, or a guaranteed runtime improvement.

**Dependencies and story role.** [M02](#m02), [M11](#m11), [M12](#m12), [M22](#m22), [M27](#m27), [M28](#m28). This integrates the theorem's load-bearing assumptions and its resource interpretation.

**Conceptual connection.** Strong accuracy on a parallel channel does not supply a different causal interface. A specimen saving also remains distinct from a saving in all physical costs.

**Sources.** Anchor: Watrous [§2.2.1][W2] and [§3.3.3][W3] for precisely specified channels. Project: [availability and endpoints](../science/model.md#availability-and-endpoints), [interpretation](../science/interpretation.md), and [converse scope](../science/converse.md#scope-of-the-conclusion).

<a id="m30"></a>

### M30. The complete contribution and proof structure

**Central question.** How do the physical mechanism, the mathematical bounds, and the implementation costs support one coherent conclusion?

**Understanding target.** Connect the source contract to the shared-swap mean, rank-sensitive variance, complete-channel upper, charged implementation, and fidelity-based converse. Explain the optimal large-batch specimen law together with its explicit benchmark, inherited methods, and unresolved boundaries.

**Dependencies and story role.** [M12](#m12), [M16](#m16), [M17](#m17), [M22](#m22), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). This completes the narrative phase by integrating the proof structure and operational meaning.

**Conceptual connection.** The channel, dilation, norm, and distinguishability tools from the anchor meet in a single result about quantum states used as instructions. The project's canonical proofs supply the specific mechanism and quantitative law.

**Sources.** Anchor: Watrous [§2.2.2][W2] and [§3.1.1, §3.2, §§3.3.2–3.3.3][W3]. Project: [scientific account](../science/README.md), [model and theorem](../science/model.md), [interpretation](../science/interpretation.md), and [attribution](../references/RELATED_WORK.md).

[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf

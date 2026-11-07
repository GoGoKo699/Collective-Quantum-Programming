# Scientific account

The processor receives specimens of an unknown flat-rank state and a batch of data registers. Its task is to apply the corresponding support reflection to the whole batch with a global channel guarantee. The specimen cost is optimal when the number of targets is at least the rank.

Read the pages in this order for the complete argument:

1. [Model and main theorem](model.md) defines the input resource, output channel, error convention and parameter range.
2. [Reduced-unitary error](collision_bound.md) proves the dimension-independent bound from the operator variance of a fixed program state.
3. [Parallel program construction](parallel_program.md) evaluates the swap moments and obtains the specimen upper bound.
4. [Unrestricted converse](converse.md) uses nearby supports and distinguishability to prove the matching large-batch lower bound.
5. [Gates, precision and storage](resources.md) implements the interaction using ordinary pair gates and accounts for finite precision and program chronology.
6. [Interpretation and scope](interpretation.md) explains the gain over separate DME and the boundaries of the result.

The [related-work account](../references/RELATED_WORK.md) identifies the established HME interaction, collision architecture and lower-bound methods, and states the resource law added here. The [verification guide](../verification/README.md) connects the numerical checks to the equations they test and explains their limits.

Each proof has one authoritative home. The general upper bound applies to every positive batch size; matching optimality is asserted for the large-batch regime stated in the theorem.

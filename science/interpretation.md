# What the batch law means

A copy of an unknown state can carry instructions for a quantum operation. Here the program is the flat state $`\rho_P=P/r`$, and the instruction is to reverse the phase on the unknown support of $`P`$. The support has no supplied classical description. The processor must act coherently on an entire batch, including inputs entangled with systems it cannot access.

For $`k\ge r`$, the [model and theorem](model.md) give

```math
N^*(d,r,k,\varepsilon)=\Theta\!\left(\frac{rk^2}{\varepsilon}\right).
```

The statement is uniform in the register dimension $`d>r`$. It concerns the copies consumed by an unconditional processor at global diamond error $`\varepsilon`$. The [lower bound](converse.md) applies to every processor in this model, while the [construction](parallel_program.md) attains the same order with known pair interactions.

## Why a shared program helps

One program register interacts with several targets before it is discarded. Its mean action generates the desired product unitary. Its fluctuations introduce error, including correlations among the targets. For the swap-star interaction on $`k`$ targets, the conditional second moment is

```math
\|M\|_\infty=k+\frac{k(k-1)}r.
```

The first term comes from using each individual swap twice. The second comes from pairs of different target interactions and is suppressed by the flat program's eigenvalue $`1/r`$. After evolution for time $`\pi r`$, the resulting sample upper bound is

```math
N=O\!\left(\frac{r^2k+rk^2}{\varepsilon}\right).
```

The [operator-variance argument](collision_bound.md) controls these fluctuations without replacing them by the worst-case squared norm of the full interaction. It also keeps the external reference in the accuracy guarantee. Shared-program correlations are therefore included in the proof.

## Comparison with separate DME

Ordinary density matrix exponentiation on one target uses $`O(r^2/\eta)`$ specimens at error $`\eta`$. Applying it separately to $`k`$ targets with error allocation $`\eta=\varepsilon/k`$ gives $`O(r^2k^2/\varepsilon)`$ total specimens. The relevant DME and HME results are attributed in [Related work](../references/RELATED_WORK.md).

| Batch regime | Shared-program specimen upper | Separate-DME specimen upper | What is established |
|---|---|---|---|
| $`k=1`$ | $`O(r^2/\varepsilon)`$ | $`O(r^2/\varepsilon)`$ | The usual one-target upper is recovered. |
| $`1<k<r`$ | $`O(r^2k/\varepsilon)`$ | $`O(r^2k^2/\varepsilon)`$ | An improved construction; the optimum is not determined here. |
| $`k\ge r`$ | $`O(rk^2/\varepsilon)`$ | $`O(r^2k^2/\varepsilon)`$ | A factor-$`r`$ improvement in the asymptotic specimen bound, with a matching unrestricted converse. |

At $`k=r`$, for example, the shared construction uses $`O(r^3/\varepsilon)`$ specimens, while the separate construction uses $`O(r^4/\varepsilon)`$. These are scaling statements; the explicit constants and ceilings are given with the constructions. The comparison is to the specified separate-DME protocol. It is not a lower bound on all processors that might be described as independent, and it does not establish a universal separation from classical estimation.

Blocks of at most $`r`$ targets suffice to attain the optimal large-batch order. This avoids the gate overhead of applying every specimen to all $`k`$ targets when $`k`$ is much larger than $`r`$. The [resource account](resources.md) gives $`O(r^2k^2/\varepsilon)`$ pair partial swaps, matching the order of the separate-DME implementation. State preparation, protected storage, elementary gates and rotation precision still have their own costs. A specimen saving need not be an execution-time saving.

## Why the quadratic batch cost remains

Two nearby supports give very similar program states. Yet a collective input can resolve their difference after enough coherent phase accumulation. The converse compares these two facts: distinguishability cannot increase under a fixed physical processor, while the target reflections would make the outputs orthogonal after suitable repetition. This enforces the $`rk^2/\varepsilon`$ cost.

The result therefore specifies a finite benefit from sharing specimens across a batch. It does not turn those specimens into indefinitely reusable classical instructions. The processor consumes its programs, and each processed block requires its inputs to be available together. A sequence of adaptive requests, whose later inputs do not yet exist when earlier outputs are required, has a different causal interface.

The rank-one case already has the quadratic $`k^2/\varepsilon`$ cost and offers no rank-dependent improvement over separate DME. The endpoint $`r=d`$ is different: $`P=I`$, so the ordinary reflection channel is the identity and needs no specimen. Exact flatness and known rank are assumptions of the stated problem. Extensions to an unknown spectrum or the full small-batch optimum require additional results.

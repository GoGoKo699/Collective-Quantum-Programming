# Check hosted mathematics

This check compares the mathematics displayed by GitHub with the Markdown at an exact commit. It reads every tracked Markdown page, opens its commit-pinned public URL in fresh anonymous Chromium contexts at widths 1440 and 760 pixels, and compares every accessible MathML expression with its source. It also checks expression counts, relation symbols, labels, the explicit [text contract](math-contract.json), and display geometry.

The [workflow](../../.github/workflows/hosted-mathematics.yml) runs on pull requests from this repository, with a read-only repository token and no retained checkout credentials. Its collector uses no GitHub authentication. Dependencies are locked, and the three official GitHub actions are pinned to complete commit hashes. Reports include the checked source commit and tree, page and expression hashes, actual hosted HTML, screenshots, and any failures. Artifacts expire after seven days; retain a report separately when using it as a durable verification record.

The workflow first runs the representative diagnostic in `probe_hosted_math.cjs` on the anchor bridge, then performs the complete comparison. The diagnostic is not release evidence.

## Run the same check

Use Node.js 18 or newer, Python 3.10 or newer, Git, and an environment that permits Chromium and access to public GitHub pages. From the repository root:

```bash
npm ci --prefix verification/hosted --ignore-scripts --no-audit --no-fund
node verification/hosted/node_modules/playwright/cli.js install --with-deps chromium
node verification/hosted/capture_hosted_math.cjs \
  --root . \
  --repository GoGoKo699/Collective-Quantum-Programming \
  --revision "$(git rev-parse HEAD)" \
  --contract verification/hosted/math-contract.json \
  --output /tmp/collective-quantum-programming-hosted
```

The output directory must be empty or absent. The revision must already be available on GitHub. The collector reads committed Git objects, so local uncommitted edits are not part of the check. Preserve failed attempts instead of overwriting their reports. An access or policy refusal is a blocked check, not permission to change account or execution policies.

## What a passing report establishes

The report establishes the recorded source-to-host comparison and the stated viewport coverage. A separate visual review must inspect the captured equation bodies, tables, page layout, and navigation against their source. Neither the automated comparison nor that visual review proves the scientific claims; the analytical arguments are in [science](../../science/README.md), and the finite numerical checks are described in the [verification guide](../README.md).

`math-contract.json` records additional source expectations for selected load-bearing expressions. Its hashes identify individual expressions, not whole pages. A source change requires regenerating the affected expectations and a fresh hosted capture. The contract cannot waive missing expressions or rendering failures.

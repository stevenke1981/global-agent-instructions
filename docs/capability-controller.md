# Capability policy adoption

`shared/CAPABILITY_POLICY.md` is the canonical English policy. The same managed block is
embedded in Codex, Claude Code, shared and AGY profiles so a copied standalone profile remains
usable. `python scripts/sync_capability.py --check` detects drift;
`python scripts/sync_capability.py --write` updates only this repository's four profiles.
Neither command installs into the user's home directory or changes any runtime/provider.

The exact two-failure escalation rule and default budgets are engineering choices, not vendor
requirements. Native effort support must be verified per backend. Model-role preferences and
model bans remain; unconditional high effort and the contradictory Sonnet-review sentence
were corrected. Existing paid-use, identity, browser-stop and deployment rules still apply.

See [seven practical examples](seven-principles.zh-TW.md). Run their commands in the matching
luna-decision-core capability branch, not in this instructions repository. The
[contract template](../examples/capability-contract.json) uses fictional models and receipts;
replace them with authorized, observed host state. The controller is opt-in through `route`
and must not be described as a model/executor installed by these instructions.

Before deploying a profile: inspect local overrides and inheritance, back up conflicts, review
the diff, perform the authorized installation, read the installed file back, then run a harmless
host smoke test. Report source checks, installation, host discovery and live execution separately.
This update alone establishes only repository source state, not installation on a user's computer.

Primary references consulted 2026-11-05:

- [OpenAI reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices): explicit outcomes and constraints; do not mandate hidden reasoning transcripts.
- [OpenAI reasoning guide](https://developers.openai.com/api/docs/guides/reasoning): effort controls depend on the selected model and API.
- [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): keep task-relevant context and retrieve as needed.
- [Anthropic building effective agents](https://www.anthropic.com/engineering/building-effective-agents): simple workflows and selective parallelization.
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): representative, repeatable evaluations rather than subjective confidence alone.

The project's offline assertions check control behavior, not model intelligence or productivity.
For a real comparison, freeze task inputs and acceptance criteria, record success/quality/human
usability separately from time and cost, repeat stochastic tasks and disclose unmeasured metrics.
Do not reuse the preceding conversation's model table as a verified capability catalog.

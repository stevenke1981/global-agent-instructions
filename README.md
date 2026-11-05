# Global agent instructions

A snapshot of personal instructions for Codex, Claude Code, and Antigravity (AGY). These files describe this owner's preferences and may refer to locally installed tools, model names, or policies that do not apply to other environments.

| File | Source and intended use |
| --- | --- |
| `codex/AGENTS.md` | Snapshot of `~/.codex/AGENTS.md`, the Codex global instructions. |
| `claude/CLAUDE.md` | Snapshot of `~/.claude/CLAUDE.md`, the Claude Code global instructions. |
| `shared/AGENTS.md` | Snapshot of `~/AGENTS.md`, a home-directory workspace instruction file; inheritance depends on the agent and workspace. |
| `agy/AGENTS.md` | AGY global-rule **template**, copied from `~/AGENTS.md`. No separate AGY global instructions file was found on the source machine when this snapshot was created. |

For AGY, `~/.gemini/AGENTS.md` is one supported global location; see the [Antigravity rules documentation](https://antigravity.google/docs/rules/). Copy a file to its target only after reviewing its instructions and backing up any existing file. Merely cloning this repository does not install or activate any rules. These snapshots are not automatically synchronized with local files.

The instruction files are written in English while retaining the owner's requested Traditional Chinese response style. Final task reports use local timestamps in filenames such as `result_20261105_083000.md`, with a suffix if needed to avoid overwriting. No credentials or application settings are included.

The AGENTS.md files also include portable engineering and multi-account identity-routing rules. See [policy sources and scope](docs/2026-11-05-policy-sources.md) for the two owner-provided conversations and the adoption boundaries.

## Capability policy and seven examples

The four profiles now embed the same [capability policy](shared/CAPABILITY_POLICY.md): clear outcomes, relevant context, native-effort routing, real tools, selective teamwork, external acceptance and root-cause recovery. Existing profile permissions and spend limits remain authoritative.

```sh
python scripts/sync_capability.py --check
python -m unittest discover -s tests -v
```

Use `--write` only to synchronize the four repository copies after editing the canonical policy. It does not install any global instructions. See [adoption and references](docs/capability-controller.md), [七個實際參考範例](docs/seven-principles.zh-TW.md) and the [offline contract template](examples/capability-contract.json).

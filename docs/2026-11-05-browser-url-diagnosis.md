# Windows Chrome URL-verification diagnosis

## Observed evidence

- In the earlier attempt, browser discovery returned an empty browser list and `The browser access host is unavailable`. A subsequent native Chrome `cua.getApp({ windowId: ... })` call was stopped because the host could not determine the current browser URL confidently enough to enforce policy.
- The current diagnostic turn reproduced the browser-host error with the supported `cua.getState()` API. No native Chrome action was attempted after that result.
- The installed Chrome plugin's read-only checks reported a correct Native Messaging manifest and an installed/enabled extension in all four inspected profiles. These checks do not prove a working session connection.
- Read-only inspection of the installed `@oai/browser-desktop` service shows that the exact host error is thrown when its browser-access pipe path or verifying identity is absent. The service requires a signed access response for the current session/turn. The failing error identifies this boundary; it does not identify which upstream component failed to supply it.

## Changes and limits

- Codex/shared/AGY instructions now require browser/tab routing for browser tasks, public retrieval before unnecessary UI use, and an explicit prohibition on falling back from a failed browser host to a native Chrome window.
- The user-owned Chrome automation skill and troubleshooting guide receive the same routing and recovery rules.
- Safety checks, native helpers, browser permissions, remote debugging, runtime environment, and application binaries are not changed. No executor identity, pipe, or verification key is fabricated or copied from another session.
- This fixes the instruction-level routing mistake. The desktop browser-access host remains unavailable in the observed session; no end-to-end browser repair is claimed.
- Sol/Terra-specific regression runs are NOT_RUN. The available evidence does not establish a model-specific defect.

## Supported recovery and acceptance

Save other work, check the normal Codex desktop browser connection/settings, and reopen the application/session if needed. Retest browser inventory through the supported API, bind the intended browser and tab, verify its current URL, then perform and verify one authorized reversible interaction. A new conversation alone is not proof of recovery. If the host still fails, retain the exact error and desktop/runtime version for vendor diagnosis.

If any tool explicitly stops Computer Use for the turn, obey that stop and its recovery conditions. A reset, alternate model, raw CDP, or a different desktop tool is not a valid workaround for the blocked action.

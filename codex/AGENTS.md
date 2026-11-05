# Codex / Dots Fix-First Policy v1.1

## Working principles
- For implementation, fixes, and improvements, act as the implementer by default: complete authorized changes and verification, rather than delivering only analysis or a review report.
- Honor explicit requests for read-only analysis or code review. This policy does not turn questions or read-only reviews into modification tasks.
- Base decisions on actual errors, reproducible behavior, build results, tests, and operational evidence. Do not present speculation as a defect without evidence.

## Workflow
1. Confirm the requirements, acceptance criteria, and minimum necessary verification. When fixing a bug, first reproduce it or collect a concrete error.
2. Identify the root cause and implement the smallest effective fix consistent with the project's architecture and conventions.
3. Run builds, tests, or smoke tests appropriate to the change. GUI features require actual launch or interaction verification.
4. If a check fails, fix the issue using its output and retest the affected scope; do not start another full review cycle.
5. After acceptance passes, perform one necessary final diff self-check and deliver if no new issue is found.

## Avoid excessive review
- By default, do not invoke `/review` during implementation, start an unrequested whole-project review, or create chains of reviewers reviewing reviewers.
- Make one lightweight self-check for ordinary changes. Retain independent review where justified by actual risk and project requirements.
- Fix evidenced defects directly; prioritize P0/P1. Speculative P2/P3 suggestions and preferences do not block acceptance or delivery.
- Use appropriate tools for formatting, lint, and type checks; do not repeat tool-verified checks through multiple rounds of manual review.
- Use subagents only when the user, an applicable skill, or project rules require teamwork. Implementers make changes, validators provide evidence of errors, and reviewers check once only when necessary.

## Fix and verification loop
- Do not rerun the same review or expensive tests without code changes, new failures, or new evidence.
- If the same error yields no progress twice in a row, change the diagnostic approach rather than repeating the same operation.
- After three consecutive attempts without new evidence, document the approaches and concrete blocker and pursue a feasible alternative. Report missing information and the next corrective action only if work truly cannot continue.
- After a fix, verify the affected scope first; expand to the full suite only for high risk, cross-module impact, CI, or project requirements.
- Once required checks pass, do not expand the scope merely to increase the number of checks.

## Delivery and scope
- Briefly list actual changes, verification performed and results, and remaining issues. Mark tests not run as NOT_RUN.
- Do not claim tests passed, deployment, publication, or remote configuration without direct evidence. Distinguish prepared, applied, and verified states.
- This is a cross-project default. Follow more specific project instructions and necessary CI and security requirements; explicitly explain mandatory review requirements that conflict with this policy and affect delivery.
- Do not disable security approvals, automatic security review, sandboxes, or required confirmations to reduce code review, and do not expand authorization beyond the original task.

## Coding preferences

1. Keep things in one function unless composable or reusable.
2. Validate unknown values once at the boundary that owns them. Pass typed values inward instead of repeating `typeof value === "object"` and property-existence checks. Do not defensively revalidate values already guaranteed by a schema, constructor, or internal type.
3. Do not extract single-use helpers preemptively. Inline the logic at the call site unless the helper is reused, hides a genuinely complex boundary, or has a clear independent name that improves the caller.
4. Before adding complexity for a speculative or vanishingly unlikely race or security edge case, explain the concrete failure mode, likelihood, and complexity cost to the user and get their buy-in. Do not silently expand scope for theoretical robustness.
5. Avoid `try` / `catch` where possible.
6. Avoid using the `any` type.
7. Use Bun APIs when possible, like `Bun.file()`.

## Model use and cost limits
- Never call `google/gemini-4-argon` or `fish-audio/transcribe-1-pro`, including for testing, acceptance, subtitle transcription, or indirect calls.
- By default, use explicitly named OpenRouter `:free` routes that have been confirmed free; never automatically fall back to paid routes. Before any paid OpenRouter model or charge, explain the model, purpose, pricing, and estimated cost or ceiling; say if these cannot be confirmed and obtain the user's explicit approval for that use before making the request. The two prohibited models remain prohibited.
- Prefer OpenRouter `fish-audio/s2.1-pro-free:free` for Fish narration; do not substitute another paid voice or transcription model.
- Use Codex `gpt-6.1-terra` for checking and judgment; do not call an external model solely for inspection. Mark actual listening or speech recognition that GPT-6.1 Terra cannot perform directly as NOT_RUN; do not present text or technical checks as a substitute.

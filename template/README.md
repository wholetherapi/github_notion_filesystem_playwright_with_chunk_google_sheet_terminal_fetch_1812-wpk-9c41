# Work Package Template

Every candidate package under `packages/<contributor>/<package-id>/` must match
the layout and content rules below. The `template/` package itself is a worked
example.

## Required artifacts

- `docs/brief.md` - non-empty item brief written in English text only. English
  means printable ASCII; do not use CJK, Cyrillic, Greek, Hangul or Kana
  characters.
- `docs/agent_prompt.md` - non-empty agent prompt written in English text only.
- `verification/verify.sh` - the verification entry point. It must exist; its
  contents are not inspected by the readiness gate.
- `src/` - implementation directory containing at least one file.
- `workspace/setup.json` - a non-empty local setup descriptor.

## Optional artifacts

- `docs/user_prompt.md` - if present, it must be non-empty and written in
  English text only. Omit the file if there is no user prompt.

A package is **ready** only when every required artifact passes. Otherwise the
package is **not_ready** and the failing requirement must be recorded.

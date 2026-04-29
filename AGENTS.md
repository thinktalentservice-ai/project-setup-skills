# AGENTS.md

## Ruthless mentor mode (ALWAYS ON)

Every response must include a brutal honest critique section. No sugarcoating. No validation for its own sake.

Rules:
- If the idea is weak, call it trash and say exactly why.
- If the code is bad, call it bad — name the specific failure.
- If the approach will cause problems later, predict them now.
- Praise only when genuinely earned. Empty praise is a lie.
- End every critique with: what's broken, why it matters, and what bulletproof looks like.
- User says "bulletproof" → that's the signal it passed. Until then, keep stress-testing.

This applies to: code, architecture decisions, plans, approaches, questions, everything.

---

## Caveman mode (ALWAYS ON — ultra)

Every session: invoke `/caveman ultra` via `Skill` tool at start. Ultra level active all responses. No revert unless user says "stop caveman" or "normal mode".

Ultra rules: abbreviate (DB/auth/config/req/res/fn/impl), strip conjunctions, arrows for causality (X → Y), one word when one word enough.

---

## Skill usage

**Always invoke skills.** If ≥1% chance a skill applies → invoke via `Skill` tool before any response or action. Not optional.

- Check skills before clarifying questions, exploration, or file reads.
- Process skills first (brainstorming, debugging, TDD) → then implementation skills.
- Rigid skills (TDD, debugging): follow exactly. Flexible skills: adapt.
- User instructions override skills. Skills override default behavior.
- Announce: "Using [skill] to [purpose]" before executing.
- Never Read skill files directly — use `Skill` tool.

---


Agent onboarding for the `project-setup-skills` repository.

## Scope

This repo contains Claude Code marketplace plugins and their skill assets:
- `caveman-ultra-setup`: installs a global SessionStart hook in `~/.claude/settings.json`
- `claude-md-setup`: creates or updates project-local `CLAUDE.md` from template sections

For feature details and examples, use `README.md` as the source of truth.

## Important Paths

- Marketplace manifest: `.claude-plugin/marketplace.json`
- Caveman plugin manifest: `caveman-ultra-setup/.claude-plugin/plugin.json`
- Claude-md plugin manifest: `claude-md-setup/.claude-plugin/plugin.json`
- Caveman skill: `caveman-ultra-setup/skills/caveman-ultra-setup/SKILL.md`
- Caveman installer script: `caveman-ultra-setup/skills/caveman-ultra-setup/scripts/install-caveman-hook.py`
- Claude-md skill: `claude-md-setup/skills/claude-md-setup/SKILL.md`
- Claude-md template: `claude-md-setup/skills/claude-md-setup/templates/CLAUDE.md`
- Existing project instruction baseline: `CLAUDE.md`

## Working Conventions

- Keep skill behavior idempotent. Re-running setup must not duplicate hooks or sections.
- Preserve user/project content on updates. Avoid destructive rewrites.
- Keep plugin metadata coherent across `marketplace.json` and per-plugin `plugin.json` files.
- Prefer additive edits; avoid broad formatting churn.

## Validation Commands

From repo root:

```powershell
python -m json.tool .claude-plugin/marketplace.json > $null
python -m json.tool caveman-ultra-setup/.claude-plugin/plugin.json > $null
python -m json.tool claude-md-setup/.claude-plugin/plugin.json > $null
python caveman-ultra-setup/skills/caveman-ultra-setup/scripts/install-caveman-hook.py
```

Note: the installer touches user-global `~/.claude/settings.json`. Use with caution while testing.

## Do Not Duplicate Docs

Link to existing docs instead of embedding long instructions:
- `README.md`
- `caveman-ultra-setup/skills/caveman-ultra-setup/SKILL.md`
- `claude-md-setup/skills/claude-md-setup/SKILL.md`

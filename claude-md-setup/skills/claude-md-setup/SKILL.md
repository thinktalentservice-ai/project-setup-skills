---
name: claude-md-setup
description: Creates or updates CLAUDE.md, AGENTS.md, and .github/copilot-instructions.md for the current project with ruthless mentor mode, caveman ultra mode, and skill usage rules. Use when user says "set up CLAUDE.md", "init project", "add mentor mode to this project", "configure this project for caveman", "scaffold claude config", or starts working in a new project directory that needs Claude configuration. Trigger even if the user just says "set up this project" or "init" without explicitly mentioning CLAUDE.md.
---

# Claude MD Setup

Write `CLAUDE.md`, `AGENTS.md`, and `.github/copilot-instructions.md` into the project root (current working directory) with the standard mentor + caveman + skill-usage rules. All three files get identical content from the template.

## Behavior

For each target file (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`):

**If file does not exist:** Create it from the template (create `.github/` dir if needed).

**If file already exists:** Read it first.
- If it already contains the three sections (Ruthless mentor mode, Caveman mode, Skill usage) → skip that file, note it's already set up.
- If it's missing some or all sections → append the missing sections at the end. Preserve all existing content.

## Steps

1. Read the template: `$CLAUDE_PLUGIN_ROOT/skills/claude-md-setup/templates/CLAUDE.md`

2. For each target file in order:
   a. `./CLAUDE.md`
   b. `./AGENTS.md`
   c. `./.github/copilot-instructions.md` (ensure `.github/` dir exists first)

3. Apply the create-or-update logic above to each file.

4. Confirm: print each path written and a one-line summary of what changed per file.

## Notes

- Do NOT modify the global `~/.claude/CLAUDE.md` — this is for the current project only.
- Preserve any existing content in each file. Never overwrite project-specific instructions the user already has.
- The three sections must be written verbatim from the template — no paraphrasing, no reordering.
- All three files get the exact same template content.

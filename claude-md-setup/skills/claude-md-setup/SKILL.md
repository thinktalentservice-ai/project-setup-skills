---
name: claude-md-setup
description: Creates or updates CLAUDE.md for the current project with ruthless mentor mode, caveman ultra mode, and skill usage rules. Use when user says "set up CLAUDE.md", "init project", "add mentor mode to this project", "configure this project for caveman", "scaffold claude config", or starts working in a new project directory that needs Claude configuration. Trigger even if the user just says "set up this project" or "init" without explicitly mentioning CLAUDE.md.
---

# Claude MD Setup

Write a `CLAUDE.md` file into the project root (current working directory) with the standard mentor + caveman + skill-usage rules.

## Behavior

**If `CLAUDE.md` does not exist:** Create it from the template.

**If `CLAUDE.md` already exists:** Read it first.
- If it already contains the three sections (Ruthless mentor mode, Caveman mode, Skill usage) → skip, tell user it's already set up.
- If it's missing some or all sections → append the missing sections at the end. Preserve all existing content.

## Steps

1. Check if `CLAUDE.md` exists in the project root (same directory as the `CLAUDE.md` you'd normally read for project instructions — i.e., `./CLAUDE.md` relative to cwd).

2. Read the template: `$CLAUDE_PLUGIN_ROOT/skills/claude-md-setup/templates/CLAUDE.md`

3. Write or update `CLAUDE.md` as described above.

4. Confirm: print the path written and a one-line summary of what changed.

## Notes

- Do NOT modify the global `~/.claude/CLAUDE.md` — this is for the current project only.
- Preserve any existing content in the file. Never overwrite project-specific instructions the user already has.
- The three sections must be written verbatim from the template — no paraphrasing, no reordering.

---
name: caveman-ultra-setup
description: This skill should be used when the user asks to "set up caveman ultra globally", "install caveman hook", "add caveman ultra to all projects", "configure caveman ultra session hook", "make caveman ultra the default", or wants caveman ultra mode active at the start of every Claude Code session across all projects.
version: 0.1.0
---

# Caveman Ultra Global Setup

Install a `SessionStart` hook into `~/.claude/settings.json` so caveman ultra mode activates automatically in every Claude Code session, globally, without relying on per-project CLAUDE.md instructions.

## What This Does

- Adds a `SessionStart` hook to global `~/.claude/settings.json`
- Hook outputs `additionalContext` JSON → injects caveman ultra rules into model context at session start
- Fires before first response, every session, every project
- Idempotent: safe to run multiple times

## Installation Steps

### Step 1: Run the install script

```bash
python "$CLAUDE_PLUGIN_ROOT/skills/caveman-ultra-setup/scripts/install-caveman-hook.py"
```

Script handles:
- Reading existing `~/.claude/settings.json` (preserves all current settings)
- Merging hook into `SessionStart` array (does not overwrite existing hooks)
- Dedup check (skips if hook already present)
- Writing updated file

### Step 2: Verify hook installed

```bash
python -c "
import json; from pathlib import Path
s = json.load(open(Path.home() / '.claude/settings.json'))
hooks = s.get('hooks', {}).get('SessionStart', [])
found = any('CAVEMAN ULTRA' in h.get('command','') for e in hooks for h in e.get('hooks',[]))
print('Hook installed:', found)
"
```

### Step 3: Reload config

Open `/hooks` in Claude Code UI or restart the session. `SessionStart` hooks fire outside the current turn — need a fresh session to activate.

## How the Hook Works

Hook type: `command` with `shell: bash`

At session start, harness runs:
```bash
echo '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"CAVEMAN ULTRA MODE ACTIVE..."}}'
```

Output JSON → `additionalContext` field → injected into model context before first response.

Caveman ultra rules injected:
- Abbreviate: DB/auth/config/req/res/fn/impl
- Strip conjunctions
- Arrows for causality: X → Y
- One word when one word enough
- Off only: "stop caveman" or "normal mode"

## Layered Defense (Recommended)

Hook alone = harness-enforced. Add CLAUDE.md instruction as backup for post-compaction sessions:

```markdown
## Caveman mode (ALWAYS ON — ultra)
Every session: invoke `/caveman ultra` via `Skill` tool at start.
Ultra level active all responses. Off only: "stop caveman" or "normal mode".
```

Both layers: hook fires at session start, CLAUDE.md re-activates after compaction.

## Troubleshooting

**Hook not firing:**
- Open `/hooks` in Claude Code to reload config
- Restart session (SessionStart fires on new session only)
- Verify JSON valid: `python -m json.tool ~/.claude/settings.json`

**Hook fires but mode not active:**
- Check `additionalContext` string in settings.json — must contain caveman ultra rules
- Re-run install script to refresh

## Scripts

- [scripts/install-caveman-hook.py](scripts/install-caveman-hook.py) — Safe merge installer, idempotent

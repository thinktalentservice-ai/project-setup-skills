# project-setup-skills

A Claude Code plugin marketplace with setup skills for global developer environment configuration.

## Skills

### caveman-ultra-setup

Installs a global `SessionStart` hook into `~/.claude/settings.json` that activates **caveman ultra mode** automatically in every Claude Code session, across all projects.

Caveman ultra: terse, compressed responses — abbreviations, arrows for causality, one word when one word enough. Off with `stop caveman` or `normal mode`.

---

### claude-md-setup

Creates or updates `CLAUDE.md` in any project root with three standard sections: **ruthless mentor mode**, **caveman ultra mode**, and **skill usage rules**.

**How it works:**

- **Trigger** — say `set up CLAUDE.md`, `init project`, `add mentor mode`, etc.
- **Creates** `./CLAUDE.md` in the current project root from a bundled template
- **Smart merge** — if file exists, appends only missing sections; preserves all existing content
- **Safe** — never touches `~/.claude/CLAUDE.md`

Invoke `/claude-md-setup` or use a natural trigger phrase in any session.

---

## Install

### 1. Register marketplace + enable plugins

Add to `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "project-setup-skills": {
      "source": {
        "source": "github",
        "repo": "thinktalentservice-ai/project-setup-skills"
      }
    }
  },
  "enabledPlugins": {
    "caveman-ultra-setup@project-setup-skills": true,
    "claude-md-setup@project-setup-skills": true
  }
}
```

### 2. Restart Claude Code

Plugin downloads and registers on next session start.

### 3. Invoke a skill

**caveman-ultra-setup:**
```
set up caveman ultra globally
```
Claude runs the install script → SessionStart hook written → caveman ultra active every future session.

**claude-md-setup:**
```
set up CLAUDE.md
```
Claude writes `./CLAUDE.md` into the current project root.

### 4. Verify caveman hook

```bash
python -c "
import json; from pathlib import Path
s = json.load(open(Path.home() / '.claude/settings.json'))
hooks = s.get('hooks', {}).get('SessionStart', [])
found = any('CAVEMAN ULTRA' in h.get('command','') for e in hooks for h in e.get('hooks',[]))
print('Hook installed:', found)
"
```

---

## How caveman-ultra-setup works

```
SessionStart event
  → harness runs hook command
  → outputs additionalContext JSON
  → caveman ultra rules injected into model context
  → every response in ultra mode
```

Deactivate: say `stop caveman` or `normal mode` in any session.

---

## Structure

```
project-setup-skills/
├── .claude-plugin/
│   └── marketplace.json
├── caveman-ultra-setup/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       └── caveman-ultra-setup/
│           ├── SKILL.md
│           └── scripts/
│               └── install-caveman-hook.py
└── claude-md-setup/
    ├── .claude-plugin/
    │   └── plugin.json
    └── skills/
        └── claude-md-setup/
            ├── SKILL.md
            └── templates/
                └── CLAUDE.md
```

## Requirements

- Claude Code with plugin support
- Python 3 (for caveman install script)
- Git Bash or bash shell on Windows

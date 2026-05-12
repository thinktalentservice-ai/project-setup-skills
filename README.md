# project-setup-skills

**🌐 GitHub Pages: [https://thinktalentservice-ai.github.io/project-setup-skills](https://thinktalentservice-ai.github.io/project-setup-skills)**

A Claude Code plugin marketplace with setup skills for global developer environment configuration.

## Skills

### caveman-ultra-setup

Installs a global `SessionStart` hook that activates **caveman ultra mode** automatically in every Claude Code session, across all projects.

Caveman ultra: terse, compressed responses — abbreviations, arrows for causality, one word when one word enough. Off with `stop caveman` or `normal mode`.

---

### claude-md-setup

Creates or updates `CLAUDE.md`, `AGENTS.md`, and `.github/copilot-instructions.md` in any project root with three standard sections: **ruthless mentor mode**, **caveman ultra mode**, and **skill usage rules**.

**How it works:**

- **Trigger** — say `set up CLAUDE.md`, `init project`, `add mentor mode`, etc.
- **Creates** `./CLAUDE.md`, `./AGENTS.md`, `./.github/copilot-instructions.md` from a bundled template
- **Smart merge** — if a file exists, appends only missing sections; preserves all existing content
- **Safe** — never touches `~/.claude/CLAUDE.md`

All three files get identical content — mentor mode, caveman ultra, and skill usage rules.

Invoke `/claude-md-setup` or use a natural trigger phrase in any session.

---

## Install

### 1. Add marketplace + install plugins

```bash
claude plugin marketplace add thinktalentservice-ai/project-setup-skills
claude plugin install caveman-ultra-setup@project-setup-skills
claude plugin install claude-md-setup@project-setup-skills
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
Claude writes `./CLAUDE.md`, `./AGENTS.md`, and `./.github/copilot-instructions.md` into the current project root.

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

## Plugin CLI

### Update

```bash
claude plugin update caveman-ultra-setup@project-setup-skills
claude plugin update claude-md-setup@project-setup-skills
```

### Disable / Enable

```bash
claude plugin disable caveman-ultra-setup@project-setup-skills
claude plugin enable caveman-ultra-setup@project-setup-skills
```

### Uninstall

```bash
claude plugin uninstall caveman-ultra-setup@project-setup-skills
claude plugin uninstall claude-md-setup@project-setup-skills
```

### List

```bash
claude plugin list
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

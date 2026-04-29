#!/usr/bin/env python3
"""Install caveman ultra SessionStart hook into ~/.claude/settings.json"""
import json
import os
import sys
from pathlib import Path

SETTINGS_PATH = Path.home() / ".claude" / "settings.json"

CAVEMAN_HOOK = {
    "hooks": [
        {
            "type": "command",
            "command": (
                "echo '{\"hookSpecificOutput\":{"
                "\"hookEventName\":\"SessionStart\","
                "\"additionalContext\":\"CAVEMAN ULTRA MODE ACTIVE. "
                "Rules: Abbreviate (DB/auth/config/req/res/fn/impl), "
                "strip conjunctions, arrows for causality (X -> Y), "
                "one word when one word enough. "
                "Pattern: [thing] [action] [reason]. "
                "Active all responses. "
                "Off only: stop caveman or normal mode."
                "\"}}'"
            ),
            "shell": "bash",
            "statusMessage": "Caveman ultra mode active"
        }
    ]
}

def load_settings():
    if SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_settings(data):
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {SETTINGS_PATH}")

def hook_already_installed(hooks_list):
    for entry in hooks_list:
        for h in entry.get("hooks", []):
            if "CAVEMAN ULTRA" in h.get("command", ""):
                return True
    return False

def main():
    settings = load_settings()
    hooks = settings.setdefault("hooks", {})
    session_hooks = hooks.setdefault("SessionStart", [])

    if hook_already_installed(session_hooks):
        print("Hook already installed. No changes made.")
        sys.exit(0)

    session_hooks.append(CAVEMAN_HOOK)
    save_settings(settings)
    print("Caveman ultra SessionStart hook installed globally.")

if __name__ == "__main__":
    main()

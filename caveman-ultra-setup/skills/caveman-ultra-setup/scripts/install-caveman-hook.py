#!/usr/bin/env python3
"""Install caveman ultra SessionStart hook into ~/.claude/settings.json"""
import json
import sys
import tempfile
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
        try:
            with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as exc:
            print(f"Error: {SETTINGS_PATH} contains invalid JSON: {exc}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(data, dict):
            print(
                f"Error: {SETTINGS_PATH} must be a JSON object, got {type(data).__name__}.",
                file=sys.stderr,
            )
            sys.exit(1)
        return data
    return {}

def save_settings(data):
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    backup = SETTINGS_PATH.with_suffix(".json.bak")
    file_existed = SETTINGS_PATH.exists()
    # Write to temp file first, then atomically replace to avoid corruption
    fd, tmp_path = tempfile.mkstemp(
        dir=SETTINGS_PATH.parent, prefix=".settings_tmp_", suffix=".json"
    )
    try:
        with open(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        if file_existed:
            SETTINGS_PATH.replace(backup)
        Path(tmp_path).replace(SETTINGS_PATH)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise
    print(f"Saved: {SETTINGS_PATH}")

def hook_already_installed(hooks_list):
    if not isinstance(hooks_list, list):
        print(
            "Error: hooks.SessionStart in settings is not a list. "
            "Cannot safely modify it. Please fix your settings.json manually.",
            file=sys.stderr,
        )
        sys.exit(1)
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

# ⚡ VibeShip

Frontend code with exceptional UX on the first generation — powered by a collective learning loop from real developer corrections.

127 seed patterns. Server-synced community pool. Gets better with every user.

## Install

```bash
claude skill install vibeship.skill
```

## Setup

```bash
# Connect to the community server
export VIBESHIP_API_URL="https://api-production-0e69.up.railway.app"

# Auto-capture corrections after every session (optional, recommended)
# Add to ~/.claude/settings.json:
{
  "hooks": {
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/vibeship/scripts/capture-hook.sh"
      }]
    }]
  }
}
```

The bundled skill ships with a shared write token, so `VIBESHIP_API_KEY` is optional. Set your own only if you want to override the shared token later.

If the shared token gets rotated, download the latest `vibeship.skill.md` and replace your local skill file.

## How It Works

1. You describe a UI → skill loads community patterns from server before generating
2. Output has proper hover states, accessible forms, responsive layouts from the start
3. You edit the output → post-session hook captures the diff
4. Diff is classified by the server and added to the community pool
5. Next developer gets better output because of your fix

Works without the server too — falls back to 127 seed patterns in `references/ux-patterns.md`.

## Commands

```bash
bash scripts/sync.sh pull      # Get latest community patterns
bash scripts/sync.sh capture   # Classify current git diffs & push
bash scripts/sync.sh log "description of what you fixed"
bash scripts/sync.sh stats     # Community stats
```

## Categories

Interaction · Layout · Typography · Forms · Accessibility · Mobile · Empty States · Feedback · Design · Navigation

## License

MIT

#!/usr/bin/env python3
"""
SkillerVibes Local Classifier — Offline fallback for diff classification.
Uses keyword matching when the server API is unreachable.
Not as accurate as the server's LLM-based classification, but works offline.

Usage: echo "diff content" | python3 classify-local.py filename.jsx
"""

import sys
import json

CATEGORY_SIGNALS = {
    "interaction": ["hover", ":hover", "click", "onclick", "active", ":active", ":focus",
                    "transition", "animation", "cursor", "pointer", "disabled", "loading",
                    "spinner", "opacity", "transform", "scale", "keydown", "keypress",
                    "mouseover", "mouseenter", "touchstart", "drag", "drop"],
    "layout": ["flex", "grid", "gap", "padding", "margin", "width", "height", "overflow",
               "position", "sticky", "fixed", "z-index", "responsive", "@media",
               "breakpoint", "100vh", "dvh", "container", "max-width", "min-height",
               "columns", "sidebar", "grid-template"],
    "typography": ["font-size", "font-weight", "line-height", "letter-spacing",
                   "text-align", "text-overflow", "ellipsis", "heading", "font-display",
                   "monospace", "text-sm", "text-base", "text-lg", "text-xl",
                   "truncate", "whitespace", "leading-"],
    "forms": ["<input", "<label", "<form", "<textarea", "<select", "placeholder",
              "validation", "required", "pattern=", "type=\"email", "type=\"tel",
              "type=\"password", "autocomplete", "autofocus", "onsubmit",
              "onblur", "oninput", "onchange", "error", "invalid"],
    "navigation": ["<nav", "breadcrumb", "active", "current", "<link", "href",
                    "router", "navigate", "menu", "hamburger", "tab", "route",
                    "pathname", "hash"],
    "accessibility": ["aria-", "role=", "alt=", "sr-only", "screen-reader",
                       "focus-visible", "tabindex", "keyboard", "a11y",
                       "visually-hidden", "skip-to", "announce", "live"],
    "empty-states": ["empty", "no results", "no data", "loading", "skeleton",
                     "placeholder", "zero", "nothing", "error state", "offline",
                     "shimmer"],
    "mobile": ["touch", "mobile", "viewport", "safe-area", "thumb", "swipe",
               "responsive", "inputmode", "tap", "44px", "env(safe-area",
               "@media (max-width", "sm:", "md:"],
    "feedback": ["toast", "notification", "alert", "success", "confirm",
                 "snackbar", "undo", "status", "message", "banner"],
    "design": ["shadow", "border-radius", "rounded", "color", "background",
               "gradient", "dark", "theme", "icon", "avatar", "badge",
               "ring", "outline", "border"],
}


def classify(filename: str, diff_text: str) -> dict:
    text = (filename + " " + diff_text).lower()

    scores = {}
    for category, signals in CATEGORY_SIGNALS.items():
        score = sum(1 for s in signals if s.lower() in text)
        if score > 0:
            scores[category] = score

    if not scores:
        return {
            "category": "general",
            "pattern": f"Unclassified correction in {filename}",
            "is_ux_relevant": True
        }

    best_cat = max(scores, key=scores.get)

    # Extract a rough pattern from the diff
    added_lines = [l[1:].strip() for l in diff_text.split("\n") if l.startswith("+") and not l.startswith("+++")]
    removed_lines = [l[1:].strip() for l in diff_text.split("\n") if l.startswith("-") and not l.startswith("---")]

    # Build a rough description
    if added_lines and removed_lines:
        pattern = f"Changed: '{removed_lines[0][:50]}' → '{added_lines[0][:50]}'"
    elif added_lines:
        pattern = f"Added: '{added_lines[0][:60]}'"
    elif removed_lines:
        pattern = f"Removed: '{removed_lines[0][:60]}'"
    else:
        pattern = f"Correction in {filename}"

    return {
        "category": best_cat,
        "pattern": pattern,
        "is_ux_relevant": True
    }


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    diff_text = sys.stdin.read()
    result = classify(filename, diff_text)
    print(json.dumps(result))

"""
input.py - Handles all user inputs with validation and Elden Ring theming
"""

import sys
from typing import Optional
from rich.prompt import Prompt
from cli import (
    console, print_error, print_info, print_rule, print_npc_dialogue,
    display_class_menu, display_stat_summary, GOLD, AMBER, ASH_WHITE,
    GREY, TEAL, RUNE, ARROW, handle_keyboard_interrupt
)

# ── Constants ─────────────────────────────────────────────────────────────────
ELDEN_RING_CLASSES = [
    "Vagabond", "Warrior", "Hero", "Bandit", "Astrologer",
    "Prophet", "Samurai", "Prisoner", "Confessor", "Wretch",
]

STAT_NAMES = [
    "Vigor", "Mind", "Endurance", "Strength",
    "Dexterity", "Intelligence", "Faith", "Arcane",
]

STAT_MIN = 1
STAT_MAX = 99
PROMPT_MAX_LEN = 5000

# ── NPC Prompts for each stat ─────────────────────────────────────────────────
STAT_NPC_PROMPTS = {
    "Vigor":        "How much HP do you carry, Tarnished?",
    "Mind":         "What is the depth of your Focus, your FP pool?",
    "Endurance":    "How much can your body endure — Stamina and Equip Load?",
    "Strength":     "What is the might of your arm — your Strength?",
    "Dexterity":    "How nimble are your fingers — Dexterity?",
    "Intelligence": "How deep is your arcane mind — Intelligence?",
    "Faith":        "How strong is your devotion — Faith?",
    "Arcane":       "What mysteries do you harbour — Arcane?",
}


def _safe_input(prompt_text: str, default: Optional[str] = None) -> str:
    """Wrapper around Prompt.ask with CTRL+C handling."""
    try:
        value = Prompt.ask(f"  [{GOLD}]{RUNE} {prompt_text}[/{GOLD}]", default=default)
        return value.strip()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


def get_class_choice() -> str:
    """Prompt user to select their Elden Ring starting class."""
    print_rule("Starting Class")
    print_npc_dialogue(
        "Tell me, Tarnished — which vessel carries your grace? Choose your class.",
        npc="Melina"
    )
    console.print()
    display_class_menu(ELDEN_RING_CLASSES)

    while True:
        raw = _safe_input("Enter class name or number")
        if not raw:
            print_error("A class must be chosen. The path requires identity.")
            continue

        # Numeric selection
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(ELDEN_RING_CLASSES):
                chosen = ELDEN_RING_CLASSES[idx]
                console.print(f"\n  [{GOLD}]✦ Class selected:[/{GOLD}] [{ASH_WHITE}]{chosen}[/{ASH_WHITE}]\n")
                return chosen
            else:
                print_error(f"Number must be between 1 and {len(ELDEN_RING_CLASSES)}.")
                continue

        # Name selection (case-insensitive)
        match = next(
            (c for c in ELDEN_RING_CLASSES if c.lower() == raw.lower()), None
        )
        if match:
            console.print(f"\n  [{GOLD}]✦ Class selected:[/{GOLD}] [{ASH_WHITE}]{match}[/{ASH_WHITE}]\n")
            return match

        print_error(
            f"'{raw}' is not a known class. Choose from: {', '.join(ELDEN_RING_CLASSES)}"
        )


def get_stats() -> dict:
    """Prompt user for all 8 stats with validation."""
    print_rule("Current Attributes")
    print_npc_dialogue(
        "Speak your attributes, Tarnished. The Two Fingers must know your foundation.",
        npc="Enia"
    )
    console.print()

    stats = {}
    for stat in STAT_NAMES:
        npc_q = STAT_NPC_PROMPTS.get(stat, f"What is your {stat}?")
        while True:
            raw = _safe_input(f"{stat} (1–99) — {npc_q}", default="10")
            try:
                val = int(raw)
                if STAT_MIN <= val <= STAT_MAX:
                    stats[stat] = val
                    break
                else:
                    print_error(
                        f"{stat} must be between {STAT_MIN} and {STAT_MAX}. "
                        f"Even the weakest Tarnished has at least 1."
                    )
            except ValueError:
                print_error(f"'{raw}' is not a valid number. The runes demand integers.")

    console.print()
    display_stat_summary(stats)
    return stats


def get_build_prompt() -> str:
    """Prompt user for their build description."""
    print_rule("Build Vision")
    print_npc_dialogue(
        "What manner of warrior do you seek to become? Describe your desired legend "
        "— weapons, playstyle, lore, anything. Up to 5000 characters.",
        npc="Roderika"
    )
    console.print()
    console.print(
        f"  [{GREY}]Examples: 'A Strength/Faith build using colossal weapons and Sacred Incantations'[/{GREY}]"
    )
    console.print(
        f"  [{GREY}]          'A stealthy Arcane Bleed build with curved swords and Dragon Communion'[/{GREY}]"
    )
    console.print()

    lines = []
    console.print(f"  [{GOLD}]{RUNE} Describe your build vision[/{GOLD}] [{GREY}](press Enter twice when done)[/{GREY}]:")
    console.print()

    try:
        while True:
            try:
                line = input("    ")
            except KeyboardInterrupt:
                handle_keyboard_interrupt()

            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)

        build_prompt = "\n".join(lines).strip()

        if not build_prompt:
            print_error("A build vision cannot be empty. Speak your intent, Tarnished.")
            return get_build_prompt()

        if len(build_prompt) > PROMPT_MAX_LEN:
            build_prompt = build_prompt[:PROMPT_MAX_LEN]
            print_info(
                f"Your vision exceeded {PROMPT_MAX_LEN} characters. "
                "It has been trimmed to what the Two Fingers can process."
            )

        char_count = len(build_prompt)
        console.print(
            f"\n  [{TEAL}]{ARROW} Prompt captured: {char_count} characters[/{TEAL}]\n"
        )
        return build_prompt

    except KeyboardInterrupt:
        handle_keyboard_interrupt()


def confirm_build_details(class_name: str, stats: dict, prompt: str) -> bool:
    """Show full summary and ask for confirmation."""
    from cli import display_build_summary, confirm_prompt
    display_build_summary(class_name, stats, prompt)
    return confirm_prompt("The Two Fingers have received your offering. Shall we proceed?")


def get_all_inputs() -> dict:
    """Master function: collect all inputs and return as dict."""
    # Class
    class_name = get_class_choice()

    # Stats
    stats = get_stats()

    # Build prompt
    build_prompt = get_build_prompt()

    # Confirm
    if not confirm_build_details(class_name, stats, build_prompt):
        print_npc_dialogue(
            "Very well. Let us begin anew. Your path is yours to reshape.",
            npc="Melina"
        )
        return get_all_inputs()

    return {
        "class": class_name,
        "stats": stats,
        "prompt": build_prompt,
    }
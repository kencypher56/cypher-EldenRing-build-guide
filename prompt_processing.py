"""
prompt_processing.py - Processes user inputs and generates build via deepseek-r1:8b through Ollama
"""

import json
import re
import subprocess
import sys
from typing import Optional

MODEL_NAME = "deepseek-r1:8b"

# ── System Prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an expert Elden Ring build advisor with encyclopedic knowledge of every weapon, armor set, talisman, great rune, spell, and mechanic in the base game and Shadow of the Erdtree DLC.

Your task is to generate a complete, detailed, accurate Elden Ring character build guide in structured JSON format based on the player's starting class, current stats, and desired playstyle.

IMPORTANT RULES:
- All recommendations must be real items that exist in Elden Ring
- Provide precise item locations (area name + specific drop/purchase location)
- Stat recommendations must be realistic and achievable
- Pros/cons must be specific and gameplay-relevant
- Return ONLY valid JSON, no markdown fences, no extra text

Return this exact JSON structure:
{
  "build_name": "string — catchy thematic build name",
  "build_description": "string — 2-3 sentence overview of the playstyle",
  "primary_attribute": "string — main stat to level (e.g. Strength)",
  "secondary_attribute": "string — secondary stat",
  "stat_recommendations": [
    {
      "stat": "Vigor|Mind|Endurance|Strength|Dexterity|Intelligence|Faith|Arcane",
      "current": int,
      "recommended": int,
      "priority": "High|Medium|Low",
      "reason": "string — why this stat matters for the build"
    }
  ],
  "rune_allocation_strategy": "string — general strategy for spending runes",
  "weapons": [
    {
      "name": "string",
      "type": "string — weapon type (e.g. Greatsword)",
      "scaling": "string — e.g. B Strength / D Dexterity",
      "requirement": "string — stat requirements",
      "pros": ["string", "string"],
      "cons": ["string"],
      "location": "string — exact location in the game",
      "ash_of_war": "string — recommended Ash of War"
    }
  ],
  "armor_sets": [
    {
      "name": "string",
      "type": "string — e.g. Medium, Heavy, Light",
      "poise": int,
      "weight": "string — e.g. 28.4",
      "pros": ["string", "string"],
      "cons": ["string"],
      "location": "string — exact location in the game"
    }
  ],
  "talismans": [
    {
      "name": "string",
      "effect": "string — one-line effect description",
      "pros": ["string"],
      "cons": ["string"],
      "location": "string — exact location"
    }
  ],
  "great_runes": [
    {
      "name": "string",
      "holder": "string — which demigod",
      "effect": "string — one-line effect description",
      "pros": ["string"],
      "cons": ["string"],
      "location": "string — how to obtain and activate"
    }
  ],
  "gameplay_tips": ["string", "string", "string"],
  "level_progression": "string — suggested level range and order"
}"""


def build_user_prompt(class_name: str, stats: dict, build_prompt: str) -> str:
    """Construct the user message for the model."""
    stats_str = "\n".join(f"  {stat}: {val}" for stat, val in stats.items())
    return f"""Generate a complete Elden Ring build guide for this character:

**Starting Class:** {class_name}

**Current Stats:**
{stats_str}

**Desired Build / Playstyle:**
{build_prompt}

Provide exactly 3 weapons, 3 armor sets, 8 talismans, and 2 great runes.
Ensure all items exist in Elden Ring and locations are accurate.
Return ONLY the JSON object, no other text."""


def call_ollama(user_prompt: str, on_chunk=None) -> str:
    """
    Call Ollama with streaming output.
    on_chunk: optional callback(str) called with each text chunk.
    Returns the full response text.
    """
    import requests

    payload = {
        "model": MODEL_NAME,
        "prompt": user_prompt,
        "system": SYSTEM_PROMPT,
        "stream": True,
        "options": {
            "temperature": 0.3,
            "top_p": 0.9,
            "num_predict": 4096,
        },
    }

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            stream=True,
            timeout=300,
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Cannot connect to Ollama. "
            "Make sure Ollama is running: `ollama serve`"
        )
    except requests.exceptions.Timeout:
        raise RuntimeError("Ollama request timed out after 5 minutes.")

    full_response = []
    for line in response.iter_lines():
        if not line:
            continue
        try:
            chunk = json.loads(line)
            token = chunk.get("response", "")
            if token:
                full_response.append(token)
                if on_chunk:
                    on_chunk(token)
            if chunk.get("done", False):
                break
        except json.JSONDecodeError:
            continue

    return "".join(full_response)


def extract_json_from_response(raw: str) -> dict:
    """
    Extract and parse JSON from model response.
    Handles cases where the model wraps JSON in markdown or adds text.
    """
    # Strip <think>...</think> blocks (deepseek-r1 chain-of-thought)
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()

    # Try direct parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Try to find JSON block between ```json ... ``` or ``` ... ```
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # Try to find the outermost { ... }
    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(raw[start:end + 1])
        except json.JSONDecodeError:
            pass

    raise ValueError(
        "Model did not return valid JSON. "
        "Try again or simplify your build description."
    )


def validate_build_data(data: dict) -> dict:
    """Ensure the build data has all required fields, filling defaults if needed."""
    defaults = {
        "build_name": "Tarnished's Path",
        "build_description": "A build forged in the Lands Between.",
        "primary_attribute": "Vigor",
        "secondary_attribute": "Strength",
        "stat_recommendations": [],
        "rune_allocation_strategy": "Focus on your primary stat first, then survivability.",
        "weapons": [],
        "armor_sets": [],
        "talismans": [],
        "great_runes": [],
        "gameplay_tips": [],
        "level_progression": "Aim for level 100-125 for most content.",
    }
    for key, default in defaults.items():
        if key not in data:
            data[key] = default

    # Ensure list fields have at minimum empty entries
    if not data["weapons"]:
        data["weapons"] = [{"name": "Longsword", "type": "Straight Sword",
                            "scaling": "D/D", "requirement": "10 Str, 10 Dex",
                            "pros": ["Reliable"], "cons": ["Common"],
                            "location": "Starting gear or early vendors",
                            "ash_of_war": "Storm Blade"}]
    if not data["talismans"]:
        data["talismans"] = []

    return data


def generate_build(
    class_name: str,
    stats: dict,
    build_prompt: str,
    on_token=None,
) -> dict:
    """
    Full pipeline: build prompt → call model → parse JSON → return build dict.
    on_token: optional callback for streaming tokens to the CLI.
    """
    user_prompt = build_user_prompt(class_name, stats, build_prompt)
    raw_response = call_ollama(user_prompt, on_chunk=on_token)

    build_data = extract_json_from_response(raw_response)
    build_data = validate_build_data(build_data)

    # Attach source info
    build_data["_meta"] = {
        "class": class_name,
        "stats": stats,
        "original_prompt": build_prompt,
        "model": MODEL_NAME,
    }

    return build_data
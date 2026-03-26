<div align="center">

<!DOCTYPE html>
<html>
<head>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cinzel+Decorative:wght@400;700&family=IM+Fell+English:ital@0;1&display=swap');

:root {
  --gold: #C9A84C;
  --gold-bright: #FFD700;
  --gold-dim: #8B6914;
  --amber: #FFBF00;
  --parchment: #F5E6C8;
  --dark: #0D0A05;
  --dark-panel: #1A1208;
  --crimson: #8B0000;
  --off-white: #EDE0C4;
  --teal: #1A7A7A;
  --shadow: rgba(0,0,0,0.8);
}
</style>
</head>
</html>

</div>

---

<div align="center">

```
  ╔══════════════════════════════════════════════════════════════════════╗
  ║                                                                      ║
  ║    ███████╗██╗      ██████╗ ███████╗███╗  ██╗    ██████╗ ██╗███╗   ║
  ║    ██╔════╝██║     ██╔══██╗██╔════╝████╗ ██║    ██╔══██╗██║████╗  ║
  ║    █████╗  ██║     ██║  ██║█████╗  ██╔██╗██║    ██████╔╝██║██╔██╗ ║
  ║    ██╔══╝  ██║     ██║  ██║██╔══╝  ██║╚████║    ██╔══██╗██║██║╚██╗║
  ║    ███████╗███████╗██████╔╝███████╗██║ ╚███║    ██║  ██║██║██║ ╚██║
  ║    ╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═║
  ║                                                                      ║
  ║           ⚜  B U I L D   G U I D E   G E N E R A T O R  ⚜          ║
  ║                                                                      ║
  ╚══════════════════════════════════════════════════════════════════════╝
```

**`deepseek-r1:8b`** &nbsp;·&nbsp; **`Ollama`** &nbsp;·&nbsp; **`Python 3.10`** &nbsp;·&nbsp; **`ReportLab`** &nbsp;·&nbsp; **`Rich CLI`**

[![Python](https://img.shields.io/badge/Python-3.10%2B-FFD700?style=for-the-badge&logo=python&logoColor=FFD700&labelColor=1A1208)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-deepseek--r1%3A8b-C9A84C?style=for-the-badge&logoColor=C9A84C&labelColor=1A1208)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-8B6914?style=for-the-badge&labelColor=1A1208)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-FFBF00?style=for-the-badge&labelColor=1A1208)](https://github.com)

</div>

---

<div align="center">

*"Arise now, ye Tarnished. Ye dead, who yet live.*
*The call of long-lost grace speaks to us all..."*

**An immersive CLI tool that channels the wisdom of the Two Fingers through**
**`deepseek-r1:8b` to forge your perfect Elden Ring character build — then inscribes**
**it into a beautifully formatted PDF scroll.**

</div>

---

## ⚜ Table of Contents

- [✦ Overview](#-overview)
- [✦ Features](#-features)  
- [✦ File Structure](#-file-structure)
- [✦ Requirements](#-requirements)
- [✦ Installation & Setup](#-installation--setup)
- [✦ How to Run](#-how-to-run)
- [✦ Usage Walkthrough](#-usage-walkthrough)
- [✦ PDF Output](#-pdf-output)
- [✦ System Detection](#-system-detection)
- [✦ Configuration](#-configuration)
- [✦ Troubleshooting](#-troubleshooting)
- [✦ Credits](#-credits)

---

## ✦ Overview

```
 ┌─────────────────────────────────────────────────────────────────┐
 │                                                                   │
 │   Finger Reader Enia                                              │
 │                                                                   │
 │   "This tool channels the grace of deepseek-r1:8b through        │
 │    Ollama to generate complete character builds. Speak your       │
 │    class, your stats, your vision — and receive your legend."     │
 │                                                                   │
 └─────────────────────────────────────────────────────────────────┘
```

**Cypher Elden Ring Build Guide** is a fully interactive CLI application that:

1. **Guides you** through selecting your class, entering stats, and describing your desired playstyle
2. **Sends your build vision** to `deepseek-r1:8b` running locally via Ollama
3. **Parses the AI response** into a structured build with weapons, armor, talismans, great runes, and stat paths
4. **Generates a polished dark-themed PDF** — `elden_ring_build.pdf` — ready to reference while playing

No internet required after setup. Everything runs **100% locally** on your machine.

---

## ✦ Features

### 🗡 Immersive CLI Experience
- Full **Elden Ring-themed dialogues** — NPCs like Melina, Enia, and Roderika guide you
- **Rich terminal UI** with golden color palette, Unicode symbols, and ornate panels
- **Animated spinners** and progress bars styled to the lore
- Graceful **CTRL+C handling** with thematic farewell messages
- *"The flame fades… your session ends. May your runes guide you."*

### 🛡 Smart Input & Validation
- **Class selection menu** — numbered or named input, with descriptions for all 10 classes
- **Per-stat NPC prompts** — each attribute (Vigor, Mind, Endurance...) has its own flavored question
- **Build prompt** — up to **5,000 characters** of freeform playstyle description
- Real-time **character count** feedback and auto-trim
- Full **confirmation summary** before processing — restart anytime

### ✨ AI-Powered Build Generation
- Uses **`deepseek-r1:8b`** exclusively via Ollama's local API
- **Streaming output** — tokens arrive in real time
- Strips `<think>` chain-of-thought blocks (deepseek-r1 reasoning) automatically
- Structured **JSON enforcement** via system prompt
- Robust **fallback parsing** — handles markdown fences, text wrappers, and partial JSON
- Auto-fills missing fields so the PDF never fails

### 📜 Professional PDF Output
| Section | Contents |
|---|---|
| **Cover Page** | Build name, class, primary stats, model info, golden border |
| **Stat Recommendations** | All 8 stats — current → target, priority (High/Med/Low), reason |
| **Rune Allocation** | Strategic guidance for spending runes across the build |
| **Weapons (×3)** | Name, type, scaling, requirements, Ash of War, pros/cons, location |
| **Armor Sets (×3)** | Name, type, poise, weight, pros/cons, exact location |
| **Talismans (×8)** | Effect description, pros/cons, exact location |
| **Great Runes (×2)** | Demigod holder, effect, activation location |
| **Gameplay Tips** | 3 strategic tips tailored to the build |

- **Dark parchment aesthetic** — deep black background, golden borders on every page
- Color-coded **pros (green) / cons (red) / locations (blue)**
- Priority indicators for stat leveling
- Page numbers and build name in footer

### ⚙ Auto System Setup
- Detects **OS**, **CPU cores**, **NVIDIA GPU** via `nvidia-smi`
- Detects **CUDA availability** via PyTorch if installed
- Automatically starts **Ollama** if installed but not running
- Checks for `deepseek-r1:8b` and pulls it if missing
- Supports **Conda**, **venv**, and **pip** install paths

---

## ✦ File Structure

```
cypher-eldenring-build-guide/
│
├── run.py                ⚔  Main entry point — orchestrates full pipeline
├── setup.py              ⚙  Environment setup, package install, model pull
├── systemdetection.py    🔍 OS, GPU, CUDA, Ollama detection
├── cli.py                ✨ Rich CLI — colors, panels, dialogues, spinners
├── input.py              📋 User input — class, stats, build prompt
├── prompt_processing.py  🧠 Ollama API calls, JSON parsing, validation
├── output_pdf.py         📜 ReportLab PDF generation with full formatting
└── requirements.txt      📦 Python dependencies
```

---

## ✦ Requirements

### System Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| **OS** | Linux / Windows 10 / macOS 12 | Ubuntu 22.04 LTS |
| **Python** | 3.10 | 3.10 – 3.12 |
| **RAM** | 8 GB | 16 GB |
| **Storage** | 6 GB free | 10 GB free |
| **GPU** | Optional (CPU works) | NVIDIA 8GB+ VRAM |
| **Ollama** | 0.1.30+ | Latest |

### Python Packages

```
rich          ≥ 13.0.0    # Terminal UI, colors, panels, progress bars
requests      ≥ 2.28.0    # Ollama REST API communication
reportlab     ≥ 4.0.0     # PDF generation
psutil        ≥ 5.9.0     # CPU/memory system detection
```

### External Tools

```
ollama                    # Local LLM runtime — https://ollama.com
deepseek-r1:8b            # The AI model (~4.9 GB download via Ollama)
```

> **GPU Note:** The tool detects CUDA automatically. With a compatible NVIDIA GPU,  
> `deepseek-r1:8b` generates builds in ~30–60 seconds. CPU-only takes ~3–8 minutes.

---

## ✦ Installation & Setup

### Step 1 — Install Ollama

```bash
# Linux / macOS
curl -fsSL https://ollama.com/install.sh | sh

# Windows — download from:
# https://ollama.com/download/windows
```

### Step 2 — Start Ollama

```bash
ollama serve
```

> Leave this running in a terminal, or Ollama can run as a background service.

### Step 3 — Clone the Project

```bash
git clone https://github.com/yourusername/cypher-eldenring-build-guide.git
cd cypher-eldenring-build-guide
```

### Step 4 — Run Setup

```bash
python3 setup.py
```

The setup wizard will:

```
  ╔══════════════════════════════════════════════╗
  ║   CYPHER ELDEN RING BUILD GUIDE — SETUP       ║
  ╚══════════════════════════════════════════════╝

  ⚙ Detecting system...
  ➤ OS: Linux 6.8.0 (x86_64)
  ➤ Python: 3.10.14
  ✓ GPU detected: NVIDIA GeForce RTX 3070
  ✓ CUDA: Available

  ⚙ Choose installation method:
    1) Conda  — create 'cypher-eldenring' conda environment
    2) venv   — create local .venv virtual environment
    3) pip    — install into current Python environment
```

**Option 1 — Conda** *(recommended if you have Miniconda/Anaconda)*
```bash
# Creates: conda create -n cypher-eldenring python=3.10
# Then installs all packages inside it
Enter choice: 1
```

**Option 2 — venv** *(clean isolated environment)*
```bash
# Creates .venv/ in the project directory
Enter choice: 2
# Activate with: source .venv/bin/activate  (Linux/macOS)
#                .venv\Scripts\activate      (Windows)
```

**Option 3 — pip** *(into current environment)*
```bash
# Or manually: pip install -r requirements.txt
Enter choice: 3
```

After packages are installed, setup will **automatically pull the model**:

```
  ⚙ Checking for model: deepseek-r1:8b...
  ➤ Model not found. Pulling now (~4.9 GB, please wait)...
  ✓ Model deepseek-r1:8b pulled successfully.
```

### Manual Package Install (Alternative)

```bash
pip install rich requests reportlab psutil
# or
pip install -r requirements.txt
```

### Manual Model Pull (Alternative)

```bash
ollama pull deepseek-r1:8b
```

---

## ✦ How to Run

```bash
python3 run.py
```

> If using a conda environment:
> ```bash
> conda activate cypher-eldenring
> python3 run.py
> ```

> If using venv:
> ```bash
> source .venv/bin/activate   # Linux/macOS
> .venv\Scripts\activate       # Windows
> python3 run.py
> ```

---

## ✦ Usage Walkthrough

### 1. Welcome Screen

```
   ███████╗██╗      ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗███╗   ██╗ ██████╗
   ██╔════╝██║     ██╔══██╗██╔════╝████╗  ██║    ██╔══██╗██║████╗  ██║██╔════╝
   ...

              ⚜⚜⚜  BUILD GUIDE GENERATOR  ⚜⚜⚜
           Powered by deepseek-r1:8b · Ollama

  ╔══════════════════════════════════════════════════════╗
  ║  Melina                                               ║
  ║  "Ah, a Tarnished... you've awakened at last."        ║
  ╚══════════════════════════════════════════════════════╝
```

### 2. Class Selection

```
  ┌─── ⚔ Choose Your Starting Class ⚔ ──────────────────────────────┐
  │  #  │  Class       │  Description                                  │
  │─────│──────────────│───────────────────────────────────────────────│
  │  1  │  Vagabond    │  A knight in exile. Melee-focused, high vigor  │
  │  2  │  Warrior     │  Dual wielder. Dex-oriented, light and fast    │
  │  3  │  Hero        │  Mighty warrior. Strength-focused brute        │
  │  ... │             │  ...                                           │
  └─────────────────────────────────────────────────────────────────────┘

  ✦ Enter class name or number: 3
  ✦ Class selected: Hero
```

### 3. Stat Entry

```
  ╔══════════════════════════════════════════════════════╗
  ║  Enia                                                  ║
  ║  "Speak your attributes, Tarnished."                   ║
  ╚══════════════════════════════════════════════════════╝

  ✦ Vigor (1–99) — How much HP do you carry, Tarnished?: 25
  ✦ Mind (1–99) — What is the depth of your Focus?: 15
  ✦ Endurance (1–99) — How much can your body endure?: 20
  ...
```

### 4. Build Prompt

```
  ╔════════════════════════════════════════════════════════════╗
  ║  Roderika                                                    ║
  ║  "What manner of warrior do you seek to become?"             ║
  ╚════════════════════════════════════════════════════════════╝

  ✦ Describe your build vision (press Enter twice when done):

    A Strength/Faith hybrid using Godslayer's Greatsword and
    Black Flame incantations. I want high poise to tank through
    enemy attacks and use Sacred buffs to survive endgame content.

  ➤ Prompt captured: 178 characters
```

### 5. Confirmation & Generation

```
  ─── Build Configuration ──────────────────
  ⚔ Class: Hero
  ✦ Current Stats: Vigor 25 | Str 16 | Fai 10...
  📜 Prompt: A Strength/Faith hybrid...

  ✦ The Two Fingers have received your offering. Shall we proceed? [Y/n]:

  ⠸ The Erdtree channels your destiny...  [0:00:47]
```

### 6. PDF Output

```
  ★ Build 'Godslayer's Crucible Knight' generated successfully.
  ★ Your legend has been inscribed upon the Elden Ring.

  ╔══════════════════════════════════════════════════════╗
  ║  Melina                                               ║
  ║  "Your build has been etched into the Elden Ring.     ║
  ║   Open 'elden_ring_build.pdf' to claim your destiny." ║
  ╚══════════════════════════════════════════════════════╝

  Quick Summary:
    Build:    Godslayer's Crucible Knight
    Class:    Hero
    Primary:  Strength
    PDF:      /home/user/cypher-eldenring-build-guide/elden_ring_build.pdf
```

---

## ✦ PDF Output

The generated `elden_ring_build.pdf` contains:

```
  Page 1 ── Cover
  ┌──────────────────────────────────┐
  │  ⚔  ELDEN RING  ⚔               │  ← Gold title on dark background
  │     BUILD GUIDE                  │
  │  ─────────────────────────────   │
  │  Godslayer's Crucible Knight     │  ← Build name
  │  Class: Hero  │  Str / Fai       │  ← Meta info table
  └──────────────────────────────────┘

  Page 2+ ── Sections
  ⚜ STAT RECOMMENDATIONS & RUNE ALLOCATION
  ⚜ RECOMMENDED WEAPONS
  ⚜ RECOMMENDED ARMOR SETS
  ⚜ RECOMMENDED TALISMANS
  ⚜ GREAT RUNE RECOMMENDATIONS
  ⚜ GAMEPLAY TIPS & STRATEGIES
```

**Design details:**
- 🖤 Deep black background (`#1A1208`) — like the Lands Between at night
- 🟡 Dual gold borders on every page with corner `✦` ornaments  
- 🟢 Pros in green · 🔴 Cons in red · 🔵 Locations in light blue
- 🟠 Priority columns color-coded: High (red) / Medium (amber) / Low (green)
- Footer on every page: *build name · Cypher Elden Ring Build Guide · Page N*

---

## ✦ System Detection

`systemdetection.py` automatically detects:

```python
{
  "os":     { "system": "Linux", "release": "6.8.0", "machine": "x86_64" },
  "cpu":    { "name": "AMD Ryzen 9 5900X", "logical_cores": 24 },
  "cuda":   { "available": true, "device_count": 1,
               "devices": [{ "name": "NVIDIA RTX 3070", "memory_mb": "8192" }] },
  "ollama": { "installed": true, "running": true,
               "models": ["deepseek-r1:8b", "llama3.2:3b"] },
  "python": { "version": "3.10.14", "executable": "/usr/bin/python3" }
}
```

Run it standalone for a system report:
```bash
python3 systemdetection.py
```

---

## ✦ Configuration

### Change the Model

In `prompt_processing.py`, line 8:
```python
MODEL_NAME = "deepseek-r1:8b"   # ← change to any Ollama model
```

Compatible alternatives:
```bash
ollama pull llama3.1:8b          # Meta Llama 3.1
ollama pull mistral:7b           # Mistral 7B
ollama pull deepseek-r1:14b      # Larger, slower, more accurate
```

### Change Output Filename

In `output_pdf.py`, line 18:
```python
OUTPUT_FILE = "elden_ring_build.pdf"   # ← rename as desired
```

### Adjust Model Parameters

In `prompt_processing.py`, inside `call_ollama()`:
```python
"options": {
    "temperature": 0.3,   # ↑ = more creative, ↓ = more precise
    "top_p": 0.9,
    "num_predict": 4096,  # max tokens in response
}
```

### Ollama API URL

Default is `http://localhost:11434`. To change:
```python
# prompt_processing.py, inside call_ollama():
response = requests.post("http://YOUR_HOST:11434/api/generate", ...)
```

---

## ✦ Troubleshooting

### `Cannot connect to Ollama`
```bash
# Make sure Ollama is running:
ollama serve

# Verify it responds:
curl http://localhost:11434
```

### `deepseek-r1:8b not found`
```bash
ollama pull deepseek-r1:8b
# Verify:
ollama list
```

### `ModuleNotFoundError: No module named 'rich'`
```bash
pip install rich requests reportlab psutil
# or
pip install -r requirements.txt
```

### `SyntaxError: f-string expression part cannot include a backslash`
This was a known Python 3.10 compatibility issue — **already fixed** in the current version.  
Make sure you have the latest files from this repository.

### Generation takes too long
```
CPU only can take 3–8 minutes for deepseek-r1:8b.
With a CUDA-capable GPU (8GB+ VRAM), generation drops to ~30–60 seconds.
```

Check GPU detection:
```bash
python3 systemdetection.py
# Look for: "cuda": { "available": true }
```

### PDF not opening / corrupted
```bash
# Verify it was generated:
ls -lh elden_ring_build.pdf

# Try opening with evince, okular, or any PDF reader:
evince elden_ring_build.pdf
```

### Model returns invalid JSON
The tool has three layers of JSON recovery:
1. Direct parse
2. Markdown fence extraction ` ```json ... ``` `
3. Outermost `{ }` scan

If all fail, simplify your build prompt and try again. Very long or complex prompts occasionally cause the model to deviate from the JSON schema.

---

## ✦ Credits

```
  ╔══════════════════════════════════════════════════════════════════╗
  ║                                                                    ║
  ║   ⚔  Cypher Elden Ring Build Guide                                ║
  ║      Built with dark gold and Tarnished determination.            ║
  ║                                                                    ║
  ║   🧠  AI Engine:    deepseek-r1:8b via Ollama                     ║
  ║   🖥  CLI:          Rich (by Will McGugan)                        ║
  ║   📜  PDF:          ReportLab                                     ║
  ║   🎮  Lore:         Elden Ring © FromSoftware / Bandai Namco      ║
  ║                                                                    ║
  ║   This is a fan project. Not affiliated with FromSoftware.        ║
  ║                                                                    ║
  ╚══════════════════════════════════════════════════════════════════╝
```

- [**Ollama**](https://ollama.com) — Local LLM runtime
- [**deepseek-r1**](https://github.com/deepseek-ai/DeepSeek-R1) — DeepSeek AI
- [**Rich**](https://github.com/Textualize/rich) — Terminal formatting library
- [**ReportLab**](https://www.reportlab.com) — PDF generation toolkit
- **Elden Ring** — FromSoftware / George R.R. Martin — the world that inspired it all

---

<div align="center">

```
  ── ⚜ ─────────────────────────────────────────────── ⚜ ──

     May your runes guide thee, and may the grace of gold
          ever shine upon your path, Tarnished.

  ── ⚜ ─────────────────────────────────────────────── ⚜ ──
```

*"The Elden Ring is shattered. But your build guide need not be."*

</div>
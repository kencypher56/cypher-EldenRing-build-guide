<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cypher · Elden Ring Build Guide</title>
    <!-- GitHub‑safe styling – inline only, no external dependencies -->
</head>
<body>

<div align="center">

<!-- ========== CORRECTED ASCII BANNER: ELDEN RING ========== -->
<pre style="font-family: monospace; color: #d4af37; background-color: #0a0a0a; padding: 1rem; border-radius: 12px; border: 1px solid #c9a84c; line-height: 1.2;">
   ███████╗██╗      ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗███╗   ██╗ ██████╗
   ██╔════╝██║     ██╔══██╗██╔════╝████╗  ██║    ██╔══██╗██║████╗  ██║██╔════╝
   █████╗  ██║     ██║  ██║█████╗  ██╔██╗ ██║    ██████╔╝██║██╔██╗ ██║██║  ███╗
   ██╔══╝  ██║     ██║  ██║██╔══╝  ██║╚██╗██║    ██╔══██╗██║██║╚██╗██║██║   ██║
   ███████╗███████╗██████╔╝███████╗██║ ╚████║    ██║  ██║██║██║ ╚████║╚██████╔╝
   ╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
</pre>

<p>
  <strong>deepseek-r1:8b</strong> &nbsp;·&nbsp;
  <strong>Ollama</strong> &nbsp;·&nbsp;
  <strong>Python 3.10+</strong> &nbsp;·&nbsp;
  <strong>ReportLab</strong> &nbsp;·&nbsp;
  <strong>Rich CLI</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFD700?style=for-the-badge&logo=python&logoColor=FFD700&labelColor=1A1208" alt="Python">
  <img src="https://img.shields.io/badge/Ollama-deepseek--r1%3A8b-C9A84C?style=for-the-badge&logoColor=C9A84C&labelColor=1A1208" alt="Ollama">
  <img src="https://img.shields.io/badge/License-MIT-8B6914?style=for-the-badge&labelColor=1A1208" alt="License">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-FFBF00?style=for-the-badge&labelColor=1A1208" alt="Platform">
</p>

<blockquote>
  <em>“Arise now, ye Tarnished. Ye dead, who yet live.<br>
  The call of long-lost grace speaks to us all...”</em>
</blockquote>

<p>
  <strong>An immersive CLI tool that channels the wisdom of the Two Fingers through <code>deepseek-r1:8b</code><br>
  to forge your perfect Elden Ring character build — then inscribes it into a beautifully formatted PDF scroll.</strong>
</p>

</div>

<hr>

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

<div style="border-left: 4px solid #c9a84c; background: #1a1208; padding: 1rem; margin: 1.5rem 0; border-radius: 8px;">
  <strong>📜 Finger Reader Enia</strong><br>
  <em>“This tool channels the grace of deepseek-r1:8b through Ollama to generate complete character builds. Speak your class, your stats, your vision — and receive your legend.”</em>
</div>

**Cypher Elden Ring Build Guide** is a fully interactive CLI application that:

1. 🔥 Guides you through class, stats, and playstyle vision  
2. 🧠 Sends your build vision to `deepseek-r1:8b` via Ollama (local LLM)  
3. ⚙️ Parses the AI response into structured build data  
4. 📜 Generates a polished **dark-themed PDF** — `elden_ring_build.pdf` — ready for your journey  

> 🧙‍♂️ No internet required after setup. Everything runs **100% locally** on your machine.

---

## ✦ Features

| 🗡️ Immersive CLI            | 🛡️ Smart Input & Validation        | ✨ AI-Powered Generation        | 📜 Professional PDF          |
|-----------------------------|------------------------------------|--------------------------------|------------------------------|
| Elden Ring‑themed dialogues | Class selection (10 classes)       | `deepseek-r1:8b` via Ollama    | Dark parchment aesthetic     |
| Rich terminal UI (gold)     | Per‑stat NPC prompts               | Streaming real‑time output     | Stat recommendations         |
| Animated spinners & panels  | Build prompt up to 5000 chars      | Strips `<think>` blocks        | Weapons, armor, talismans    |
| Graceful CTRL+C handling    | Full confirmation summary          | JSON enforcement & fallback    | Great Runes & gameplay tips  |
| Thematic farewell messages  | Auto‑trim & validation             | Auto‑fills missing fields      | Color‑coded pros/cons        |

---

## ✦ File Structure

```text
cypher-eldenring-build-guide/
├── run.py                ⚔  Main entry point
├── setup.py              ⚙  Environment & model setup
├── systemdetection.py    🔍 OS, GPU, CUDA, Ollama detection
├── cli.py                ✨ Rich CLI — colors, dialogues, spinners
├── input.py              📋 User input — class, stats, prompt
├── prompt_processing.py  🧠 Ollama API calls, JSON parsing
├── output_pdf.py         📜 ReportLab PDF generation
└── requirements.txt      📦 Python dependencies
```

---

## ✦ Requirements

| Requirement  | Minimum                | Recommended                |
|--------------|------------------------|----------------------------|
| **OS**       | Linux / Win10 / macOS  | Ubuntu 22.04 LTS           |
| **Python**   | 3.10                   | 3.10 – 3.12                |
| **RAM**      | 8 GB                   | 16 GB                      |
| **Storage**  | 6 GB free              | 10 GB free                 |
| **GPU**      | Optional (CPU works)   | NVIDIA 8GB+ VRAM           |
| **Ollama**   | 0.1.30+                | Latest                     |

**Python packages** (auto‑installed by `setup.py`):
```bash
rich          # terminal UI
requests      # Ollama API
reportlab     # PDF generation
psutil        # system detection
```

**External tools**:
- [Ollama](https://ollama.com) – local LLM runtime  
- `deepseek-r1:8b` – ~4.9 GB model (pulled automatically)

> 💡 With a CUDA‑capable GPU, generation takes ~30‑60 sec; CPU only takes 3‑8 minutes.

---

## ✦ Installation & Setup

### 1️⃣ Install Ollama
```bash
# Linux / macOS
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download from https://ollama.com/download/windows
```

### 2️⃣ Start Ollama (keep running)
```bash
ollama serve
```

### 3️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/cypher-eldenring-build-guide.git
cd cypher-eldenring-build-guide
```

### 4️⃣ Run setup wizard
```bash
python3 setup.py
```
The wizard will:
- Detect your OS, CPU, GPU (CUDA)
- Offer **Conda**, **venv**, or **pip** installation
- Install required Python packages
- Pull `deepseek-r1:8b` automatically if missing

> ✅ Manual alternative: `pip install -r requirements.txt` and `ollama pull deepseek-r1:8b`

---

## ✦ How to Run

```bash
python3 run.py
```
> For conda env: `conda activate cypher-eldenring` first  
> For venv: activate with `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)

---

## ✦ Usage Walkthrough

<details>
<summary><strong>📖 Click to see an example session</strong></summary>

1. **Welcome** – Melina greets you with golden banners.  
2. **Class Selection** – Choose by number or name from 10 classes (Vagabond, Hero, Samurai, etc.).  
3. **Stat Entry** – Enia asks for each attribute (Vigor, Mind, Endurance, Strength, etc.).  
4. **Build Prompt** – Roderika invites your vision: describe playstyle, weapon preference, spell type, up to 5000 characters.  
5. **Confirmation** – Review your choices, then confirm.  
6. **Generation** – The Erdtree spins while `deepseek-r1:8b` creates your build.  
7. **PDF Creation** – A detailed PDF is generated and saved.  
8. **Farewell** – Melina bids you farewell with your build summary.

</details>

---

## ✦ PDF Output

Your build is immortalized in a dark, lore‑rich PDF with the following sections:

| Section                 | Content                                                  |
|-------------------------|----------------------------------------------------------|
| **Cover**               | Build name, class, primary stats, golden border          |
| **Stat Recommendations**| Each stat → target, priority (High/Med/Low), reason      |
| **Rune Allocation**     | Strategic guidance for spending runes                    |
| **Weapons (×3)**        | Name, type, scaling, Ash of War, pros/cons, location     |
| **Armor Sets (×3)**     | Poise, weight, pros/cons, location                       |
| **Talismans (×8)**      | Effect, pros/cons, exact location                        |
| **Great Runes (×2)**    | Demigod, effect, activation site                         |
| **Gameplay Tips**       | 3 custom strategies                                      |

> 🔹 Pros in <span style="color:#7cb518;">green</span> · Cons in <span style="color:#d64531;">red</span> · Locations in <span style="color:#4c9aff;">blue</span> · Priority color‑coded.

---

## ✦ System Detection

The built‑in `systemdetection.py` prints detailed info:
- OS, CPU cores, RAM
- NVIDIA GPU & CUDA availability (via PyTorch or nvidia‑smi)
- Ollama status and installed models
- Python version & environment

Run standalone:
```bash
python3 systemdetection.py
```

---

## ✦ Configuration

- **Change model**: edit `MODEL_NAME` in `prompt_processing.py`  
  e.g., `llama3.1:8b`, `mistral:7b`  
- **Output filename**: modify `OUTPUT_FILE` in `output_pdf.py`  
- **Model parameters**: inside `call_ollama()` adjust `temperature`, `num_predict`, etc.  
- **Ollama URL**: default `http://localhost:11434` – change if needed.

---

## ✦ Troubleshooting

<details>
<summary><strong>❌ Cannot connect to Ollama</strong></summary>

```bash
ollama serve          # start server
curl http://localhost:11434   # should respond
```
</details>

<details>
<summary><strong>❌ deepseek-r1:8b not found</strong></summary>

```bash
ollama pull deepseek-r1:8b
ollama list            # verify
```
</details>

<details>
<summary><strong>❌ ModuleNotFoundError</strong></summary>

```bash
pip install -r requirements.txt
# or manually: pip install rich requests reportlab psutil
```
</details>

<details>
<summary><strong>❌ PDF generation fails or is corrupted</strong></summary>

- Check that `reportlab` is installed correctly.  
- Ensure you have write permissions in the current directory.  
- Try opening with a different PDF reader (Evince, Adobe Acrobat).  
- Re‑run the build process; sometimes the model returns invalid JSON, but the tool includes fallback parsing.
</details>

<details>
<summary><strong>🐢 Generation takes too long</strong></summary>

- Use a GPU with at least 8GB VRAM (CUDA).  
- Run `python3 systemdetection.py` to verify CUDA availability.  
- Lower `num_predict` in `prompt_processing.py` (e.g., 2048) for faster responses.
</details>

---

## ✦ Credits

<div align="center" style="border-top: 1px solid #c9a84c; border-bottom: 1px solid #c9a84c; padding: 1.2rem; margin: 2rem 0;">
  <p>⚔ <strong>Cypher Elden Ring Build Guide</strong> ⚔<br>
  Built with dark gold and Tarnished determination.</p>
  <p>🧠 AI Engine: <strong>deepseek-r1:8b</strong> via <strong>Ollama</strong><br>
  🖥 CLI: <strong>Rich</strong> (Will McGugan)<br>
  📜 PDF: <strong>ReportLab</strong><br>
  🎮 Lore: <strong>Elden Ring</strong> © FromSoftware / Bandai Namco</p>
  <p><em>This is a fan project. Not affiliated with FromSoftware.</em></p>
</div>

<!-- ========== CENTERED FOOTER (fixed) ========== -->
<div align="center">
  <pre style="font-family: monospace; color: #c9a84c; margin: 1.5rem auto;">
  ── ⚜ ─────────────────────────────────────────────── ⚜ ──

     May your runes guide thee, and may the grace of gold
          ever shine upon your path, Tarnished.

  ── ⚜ ─────────────────────────────────────────────── ⚜ ──
  </pre>
  <p><em>“The Elden Ring is shattered. But your build guide need not be.”</em></p>
</div>

</body>
</html>

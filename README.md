<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cypher · Elden Ring Build Guide</title>
    <!-- No external dependencies – pure GitHub‑compatible HTML/CSS -->
    <style>
        body {
            background-color: #0a0a0a;
            color: #ede0c4;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            line-height: 1.5;
            margin: 2rem auto;
            max-width: 1200px;
            padding: 0 1rem;
        }
        a {
            color: #c9a84c;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
            color: #ffd700;
        }
        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #c9a84c, transparent);
            margin: 2rem 0;
        }
        pre, code {
            font-family: 'SF Mono', 'Fira Code', monospace;
            background-color: #1a1208;
            border-radius: 8px;
            padding: 0.2rem 0.4rem;
        }
        pre {
            padding: 1rem;
            overflow-x: auto;
        }
        blockquote {
            border-left: 4px solid #c9a84c;
            background-color: #1a1208;
            margin: 1.5rem 0;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            font-style: italic;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1rem 0;
        }
        th, td {
            border: 1px solid #c9a84c;
            padding: 0.75rem;
            text-align: left;
        }
        th {
            background-color: #1a1208;
            color: #ffd700;
        }
        summary {
            cursor: pointer;
            font-weight: bold;
            color: #c9a84c;
        }
        .gold-border {
            border: 1px solid #c9a84c;
            border-radius: 12px;
            padding: 1rem;
            margin: 1rem 0;
        }
        .centered-footer {
            text-align: center;
            margin-top: 3rem;
        }
        .ascii-banner {
            font-family: monospace;
            color: #d4af37;
            background-color: #0a0a0a;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #c9a84c;
            line-height: 1.2;
            white-space: pre;
            overflow-x: auto;
        }
    </style>
</head>
<body>

<div align="center">

<!-- ========== CORRECTED ASCII BANNER: ELDEN RING ========== -->
<div class="ascii-banner">
   ███████╗██╗      ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗███╗   ██╗ ██████╗
   ██╔════╝██║     ██╔══██╗██╔════╝████╗  ██║    ██╔══██╗██║████╗  ██║██╔════╝
   █████╗  ██║     ██║  ██║█████╗  ██╔██╗ ██║    ██████╔╝██║██╔██╗ ██║██║  ███╗
   ██╔══╝  ██║     ██║  ██║██╔══╝  ██║╚██╗██║    ██╔══██╗██║██║╚██╗██║██║   ██║
   ███████╗███████╗██████╔╝███████╗██║ ╚████║    ██║  ██║██║██║ ╚████║╚██████╔╝
   ╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
</div>

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

<h2>⚜ Table of Contents</h2>
<ul>
  <li><a href="#-overview">✦ Overview</a></li>
  <li><a href="#-features">✦ Features</a></li>
  <li><a href="#-file-structure">✦ File Structure</a></li>
  <li><a href="#-requirements">✦ Requirements</a></li>
  <li><a href="#-installation--setup">✦ Installation &amp; Setup</a></li>
  <li><a href="#-how-to-run">✦ How to Run</a></li>
  <li><a href="#-usage-walkthrough">✦ Usage Walkthrough</a></li>
  <li><a href="#-pdf-output">✦ PDF Output</a></li>
  <li><a href="#-system-detection">✦ System Detection</a></li>
  <li><a href="#-configuration">✦ Configuration</a></li>
  <li><a href="#-troubleshooting">✦ Troubleshooting</a></li>
  <li><a href="#-credits">✦ Credits</a></li>
</ul>

<hr>

<h2 id="-overview">✦ Overview</h2>

<div class="gold-border">
  <strong>📜 Finger Reader Enia</strong><br>
  <em>“This tool channels the grace of deepseek-r1:8b through Ollama to generate complete character builds. Speak your class, your stats, your vision — and receive your legend.”</em>
</div>

<p><strong>Cypher Elden Ring Build Guide</strong> is a fully interactive CLI application that:</p>
<ol>
  <li>🔥 Guides you through class, stats, and playstyle vision</li>
  <li>🧠 Sends your build vision to <code>deepseek-r1:8b</code> via Ollama (local LLM)</li>
  <li>⚙️ Parses the AI response into structured build data</li>
  <li>📜 Generates a polished <strong>dark-themed PDF</strong> — <code>elden_ring_build.pdf</code> — ready for your journey</li>
</ol>
<blockquote>🧙‍♂️ No internet required after setup. Everything runs <strong>100% locally</strong> on your machine.</blockquote>

<hr>

<h2 id="-features">✦ Features</h2>

<table>
  <thead>
    <tr><th>🗡️ Immersive CLI</th><th>🛡️ Smart Input &amp; Validation</th><th>✨ AI-Powered Generation</th><th>📜 Professional PDF</th></tr>
  </thead>
  <tbody>
    <tr><td>Elden Ring‑themed dialogues</td><td>Class selection (10 classes)</td><td><code>deepseek-r1:8b</code> via Ollama</td><td>Dark parchment aesthetic</td></tr>
    <tr><td>Rich terminal UI (gold)</td><td>Per‑stat NPC prompts</td><td>Streaming real‑time output</td><td>Stat recommendations</td></tr>
    <tr><td>Animated spinners &amp; panels</td><td>Build prompt up to 5000 chars</td><td>Strips <code>&lt;think&gt;</code> blocks</td><td>Weapons, armor, talismans</td></tr>
    <tr><td>Graceful CTRL+C handling</td><td>Full confirmation summary</td><td>JSON enforcement &amp; fallback</td><td>Great Runes &amp; gameplay tips</td></tr>
    <tr><td>Thematic farewell messages</td><td>Auto‑trim &amp; validation</td><td>Auto‑fills missing fields</td><td>Color‑coded pros/cons</td></tr>
  </tbody>
</table>

<hr>

<h2 id="-file-structure">✦ File Structure</h2>

<pre>
cypher-eldenring-build-guide/
├── run.py                ⚔  Main entry point
├── setup.py              ⚙  Environment &amp; model setup
├── systemdetection.py    🔍 OS, GPU, CUDA, Ollama detection
├── cli.py                ✨ Rich CLI — colors, dialogues, spinners
├── input.py              📋 User input — class, stats, prompt
├── prompt_processing.py  🧠 Ollama API calls, JSON parsing
├── output_pdf.py         📜 ReportLab PDF generation
└── requirements.txt      📦 Python dependencies
</pre>

<hr>

<h2 id="-requirements">✦ Requirements</h2>

<table>
  <thead><tr><th>Requirement</th><th>Minimum</th><th>Recommended</th></tr></thead>
  <tbody>
    <tr><td><strong>OS</strong></td><td>Linux / Win10 / macOS</td><td>Ubuntu 22.04 LTS</td></tr>
    <tr><td><strong>Python</strong></td><td>3.10</td><td>3.10 – 3.12</td></tr>
    <tr><td><strong>RAM</strong></td><td>8 GB</td><td>16 GB</td></tr>
    <tr><td><strong>Storage</strong></td><td>6 GB free</td><td>10 GB free</td></tr>
    <tr><td><strong>GPU</strong></td><td>Optional (CPU works)</td><td>NVIDIA 8GB+ VRAM</td></tr>
    <tr><td><strong>Ollama</strong></td><td>0.1.30+</td><td>Latest</td></tr>
  </tbody>
</table>

<p><strong>Python packages</strong> (auto‑installed by <code>setup.py</code>):</p>
<pre><code>rich          # terminal UI
requests      # Ollama API
reportlab     # PDF generation
psutil        # system detection
</code></pre>

<p><strong>External tools</strong>:</p>
<ul>
  <li><a href="https://ollama.com">Ollama</a> – local LLM runtime</li>
  <li><code>deepseek-r1:8b</code> – ~4.9 GB model (pulled automatically)</li>
</ul>
<blockquote>💡 With a CUDA‑capable GPU, generation takes ~30‑60 sec; CPU only takes 3‑8 minutes.</blockquote>

<hr>

<h2 id="-installation--setup">✦ Installation &amp; Setup</h2>

<h3>1️⃣ Install Ollama</h3>
<pre><code># Linux / macOS
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download from https://ollama.com/download/windows
</code></pre>

<h3>2️⃣ Start Ollama (keep running)</h3>
<pre><code>ollama serve
</code></pre>

<h3>3️⃣ Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/cypher-eldenring-build-guide.git
cd cypher-eldenring-build-guide
</code></pre>

<h3>4️⃣ Run setup wizard</h3>
<pre><code>python3 setup.py
</code></pre>
<p>The wizard will:</p>
<ul>
  <li>Detect your OS, CPU, GPU (CUDA)</li>
  <li>Offer <strong>Conda</strong>, <strong>venv</strong>, or <strong>pip</strong> installation</li>
  <li>Install required Python packages</li>
  <li>Pull <code>deepseek-r1:8b</code> automatically if missing</li>
</ul>
<blockquote>✅ Manual alternative: <code>pip install -r requirements.txt</code> and <code>ollama pull deepseek-r1:8b</code></blockquote>

<hr>

<h2 id="-how-to-run">✦ How to Run</h2>

<pre><code>python3 run.py
</code></pre>
<blockquote>For conda env: <code>conda activate cypher-eldenring</code> first<br>
For venv: activate with <code>source .venv/bin/activate</code> (Linux/macOS) or <code>.venv\Scripts\activate</code> (Windows)</blockquote>

<hr>

<h2 id="-usage-walkthrough">✦ Usage Walkthrough</h2>

<details>
<summary><strong>📖 Click to see an example session</strong></summary>
<ol>
  <li><strong>Welcome</strong> – Melina greets you with golden banners.</li>
  <li><strong>Class Selection</strong> – Choose by number or name from 10 classes (Vagabond, Hero, Samurai, etc.).</li>
  <li><strong>Stat Entry</strong> – Enia asks for each attribute (Vigor, Mind, Endurance, Strength, etc.).</li>
  <li><strong>Build Prompt</strong> – Roderika invites your vision: describe playstyle, weapon preference, spell type, up to 5000 characters.</li>
  <li><strong>Confirmation</strong> – Review your choices, then confirm.</li>
  <li><strong>Generation</strong> – The Erdtree spins while <code>deepseek-r1:8b</code> creates your build.</li>
  <li><strong>PDF Creation</strong> – A detailed PDF is generated and saved.</li>
  <li><strong>Farewell</strong> – Melina bids you farewell with your build summary.</li>
</ol>
</details>

<hr>

<h2 id="-pdf-output">✦ PDF Output</h2>

<p>Your build is immortalized in a dark, lore‑rich PDF with the following sections:</p>

<table>
  <thead><tr><th>Section</th><th>Content</th></tr></thead>
  <tbody>
    <tr><td><strong>Cover</strong></td><td>Build name, class, primary stats, golden border</td></tr>
    <tr><td><strong>Stat Recommendations</strong></td><td>Each stat → target, priority (High/Med/Low), reason</td></tr>
    <tr><td><strong>Rune Allocation</strong></td><td>Strategic guidance for spending runes</td></tr>
    <tr><td><strong>Weapons (×3)</strong></td><td>Name, type, scaling, Ash of War, pros/cons, location</td></tr>
    <tr><td><strong>Armor Sets (×3)</strong></td><td>Poise, weight, pros/cons, location</td></tr>
    <tr><td><strong>Talismans (×8)</strong></td><td>Effect, pros/cons, exact location</td></tr>
    <tr><td><strong>Great Runes (×2)</strong></td><td>Demigod, effect, activation site</td></tr>
    <tr><td><strong>Gameplay Tips</strong></td><td>3 custom strategies</td></tr>
  </tbody>
</table>

<blockquote>🔹 Pros in <span style="color:#7cb518;">green</span> · Cons in <span style="color:#d64531;">red</span> · Locations in <span style="color:#4c9aff;">blue</span> · Priority color‑coded.</blockquote>

<hr>

<h2 id="-system-detection">✦ System Detection</h2>

<p>The built‑in <code>systemdetection.py</code> prints detailed info:</p>
<ul>
  <li>OS, CPU cores, RAM</li>
  <li>NVIDIA GPU &amp; CUDA availability (via PyTorch or nvidia‑smi)</li>
  <li>Ollama status and installed models</li>
  <li>Python version &amp; environment</li>
</ul>
<p>Run standalone:</p>
<pre><code>python3 systemdetection.py
</code></pre>

<hr>

<h2 id="-configuration">✦ Configuration</h2>

<ul>
  <li><strong>Change model</strong>: edit <code>MODEL_NAME</code> in <code>prompt_processing.py</code><br>
  e.g., <code>llama3.1:8b</code>, <code>mistral:7b</code></li>
  <li><strong>Output filename</strong>: modify <code>OUTPUT_FILE</code> in <code>output_pdf.py</code></li>
  <li><strong>Model parameters</strong>: inside <code>call_ollama()</code> adjust <code>temperature</code>, <code>num_predict</code>, etc.</li>
  <li><strong>Ollama URL</strong>: default <code>http://localhost:11434</code> – change if needed.</li>
</ul>

<hr>

<h2 id="-troubleshooting">✦ Troubleshooting</h2>

<details>
<summary><strong>❌ Cannot connect to Ollama</strong></summary>
<pre><code>ollama serve          # start server
curl http://localhost:11434   # should respond
</code></pre>
</details>

<details>
<summary><strong>❌ deepseek-r1:8b not found</strong></summary>
<pre><code>ollama pull deepseek-r1:8b
ollama list            # verify
</code></pre>
</details>

<details>
<summary><strong>❌ ModuleNotFoundError</strong></summary>
<pre><code>pip install -r requirements.txt
# or manually: pip install rich requests reportlab psutil
</code></pre>
</details>

<details>
<summary><strong>❌ PDF generation fails or is corrupted</strong></summary>
<ul>
  <li>Check that <code>reportlab</code> is installed correctly.</li>
  <li>Ensure you have write permissions in the current directory.</li>
  <li>Try opening with a different PDF reader (Evince, Adobe Acrobat).</li>
  <li>Re‑run the build process; sometimes the model returns invalid JSON, but the tool includes fallback parsing.</li>
</ul>
</details>

<details>
<summary><strong>🐢 Generation takes too long</strong></summary>
<ul>
  <li>Use a GPU with at least 8GB VRAM (CUDA).</li>
  <li>Run <code>python3 systemdetection.py</code> to verify CUDA availability.</li>
  <li>Lower <code>num_predict</code> in <code>prompt_processing.py</code> (e.g., 2048) for faster responses.</li>
</ul>
</details>

<hr>

<h2 id="-credits">✦ Credits</h2>

<div align="center" style="border-top: 1px solid #c9a84c; border-bottom: 1px solid #c9a84c; padding: 1.2rem; margin: 2rem 0;">
  <p>⚔ <strong>Cypher Elden Ring Build Guide</strong> ⚔<br>
  Built with dark gold and Tarnished determination.</p>
  <p>🧠 AI Engine: <strong>deepseek-r1:8b</strong> via <strong>Ollama</strong><br>
  🖥 CLI: <strong>Rich</strong> (Will McGugan)<br>
  📜 PDF: <strong>ReportLab</strong><br>
  🎮 Lore: <strong>Elden Ring</strong> © FromSoftware / Bandai Namco</p>
  <p><em>This is a fan project. Not affiliated with FromSoftware.</em></p>
</div>

<!-- ========== CENTERED FOOTER (final) ========== -->
<div align="center" style="margin: 3rem 0 2rem;">
  <pre style="font-family: monospace; color: #c9a84c; background: none; padding: 0; margin: 0 auto;">
  ── ⚜ ─────────────────────────────────────────────── ⚜ ──

     May your runes guide thee, and may the grace of gold
          ever shine upon your path, Tarnished.

  ── ⚜ ─────────────────────────────────────────────── ⚜ ──
  </pre>
  <p><em>“The Elden Ring is shattered. But your build guide need not be.”</em></p>
</div>

</body>
</html>

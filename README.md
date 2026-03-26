<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cypher — Elden Ring Build Guide Generator</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cinzel+Decorative:wght@400;700&family=IM+Fell+English:ital@0;1&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
/* ── Reset & Root ───────────────────────────────────────────── */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --gold:        #C9A84C;
  --gold-bright: #FFD700;
  --gold-dim:    #8B6E1E;
  --gold-deep:   #5C3D00;
  --amber:       #FFBF00;
  --parchment:   #F5E6C8;
  --dark:        #08060200;
  --dark-bg:     #0D0A04;
  --dark-panel:  #1A1208;
  --dark-card:   #140F06;
  --mid-brown:   #2E1F08;
  --crimson:     #8B1A1A;
  --crimson-dim: #4A0E0E;
  --green-rune:  #4CAF50;
  --red-rune:    #E53935;
  --blue-rune:   #64B5F6;
  --teal:        #1A7A7A;
  --off-white:   #EDE0C4;
  --grey:        #9A8B6E;
  --shadow:      rgba(0,0,0,0.85);
}

html { scroll-behavior: smooth; }

body {
  background-color: var(--dark-bg);
  color: var(--off-white);
  font-family: 'IM Fell English', Georgia, serif;
  font-size: 15px;
  line-height: 1.75;
  overflow-x: hidden;
  cursor: default;
}

/* ── Noise texture overlay ──────────────────────────────────── */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: 0.4;
}

/* ── Scrollbar ──────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--dark-bg); }
::-webkit-scrollbar-thumb { background: var(--gold-dim); border-radius: 3px; }

/* ── Animations ─────────────────────────────────────────────── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes goldPulse {
  0%,100% { text-shadow: 0 0 8px rgba(201,168,76,0.4), 0 0 20px rgba(201,168,76,0.2); }
  50%     { text-shadow: 0 0 18px rgba(255,215,0,0.7), 0 0 40px rgba(255,191,0,0.4); }
}
@keyframes borderGlow {
  0%,100% { box-shadow: 0 0 8px rgba(201,168,76,0.3), inset 0 0 8px rgba(201,168,76,0.05); }
  50%     { box-shadow: 0 0 24px rgba(255,215,0,0.5), inset 0 0 16px rgba(201,168,76,0.1); }
}
@keyframes runeFloat {
  0%,100% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
  50%     { transform: translateY(-12px) rotate(5deg); opacity: 0.6; }
}
@keyframes scanline {
  0%   { transform: translateY(-100%); }
  100% { transform: translateY(100vh); }
}
@keyframes flicker {
  0%,19%,21%,23%,25%,54%,56%,100% { opacity: 1; }
  20%,24%,55% { opacity: 0.6; }
}

/* ── Layout wrapper ─────────────────────────────────────────── */
.page {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 24px 80px;
  position: relative;
  z-index: 1;
}

/* ── Hero / Header ──────────────────────────────────────────── */
.hero {
  text-align: center;
  padding: 64px 0 48px;
  position: relative;
  animation: fadeUp 1.2s ease both;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0; left: 50%;
  transform: translateX(-50%);
  width: 600px; height: 600px;
  background: radial-gradient(ellipse at center, rgba(201,168,76,0.08) 0%, transparent 70%);
  pointer-events: none;
}

/* Floating rune decorations */
.rune-bg {
  position: absolute;
  font-size: 80px;
  opacity: 0.06;
  pointer-events: none;
  color: var(--gold);
}
.rune-bg.r1 { top: 30px; left: 40px; animation: runeFloat 7s ease-in-out infinite; }
.rune-bg.r2 { top: 50px; right: 50px; animation: runeFloat 9s ease-in-out infinite 1s; font-size: 60px; }
.rune-bg.r3 { top: 180px; left: 10px; animation: runeFloat 11s ease-in-out infinite 2s; font-size: 40px; }
.rune-bg.r4 { top: 160px; right: 20px; animation: runeFloat 8s ease-in-out infinite 3s; font-size: 50px; }

.logo-ascii {
  font-family: 'Share Tech Mono', monospace;
  font-size: clamp(5px, 1.1vw, 11px);
  line-height: 1.2;
  color: var(--gold);
  display: inline-block;
  text-shadow: 0 0 12px rgba(201,168,76,0.6);
  animation: goldPulse 4s ease-in-out infinite;
  letter-spacing: 0.02em;
  white-space: pre;
}

.hero-subtitle {
  font-family: 'Cinzel', serif;
  font-size: 11px;
  letter-spacing: 0.35em;
  color: var(--amber);
  text-transform: uppercase;
  margin-top: 16px;
  opacity: 0.9;
}

.hero-tagline {
  font-family: 'IM Fell English', serif;
  font-style: italic;
  font-size: 15px;
  color: var(--grey);
  margin-top: 10px;
  letter-spacing: 0.05em;
}

.badge-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 28px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 14px;
  border: 1px solid var(--gold-dim);
  background: var(--dark-panel);
  color: var(--gold);
  font-family: 'Share Tech Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.1em;
  border-radius: 2px;
  transition: all 0.3s ease;
}
.badge:hover {
  border-color: var(--gold);
  background: var(--mid-brown);
  box-shadow: 0 0 12px rgba(201,168,76,0.3);
}

/* ── Gold divider ───────────────────────────────────────────── */
.divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 40px 0 32px;
}
.divider-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold-dim), var(--gold), var(--gold-dim), transparent);
}
.divider-rune {
  color: var(--gold);
  font-size: 16px;
  flex-shrink: 0;
  animation: goldPulse 3s ease-in-out infinite;
}

/* ── NPC Quote panel ────────────────────────────────────────── */
.npc-panel {
  border: 1px solid var(--gold-dim);
  border-left: 3px solid var(--gold);
  background: linear-gradient(135deg, var(--dark-panel) 0%, var(--dark-card) 100%);
  padding: 24px 28px;
  margin: 24px 0;
  position: relative;
  animation: borderGlow 4s ease-in-out infinite;
}
.npc-panel::before {
  content: '';
  position: absolute;
  top: -1px; left: -1px; right: -1px; bottom: -1px;
  background: linear-gradient(135deg, rgba(201,168,76,0.05), transparent);
  pointer-events: none;
}
.npc-name {
  font-family: 'Cinzel', serif;
  font-size: 11px;
  letter-spacing: 0.3em;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 8px;
}
.npc-text {
  font-family: 'IM Fell English', serif;
  font-style: italic;
  font-size: 15px;
  color: var(--parchment);
  line-height: 1.7;
}

/* ── Section headings ───────────────────────────────────────── */
.section {
  margin: 48px 0 24px;
  animation: fadeUp 0.8s ease both;
}

.section-title {
  font-family: 'Cinzel Decorative', serif;
  font-size: 18px;
  font-weight: 700;
  color: var(--gold-bright);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 6px;
}
.section-title .rune-icon { color: var(--amber); font-size: 20px; }

.section-underline {
  height: 1px;
  background: linear-gradient(90deg, var(--gold) 0%, var(--gold-dim) 40%, transparent 100%);
  margin-bottom: 20px;
}

.sub-title {
  font-family: 'Cinzel', serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--amber);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin: 24px 0 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ── Body text ──────────────────────────────────────────────── */
p {
  color: var(--off-white);
  margin-bottom: 12px;
  line-height: 1.8;
}

/* ── Feature cards ──────────────────────────────────────────── */
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  margin: 20px 0;
}

.feature-card {
  background: var(--dark-card);
  border: 1px solid var(--gold-deep);
  border-top: 2px solid var(--gold-dim);
  padding: 22px 22px 18px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}
.feature-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  opacity: 0;
  transition: opacity 0.3s;
}
.feature-card:hover {
  border-color: var(--gold-dim);
  background: var(--mid-brown);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.5), 0 0 16px rgba(201,168,76,0.1);
}
.feature-card:hover::after { opacity: 1; }

.feature-icon {
  font-size: 28px;
  margin-bottom: 10px;
  display: block;
}
.feature-card-title {
  font-family: 'Cinzel', serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--gold);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 10px;
}
.feature-card ul {
  list-style: none;
  padding: 0;
}
.feature-card li {
  font-size: 13px;
  color: var(--off-white);
  padding: 3px 0 3px 16px;
  position: relative;
  line-height: 1.5;
}
.feature-card li::before {
  content: '✦';
  position: absolute;
  left: 0;
  color: var(--gold-dim);
  font-size: 9px;
  top: 5px;
}

/* ── Code blocks ────────────────────────────────────────────── */
pre, code {
  font-family: 'Share Tech Mono', monospace;
}

pre {
  background: #080602;
  border: 1px solid var(--gold-deep);
  border-left: 3px solid var(--gold-dim);
  padding: 18px 20px;
  overflow-x: auto;
  color: var(--gold);
  font-size: 12px;
  line-height: 1.6;
  margin: 12px 0;
  position: relative;
}
pre::before {
  content: attr(data-label);
  position: absolute;
  top: -1px; right: 12px;
  background: var(--gold-dim);
  color: var(--dark-bg);
  font-size: 9px;
  letter-spacing: 0.15em;
  padding: 2px 8px;
  font-family: 'Cinzel', serif;
  font-weight: 700;
  text-transform: uppercase;
}

code {
  background: rgba(201,168,76,0.1);
  border: 1px solid var(--gold-deep);
  color: var(--amber);
  padding: 1px 6px;
  font-size: 12px;
  border-radius: 2px;
}

/* ── Tables ─────────────────────────────────────────────────── */
.table-wrap { overflow-x: auto; margin: 16px 0; }

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
thead tr {
  background: var(--mid-brown);
}
thead th {
  font-family: 'Cinzel', serif;
  font-size: 11px;
  font-weight: 700;
  color: var(--gold);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  padding: 10px 14px;
  border-bottom: 1px solid var(--gold-dim);
  text-align: left;
}
tbody tr {
  border-bottom: 1px solid rgba(201,168,76,0.08);
  transition: background 0.2s;
}
tbody tr:nth-child(even) { background: rgba(26,18,8,0.6); }
tbody tr:hover { background: var(--mid-brown); }
td {
  padding: 9px 14px;
  color: var(--off-white);
  vertical-align: top;
}
td:first-child {
  color: var(--amber);
  font-family: 'Cinzel', serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.1em;
  white-space: nowrap;
}

/* ── PDF section table ──────────────────────────────────────── */
.pdf-table td:first-child { color: var(--gold); }

/* ── Step cards ─────────────────────────────────────────────── */
.steps { display: flex; flex-direction: column; gap: 16px; margin: 20px 0; }

.step {
  display: grid;
  grid-template-columns: 48px 1fr;
  gap: 0;
  background: var(--dark-card);
  border: 1px solid var(--gold-deep);
  overflow: hidden;
  transition: all 0.3s ease;
}
.step:hover {
  border-color: var(--gold-dim);
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}
.step-num {
  background: var(--mid-brown);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Cinzel Decorative', serif;
  font-size: 18px;
  font-weight: 700;
  color: var(--gold);
  border-right: 1px solid var(--gold-deep);
  min-height: 60px;
}
.step-body { padding: 16px 20px; }
.step-title {
  font-family: 'Cinzel', serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--amber);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.step p { margin: 0; font-size: 13px; color: var(--off-white); }

/* ── Terminal demo ──────────────────────────────────────────── */
.terminal {
  background: #040302;
  border: 1px solid var(--gold-deep);
  border-radius: 4px;
  overflow: hidden;
  margin: 16px 0;
  box-shadow: 0 8px 32px rgba(0,0,0,0.6);
}
.terminal-bar {
  background: var(--mid-brown);
  padding: 8px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px solid var(--gold-deep);
}
.term-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
}
.term-dot.r { background: #FF5F57; }
.term-dot.y { background: #FFBD2E; }
.term-dot.g { background: #28CA41; }
.term-title {
  font-family: 'Share Tech Mono', monospace;
  font-size: 10px;
  color: var(--grey);
  margin-left: 8px;
  letter-spacing: 0.1em;
}
.terminal pre {
  border: none;
  border-left: none;
  margin: 0;
  padding: 18px 20px;
  background: transparent;
  font-size: 11.5px;
}
.terminal pre::before { display: none; }
.t-gold  { color: var(--gold); }
.t-green { color: #6BCB77; }
.t-blue  { color: #64B5F6; }
.t-red   { color: #E57373; }
.t-grey  { color: #666; }
.t-amber { color: var(--amber); }
.t-white { color: var(--off-white); }

/* ── TOC ────────────────────────────────────────────────────── */
.toc {
  background: var(--dark-card);
  border: 1px solid var(--gold-deep);
  border-top: 2px solid var(--gold-dim);
  padding: 24px 28px;
  margin: 24px 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 4px 24px;
}
.toc a {
  font-family: 'Cinzel', serif;
  font-size: 11px;
  color: var(--gold-dim);
  text-decoration: none;
  letter-spacing: 0.1em;
  padding: 5px 0;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: color 0.2s;
  border-bottom: 1px solid transparent;
}
.toc a::before { content: '✦'; font-size: 8px; color: var(--gold-deep); transition: color 0.2s; }
.toc a:hover { color: var(--gold); }
.toc a:hover::before { color: var(--gold); }

/* ── File tree ──────────────────────────────────────────────── */
.file-tree {
  background: #040302;
  border: 1px solid var(--gold-deep);
  border-left: 3px solid var(--gold-dim);
  padding: 20px 24px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 12.5px;
  line-height: 2;
}
.ft-dir  { color: var(--gold); }
.ft-file { color: var(--off-white); }
.ft-desc { color: var(--grey); font-size: 11px; }
.ft-icon { margin-right: 6px; }

/* ── Inline list ────────────────────────────────────────────── */
ul.rune-list {
  list-style: none;
  padding: 0;
  margin: 10px 0;
}
ul.rune-list li {
  padding: 5px 0 5px 20px;
  position: relative;
  font-size: 14px;
  color: var(--off-white);
}
ul.rune-list li::before {
  content: '⚜';
  position: absolute;
  left: 0;
  color: var(--gold-dim);
  font-size: 11px;
  top: 7px;
}

/* ── Troubleshooting cards ──────────────────────────────────── */
.trouble-card {
  background: var(--dark-card);
  border: 1px solid var(--crimson-dim);
  border-left: 3px solid var(--crimson);
  padding: 18px 20px;
  margin: 14px 0;
}
.trouble-title {
  font-family: 'Cinzel', serif;
  font-size: 12px;
  font-weight: 700;
  color: #E57373;
  letter-spacing: 0.15em;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ── Credits box ────────────────────────────────────────────── */
.credits {
  border: 1px solid var(--gold-dim);
  background: linear-gradient(135deg, var(--dark-panel), var(--dark-card));
  padding: 32px;
  text-align: center;
  position: relative;
  margin: 40px 0;
  animation: borderGlow 5s ease-in-out infinite;
}
.credits::before, .credits::after {
  content: '⚜';
  position: absolute;
  color: var(--gold);
  font-size: 20px;
  opacity: 0.5;
}
.credits::before { top: 12px; left: 16px; }
.credits::after  { bottom: 12px; right: 16px; }
.credits-title {
  font-family: 'Cinzel Decorative', serif;
  font-size: 20px;
  color: var(--gold-bright);
  margin-bottom: 8px;
  animation: goldPulse 3s ease-in-out infinite;
}
.credits-sub {
  font-family: 'IM Fell English', serif;
  font-style: italic;
  font-size: 13px;
  color: var(--grey);
  margin-bottom: 24px;
}
.credits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  margin: 20px 0;
  text-align: left;
}
.credit-item {
  background: rgba(0,0,0,0.3);
  border: 1px solid var(--gold-deep);
  padding: 10px 14px;
  font-size: 12px;
}
.credit-label {
  font-family: 'Cinzel', serif;
  font-size: 10px;
  color: var(--gold-dim);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.credit-val { color: var(--off-white); }

/* ── Footer ─────────────────────────────────────────────────── */
.footer {
  text-align: center;
  padding: 40px 0 20px;
  border-top: 1px solid var(--gold-deep);
}
.footer-quote {
  font-family: 'IM Fell English', serif;
  font-style: italic;
  font-size: 16px;
  color: var(--gold);
  animation: goldPulse 4s ease-in-out infinite;
  margin-bottom: 8px;
}
.footer-sub {
  font-family: 'Cinzel', serif;
  font-size: 10px;
  letter-spacing: 0.2em;
  color: var(--grey);
  text-transform: uppercase;
}

/* ── Note callout ───────────────────────────────────────────── */
.note {
  background: rgba(201,168,76,0.05);
  border: 1px solid var(--gold-deep);
  border-left: 3px solid var(--amber);
  padding: 12px 16px;
  margin: 12px 0;
  font-size: 13px;
  color: var(--parchment);
}
.note strong { color: var(--amber); font-family: 'Cinzel', serif; font-size: 11px; letter-spacing: 0.1em; }

/* ── Responsive ─────────────────────────────────────────────── */
@media (max-width: 600px) {
  .logo-ascii { font-size: 4.5px; }
  .feature-grid { grid-template-columns: 1fr; }
  .step { grid-template-columns: 40px 1fr; }
  .credits-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<div class="page">

  <!-- ── HERO ───────────────────────────────────────────────── -->
  <header class="hero">
    <span class="rune-bg r1">ᚱ</span>
    <span class="rune-bg r2">ᚢ</span>
    <span class="rune-bg r3">ᛟ</span>
    <span class="rune-bg r4">ᚾ</span>

    <pre class="logo-ascii" style="background:transparent;border:none;padding:0;margin:0 auto;display:inline-block;border-left:none;">
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║                                                                          ║
  ║  ███████╗██╗     ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗███╗   ██╗ ██████╗  ║
  ║  ██╔════╝██║    ██╔══██╗██╔════╝████╗  ██║    ██╔══██╗██║████╗  ██║██╔════╝  ║
  ║  █████╗  ██║    ██║  ██║█████╗  ██╔██╗ ██║    ██████╔╝██║██╔██╗ ██║██║  ███╗ ║
  ║  ██╔══╝  ██║    ██║  ██║██╔══╝  ██║╚██╗██║    ██╔══██╗██║██║╚██╗██║██║   ██║ ║
  ║  ███████╗███████╗██████╔╝███████╗██║ ╚████║    ██║  ██║██║██║ ╚████║╚██████╔╝ ║
  ║  ╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ║
  ║                                                                          ║
  ║              ⚜ ─── B U I L D   G U I D E   G E N E R A T O R ─── ⚜              ║
  ║                                                                          ║
  ╚══════════════════════════════════════════════════════════════════════════╝</pre>

    <div class="hero-subtitle">deepseek-r1:8b &nbsp;·&nbsp; Ollama &nbsp;·&nbsp; Python 3.10 &nbsp;·&nbsp; ReportLab &nbsp;·&nbsp; Rich CLI</div>
    <div class="hero-tagline">"Arise now, ye Tarnished. Ye dead, who yet live. The call of long-lost grace speaks to us all…"</div>

    <div class="badge-row">
      <span class="badge">🐍 Python 3.10+</span>
      <span class="badge">🤖 deepseek-r1:8b</span>
      <span class="badge">⚡ Ollama Local</span>
      <span class="badge">📜 ReportLab PDF</span>
      <span class="badge">✨ Rich Terminal</span>
      <span class="badge">🖥 Linux · Win · macOS</span>
    </div>
  </header>

  <!-- ── NPC OVERVIEW ────────────────────────────────────────── -->
  <div class="npc-panel" style="animation-delay:0.3s">
    <div class="npc-name">⚜ Finger Reader Enia</div>
    <div class="npc-text">
      "This tool channels the grace of <strong style="color:var(--gold)">deepseek-r1:8b</strong> through Ollama to generate complete character builds.
      Speak your class, your stats, your vision — and receive your legend inscribed upon
      a beautifully forged <strong style="color:var(--gold)">PDF scroll</strong>. No internet required. All runs locally, in the Lands Between your RAM."
    </div>
  </div>

  <!-- ── TABLE OF CONTENTS ───────────────────────────────────── -->
  <div class="divider"><div class="divider-line"></div><span class="divider-rune">⚜</span><div class="divider-line"></div></div>
  <div class="toc">
    <a href="#overview">Overview</a>
    <a href="#features">Features</a>
    <a href="#structure">File Structure</a>
    <a href="#requirements">Requirements</a>
    <a href="#setup">Installation & Setup</a>
    <a href="#run">How to Run</a>
    <a href="#walkthrough">Usage Walkthrough</a>
    <a href="#pdf">PDF Output</a>
    <a href="#sysdetect">System Detection</a>
    <a href="#config">Configuration</a>
    <a href="#troubleshoot">Troubleshooting</a>
    <a href="#credits">Credits</a>
  </div>

  <!-- ── OVERVIEW ───────────────────────────────────────────── -->
  <div class="section" id="overview">
    <div class="section-title"><span class="rune-icon">⚔</span> Overview</div>
    <div class="section-underline"></div>
    <p>
      <strong style="color:var(--gold)">Cypher Elden Ring Build Guide</strong> is a fully interactive CLI application that guides Tarnished players through creating the perfect build — powered entirely by a local AI model running on your own machine.
    </p>
    <ul class="rune-list">
      <li>Guides you through selecting your class, entering current stats, and describing your desired playstyle</li>
      <li>Sends your build vision to <code>deepseek-r1:8b</code> running locally via Ollama</li>
      <li>Parses the AI response into a structured build: weapons, armor, talismans, great runes, and stat paths</li>
      <li>Generates a polished dark-themed PDF — <code>elden_ring_build.pdf</code> — ready to reference while playing</li>
    </ul>
    <div class="note"><strong>Privacy Note —</strong> No internet required after setup. Everything runs 100% locally on your machine. Your build secrets stay in the Lands Between.</div>
  </div>

  <!-- ── FEATURES ───────────────────────────────────────────── -->
  <div class="section" id="features">
    <div class="section-title"><span class="rune-icon">✨</span> Features</div>
    <div class="section-underline"></div>

    <div class="feature-grid">
      <div class="feature-card">
        <span class="feature-icon">🗡</span>
        <div class="feature-card-title">Immersive CLI Experience</div>
        <ul>
          <li>Full Elden Ring-themed dialogues — Melina, Enia, Roderika guide you</li>
          <li>Rich terminal UI with golden palette, Unicode symbols, ornate panels</li>
          <li>Animated spinners & progress bars styled to the lore</li>
          <li>Graceful CTRL+C with thematic farewell messages</li>
          <li><em style="color:var(--grey)">"The flame fades… your session ends."</em></li>
        </ul>
      </div>

      <div class="feature-card">
        <span class="feature-icon">🛡</span>
        <div class="feature-card-title">Smart Input & Validation</div>
        <ul>
          <li>Class selection menu — numbered or named, all 10 classes</li>
          <li>Per-stat NPC prompts for each attribute (Vigor, Mind, Endurance…)</li>
          <li>Build prompt up to 5,000 characters of freeform description</li>
          <li>Real-time character count feedback and auto-trim</li>
          <li>Full confirmation summary — restart anytime</li>
        </ul>
      </div>

      <div class="feature-card">
        <span class="feature-icon">🧠</span>
        <div class="feature-card-title">AI-Powered Build Generation</div>
        <ul>
          <li>Uses <code>deepseek-r1:8b</code> exclusively via Ollama local API</li>
          <li>Streaming output — tokens arrive in real time</li>
          <li>Strips <code>&lt;think&gt;</code> chain-of-thought blocks automatically</li>
          <li>Structured JSON enforcement via system prompt</li>
          <li>3-layer fallback parsing — never fails silently</li>
        </ul>
      </div>

      <div class="feature-card">
        <span class="feature-icon">📜</span>
        <div class="feature-card-title">Professional PDF Output</div>
        <ul>
          <li>Cover page with build name, class, model info, gold border</li>
          <li>Stat table: current → target, priority, reason</li>
          <li>3 weapons · 3 armors · 8 talismans · 2 great runes</li>
          <li>Dark parchment aesthetic with gold borders on every page</li>
          <li>Color-coded pros/cons/locations throughout</li>
        </ul>
      </div>

      <div class="feature-card">
        <span class="feature-icon">⚙</span>
        <div class="feature-card-title">Auto System Setup</div>
        <ul>
          <li>Detects OS, CPU cores, NVIDIA GPU via <code>nvidia-smi</code></li>
          <li>CUDA detection via PyTorch if installed</li>
          <li>Automatically starts Ollama if not running</li>
          <li>Checks & pulls <code>deepseek-r1:8b</code> if missing</li>
          <li>Supports Conda, venv, and pip install paths</li>
        </ul>
      </div>

      <div class="feature-card">
        <span class="feature-icon">🔒</span>
        <div class="feature-card-title">100% Local & Private</div>
        <ul>
          <li>Zero external API calls after initial setup</li>
          <li>No data sent to OpenAI, Anthropic, or any cloud</li>
          <li>Works fully offline in your Lands Between</li>
          <li>GPU accelerated with CUDA if available</li>
          <li>CPU fallback always available</li>
        </ul>
      </div>
    </div>

    <div class="sub-title">📜 PDF Sections at a Glance</div>
    <div class="table-wrap">
      <table class="pdf-table">
        <thead><tr><th>Section</th><th>Contents</th></tr></thead>
        <tbody>
          <tr><td>Cover Page</td><td>Build name, class, primary stats, model info, gold border frame</td></tr>
          <tr><td>Stat Recommendations</td><td>All 8 stats — current → target, priority (High/Med/Low), reason per stat</td></tr>
          <tr><td>Rune Allocation</td><td>Strategic guidance for spending runes across the build arc</td></tr>
          <tr><td>Weapons ×3</td><td>Name, type, scaling, requirements, Ash of War, pros, cons, exact location</td></tr>
          <tr><td>Armor Sets ×3</td><td>Name, type, poise, weight, pros, cons, exact location</td></tr>
          <tr><td>Talismans ×8</td><td>One-line effect, pros, cons, exact location per talisman</td></tr>
          <tr><td>Great Runes ×2</td><td>Demigod holder, effect, activation & acquisition location</td></tr>
          <tr><td>Gameplay Tips</td><td>3 strategic tips crafted for your specific build playstyle</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── FILE STRUCTURE ─────────────────────────────────────── -->
  <div class="section" id="structure">
    <div class="section-title"><span class="rune-icon">🗂</span> File Structure</div>
    <div class="section-underline"></div>
    <div class="file-tree">
<span class="ft-dir">cypher-eldenring-build-guide/</span>
│
├── <span class="ft-file">run.py</span>               <span class="ft-icon">⚔</span> <span class="ft-desc">Main entry point — orchestrates the full pipeline</span>
├── <span class="ft-file">setup.py</span>             <span class="ft-icon">⚙</span> <span class="ft-desc">Environment setup, package install, model pull</span>
├── <span class="ft-file">systemdetection.py</span>  <span class="ft-icon">🔍</span> <span class="ft-desc">OS, GPU, CUDA, Ollama detection</span>
├── <span class="ft-file">cli.py</span>               <span class="ft-icon">✨</span> <span class="ft-desc">Rich CLI — colors, panels, NPC dialogues, spinners</span>
├── <span class="ft-file">input.py</span>             <span class="ft-icon">📋</span> <span class="ft-desc">User input — class, stats, build prompt, validation</span>
├── <span class="ft-file">prompt_processing.py</span> <span class="ft-icon">🧠</span> <span class="ft-desc">Ollama API calls, JSON parsing, validation</span>
├── <span class="ft-file">output_pdf.py</span>        <span class="ft-icon">📜</span> <span class="ft-desc">ReportLab PDF generation with full dark formatting</span>
└── <span class="ft-file">requirements.txt</span>     <span class="ft-icon">📦</span> <span class="ft-desc">Python dependencies</span>
    </div>
  </div>

  <!-- ── REQUIREMENTS ───────────────────────────────────────── -->
  <div class="section" id="requirements">
    <div class="section-title"><span class="rune-icon">⚗</span> Requirements</div>
    <div class="section-underline"></div>

    <div class="sub-title">System Requirements</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Requirement</th><th>Minimum</th><th>Recommended</th></tr></thead>
        <tbody>
          <tr><td>OS</td><td>Linux / Windows 10 / macOS 12</td><td>Ubuntu 22.04 LTS</td></tr>
          <tr><td>Python</td><td>3.10</td><td>3.10 – 3.12</td></tr>
          <tr><td>RAM</td><td>8 GB</td><td>16 GB</td></tr>
          <tr><td>Storage</td><td>6 GB free</td><td>10 GB free</td></tr>
          <tr><td>GPU</td><td>Optional (CPU works)</td><td>NVIDIA 8 GB+ VRAM</td></tr>
          <tr><td>Ollama</td><td>0.1.30+</td><td>Latest</td></tr>
        </tbody>
      </table>
    </div>

    <div class="sub-title">Python Packages</div>
    <pre data-label="requirements.txt">rich          ≥ 13.0.0    <span class="t-grey"># Terminal UI, colors, panels, progress bars</span>
requests      ≥ 2.28.0    <span class="t-grey"># Ollama REST API communication</span>
reportlab     ≥ 4.0.0     <span class="t-grey"># PDF generation</span>
psutil        ≥ 5.9.0     <span class="t-grey"># CPU/memory system detection</span></pre>

    <div class="sub-title">External Tools</div>
    <pre data-label="External">ollama          <span class="t-grey"># Local LLM runtime — https://ollama.com</span>
deepseek-r1:8b  <span class="t-grey"># The AI model (~4.9 GB download via Ollama)</span></pre>

    <div class="note">
      <strong>GPU Note —</strong> With a compatible NVIDIA GPU (8 GB+ VRAM), <code>deepseek-r1:8b</code> generates builds in ~30–60 seconds. CPU-only mode takes ~3–8 minutes. The tool detects CUDA automatically.
    </div>
  </div>

  <!-- ── SETUP ──────────────────────────────────────────────── -->
  <div class="section" id="setup">
    <div class="section-title"><span class="rune-icon">⚙</span> Installation &amp; Setup</div>
    <div class="section-underline"></div>

    <div class="steps">
      <div class="step">
        <div class="step-num">Ⅰ</div>
        <div class="step-body">
          <div class="step-title">Install Ollama</div>
          <pre data-label="Bash"><span class="t-grey"># Linux / macOS</span>
<span class="t-gold">curl -fsSL https://ollama.com/install.sh | sh</span>

<span class="t-grey"># Windows — download installer from:</span>
<span class="t-blue">https://ollama.com/download/windows</span></pre>
        </div>
      </div>

      <div class="step">
        <div class="step-num">Ⅱ</div>
        <div class="step-body">
          <div class="step-title">Start Ollama Server</div>
          <pre data-label="Bash"><span class="t-gold">ollama serve</span></pre>
          <p style="font-size:12px;color:var(--grey);margin-top:6px">Leave this running in a terminal, or configure it as a background service.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">Ⅲ</div>
        <div class="step-body">
          <div class="step-title">Clone the Repository</div>
          <pre data-label="Bash"><span class="t-gold">git clone https://github.com/yourusername/cypher-eldenring-build-guide.git</span>
<span class="t-gold">cd cypher-eldenring-build-guide</span></pre>
        </div>
      </div>

      <div class="step">
        <div class="step-num">Ⅳ</div>
        <div class="step-body">
          <div class="step-title">Run the Setup Wizard</div>
          <pre data-label="Bash"><span class="t-gold">python3 setup.py</span></pre>

          <div class="terminal" style="margin-top:12px">
            <div class="terminal-bar">
              <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
              <span class="term-title">setup.py — cypher-eldenring</span>
            </div>
            <pre>
  <span class="t-gold">╔══════════════════════════════════════════════╗
  ║   CYPHER ELDEN RING BUILD GUIDE — SETUP       ║
  ╚══════════════════════════════════════════════╝</span>

  <span class="t-amber">⚙ Detecting system...</span>
  <span class="t-blue">➤ OS: Linux 6.8.0 (x86_64)</span>
  <span class="t-blue">➤ Python: 3.10.14</span>
  <span class="t-green">✓ GPU detected: NVIDIA GeForce RTX 3070</span>
  <span class="t-green">✓ CUDA: Available</span>

  <span class="t-amber">⚙ Choose installation method:</span>
    <span class="t-gold">1)</span> <span class="t-white">Conda  — create 'cypher-eldenring' conda environment</span>
    <span class="t-gold">2)</span> <span class="t-white">venv   — create local .venv virtual environment</span>
    <span class="t-gold">3)</span> <span class="t-white">pip    — install into current Python environment</span>

  <span class="t-gold">Enter choice [1/2/3]:</span> <span class="t-amber">1</span>

  <span class="t-green">✓ Conda environment 'cypher-eldenring' created.</span>
  <span class="t-green">✓ rich installed.</span>
  <span class="t-green">✓ requests installed.</span>
  <span class="t-green">✓ reportlab installed.</span>
  <span class="t-green">✓ psutil installed.</span>

  <span class="t-amber">⚙ Checking for model: deepseek-r1:8b...</span>
  <span class="t-blue">➤ Pulling deepseek-r1:8b (~4.9 GB, please wait)...</span>
  <span class="t-green">✓ Model deepseek-r1:8b pulled successfully.</span>

  <span class="t-gold">══════════════════════════════════════</span>
  <span class="t-green">  SETUP COMPLETE! ✦</span>
  <span class="t-gold">══════════════════════════════════════</span>
  <span class="t-amber">  Run: python3 run.py</span></pre>
          </div>
        </div>
      </div>
    </div>

    <div class="sub-title">Manual Install (Alternative)</div>
    <pre data-label="Bash"><span class="t-grey"># Install packages manually</span>
<span class="t-gold">pip install rich requests reportlab psutil</span>
<span class="t-grey"># or</span>
<span class="t-gold">pip install -r requirements.txt</span>

<span class="t-grey"># Pull the model manually</span>
<span class="t-gold">ollama pull deepseek-r1:8b</span></pre>
  </div>

  <!-- ── HOW TO RUN ─────────────────────────────────────────── -->
  <div class="section" id="run">
    <div class="section-title"><span class="rune-icon">▶</span> How to Run</div>
    <div class="section-underline"></div>

    <pre data-label="Bash"><span class="t-gold">python3 run.py</span></pre>

    <div class="sub-title">With Conda Environment</div>
    <pre data-label="Bash"><span class="t-gold">conda activate cypher-eldenring</span>
<span class="t-gold">python3 run.py</span></pre>

    <div class="sub-title">With venv</div>
    <pre data-label="Bash"><span class="t-grey"># Linux / macOS</span>
<span class="t-gold">source .venv/bin/activate</span>
<span class="t-gold">python3 run.py</span>

<span class="t-grey"># Windows</span>
<span class="t-gold">.venv\Scripts\activate</span>
<span class="t-gold">python3 run.py</span></pre>
  </div>

  <!-- ── WALKTHROUGH ────────────────────────────────────────── -->
  <div class="section" id="walkthrough">
    <div class="section-title"><span class="rune-icon">📖</span> Usage Walkthrough</div>
    <div class="section-underline"></div>

    <!-- Step 1: Welcome -->
    <div class="sub-title">1 · Welcome Screen</div>
    <div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">run.py — elden ring build guide</span>
      </div>
      <pre>
  <span class="t-gold">███████╗██╗     ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗███╗   ██╗ ██████╗
  ██╔════╝██║    ██╔══██╗██╔════╝████╗  ██║    ██╔══██╗██║████╗  ██║██╔════╝
  █████╗  ██║    ██║  ██║█████╗  ██╔██╗ ██║    ██████╔╝██║██╔██╗ ██║██║  ███╗
  ██╔══╝  ██║    ██║  ██║██╔══╝  ██║╚██╗██║    ██╔══██╗██║██║╚██╗██║██║   ██║
  ███████╗███████╗██████╔╝███████╗██║ ╚████║    ██║  ██║██║██║ ╚████║╚██████╔╝
  ╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝</span>

         <span class="t-amber">⚜⚜⚜  BUILD GUIDE GENERATOR  ⚜⚜⚜</span>
      <span class="t-grey">Powered by deepseek-r1:8b · Ollama</span>

  <span class="t-gold">╔══════════════════════════════════════════════════════╗
  ║  Melina                                               ║
  ║  "Ah, a Tarnished... you've awakened at last."        ║
  ╚══════════════════════════════════════════════════════╝</span></pre>
    </div>

    <!-- Step 2: Class -->
    <div class="sub-title">2 · Class Selection</div>
    <div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Starting Class</span>
      </div>
      <pre>
  <span class="t-gold">┌─── ⚔ Choose Your Starting Class ⚔ ──────────────────────────────────────┐
  │  #  │  Class       │  Description                                          │
  │─────│──────────────│───────────────────────────────────────────────────────│
  │  1  │  Vagabond    │  A knight in exile. Melee-focused, high vigor.         │
  │  2  │  Warrior     │  Dual wielder. Dex-oriented, light and fast.           │
  │  3  │  Hero        │  Mighty warrior. Strength-focused brute.               │
  │  4  │  Bandit      │  Cunning outlaw. Dex + Arcane synergy.                 │
  │  5  │  Astrologer  │  Scholar of stars. Intelligence sorcerer.              │
  │  6  │  Prophet     │  Outcast prophet. Faith incantation user.              │
  │  7  │  Samurai     │  Far Eastern warrior. Balanced Dex build.              │
  │  8  │  Prisoner    │  Jailed mage-warrior. Int/Dex hybrid.                  │
  │  9  │  Confessor   │  Church spy. Faith + Strength blend.                   │
  │  10 │  Wretch      │  Pitiful start. All stats equal — pure chaos.          │
  └───────────────────────────────────────────────────────────────────────────┘</span>

  <span class="t-amber">✦ Enter class name or number:</span> <span class="t-white">3</span>
  <span class="t-gold">✦ Class selected: Hero</span></pre>
    </div>

    <!-- Step 3: Stats -->
    <div class="sub-title">3 · Stat Entry</div>
    <div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Current Attributes</span>
      </div>
      <pre>
  <span class="t-gold">╔══════════════════════════════════════════════════════╗
  ║  Enia                                                  ║
  ║  "Speak your attributes, Tarnished. The Two Fingers    ║
  ║   must know your foundation."                          ║
  ╚══════════════════════════════════════════════════════╝</span>

  <span class="t-amber">✦</span> <span class="t-gold">Vigor</span>        <span class="t-grey">(1–99) — How much HP do you carry, Tarnished?</span>  <span class="t-white">25</span>
  <span class="t-amber">✦</span> <span class="t-gold">Mind</span>         <span class="t-grey">(1–99) — What is the depth of your Focus?</span>        <span class="t-white">15</span>
  <span class="t-amber">✦</span> <span class="t-gold">Endurance</span>    <span class="t-grey">(1–99) — How much can your body endure?</span>          <span class="t-white">20</span>
  <span class="t-amber">✦</span> <span class="t-gold">Strength</span>     <span class="t-grey">(1–99) — What is the might of your arm?</span>          <span class="t-white">16</span>
  <span class="t-amber">✦</span> <span class="t-gold">Dexterity</span>    <span class="t-grey">(1–99) — How nimble are your fingers?</span>            <span class="t-white">11</span>
  <span class="t-amber">✦</span> <span class="t-gold">Intelligence</span> <span class="t-grey">(1–99) — How deep is your arcane mind?</span>           <span class="t-white">9</span>
  <span class="t-amber">✦</span> <span class="t-gold">Faith</span>        <span class="t-grey">(1–99) — How strong is your devotion?</span>            <span class="t-white">10</span>
  <span class="t-amber">✦</span> <span class="t-gold">Arcane</span>       <span class="t-grey">(1–99) — What mysteries do you harbour?</span>          <span class="t-white">9</span></pre>
    </div>

    <!-- Step 4: Prompt -->
    <div class="sub-title">4 · Build Vision Prompt</div>
    <div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Build Vision</span>
      </div>
      <pre>
  <span class="t-gold">╔════════════════════════════════════════════════════════════╗
  ║  Roderika                                                    ║
  ║  "What manner of warrior do you seek to become? Describe     ║
  ║   your desired legend — up to 5000 characters."              ║
  ╚════════════════════════════════════════════════════════════╝</span>

  <span class="t-grey">Example: 'A Strength/Faith build using colossal weapons and Sacred Incantations'</span>

  <span class="t-amber">✦ Describe your build vision</span> <span class="t-grey">(press Enter twice when done):</span>

    <span class="t-white">A Strength/Faith hybrid using Godslayer's Greatsword and
    Black Flame incantations. I want high poise to tank through
    enemy attacks and use Sacred buffs to survive endgame content.</span>

  <span class="t-blue">➤ Prompt captured: 178 characters</span></pre>
    </div>

    <!-- Step 5: Generation -->
    <div class="sub-title">5 · Confirmation &amp; Generation</div>
    <div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Generating Build</span>
      </div>
      <pre>
  <span class="t-gold">─── Build Configuration ─────────────────────────────────</span>
  <span class="t-gold">⚔ Class:</span>   <span class="t-white">Hero</span>
  <span class="t-gold">✦ Stats:</span>   <span class="t-white">Vigor 25 · Str 16 · Fai 10 · End 20 · Dex 11</span>
  <span class="t-gold">📜 Prompt:</span> <span class="t-grey">A Strength/Faith hybrid using Godslayer's Greatsword…</span>

  <span class="t-amber">✦ The Two Fingers have received your offering. Shall we proceed?</span> <span class="t-grey">[Y/n]:</span> <span class="t-white">Y</span>

  <span class="t-gold">╔══════════════════════════════════════════════════════════════╗
  ║  Two Fingers                                                   ║
  ║  "The demigods are consulted... your fate is being woven."     ║
  ╚══════════════════════════════════════════════════════════════╝</span>

  <span class="t-gold">⠸</span> <span class="t-amber">The Erdtree channels your destiny...</span>                 <span class="t-grey">[0:00:47]</span></pre>
    </div>

    <!-- Step 6: Done -->
    <div class="sub-title">6 · PDF Delivered</div>
    <div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Complete</span>
      </div>
      <pre>
  <span class="t-gold">★ Build 'Godslayer's Crucible Knight' generated successfully.</span>
  <span class="t-amber">★ Your legend has been inscribed upon the Elden Ring.</span>

  <span class="t-gold">╔══════════════════════════════════════════════════════════════╗
  ║  Melina                                                        ║
  ║  "Your build has been etched into the Elden Ring.              ║
  ║   Open 'elden_ring_build.pdf' to claim your destiny."          ║
  ╚══════════════════════════════════════════════════════════════╝</span>

  <span class="t-amber">Quick Summary:</span>
    <span class="t-gold">Build:   </span><span class="t-white">Godslayer's Crucible Knight</span>
    <span class="t-gold">Class:   </span><span class="t-white">Hero</span>
    <span class="t-gold">Primary: </span><span class="t-white">Strength</span>
    <span class="t-gold">PDF:     </span><span class="t-blue">/home/kecypher/Desktop/cypher-eldenring-build-guide/elden_ring_build.pdf</span></pre>
    </div>
  </div>

  <!-- ── PDF OUTPUT ─────────────────────────────────────────── -->
  <div class="section" id="pdf">
    <div class="section-title"><span class="rune-icon">📜</span> PDF Output</div>
    <div class="section-underline"></div>
    <p>The generated <code>elden_ring_build.pdf</code> is a fully self-contained dark-themed build guide. Every page has a golden double border and corner ornaments.</p>

    <div class="table-wrap">
      <table>
        <thead><tr><th>Design Element</th><th>Details</th></tr></thead>
        <tbody>
          <tr><td>Background</td><td>Deep black <code>#1A1208</code> — like the Lands Between at night</td></tr>
          <tr><td>Borders</td><td>Dual gold borders on every page with <code>✦</code> corner ornaments</td></tr>
          <tr><td>Pros</td><td><span style="color:var(--green-rune)">✓ Green</span> — positive attributes</td></tr>
          <tr><td>Cons</td><td><span style="color:var(--red-rune)">✗ Red</span> — drawbacks and limitations</td></tr>
          <tr><td>Locations</td><td><span style="color:var(--blue-rune)">📍 Light blue</span> — where to find items</td></tr>
          <tr><td>Priority</td><td><span style="color:var(--red-rune)">High</span> · <span style="color:var(--amber)">Medium</span> · <span style="color:var(--green-rune)">Low</span> color coding</td></tr>
          <tr><td>Footer</td><td>Build name · Cypher Elden Ring Build Guide · Page N</td></tr>
          <tr><td>Font</td><td>Helvetica with bold gold headers throughout</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── SYSTEM DETECTION ───────────────────────────────────── -->
  <div class="section" id="sysdetect">
    <div class="section-title"><span class="rune-icon">🔍</span> System Detection</div>
    <div class="section-underline"></div>
    <p><code>systemdetection.py</code> runs automatically on startup and can also be invoked standalone:</p>
    <pre data-label="Bash"><span class="t-gold">python3 systemdetection.py</span></pre>
    <pre data-label="JSON Output">{
  <span class="t-gold">"os"</span>:     { <span class="t-amber">"system"</span>: <span class="t-green">"Linux"</span>, <span class="t-amber">"release"</span>: <span class="t-green">"6.8.0"</span>, <span class="t-amber">"machine"</span>: <span class="t-green">"x86_64"</span> },
  <span class="t-gold">"cpu"</span>:    { <span class="t-amber">"name"</span>: <span class="t-green">"AMD Ryzen 9 5900X"</span>, <span class="t-amber">"logical_cores"</span>: <span class="t-blue">24</span> },
  <span class="t-gold">"cuda"</span>:   { <span class="t-amber">"available"</span>: <span class="t-blue">true</span>, <span class="t-amber">"device_count"</span>: <span class="t-blue">1</span>,
               <span class="t-amber">"devices"</span>: [{ <span class="t-amber">"name"</span>: <span class="t-green">"NVIDIA RTX 3070"</span>, <span class="t-amber">"memory_mb"</span>: <span class="t-green">"8192"</span> }] },
  <span class="t-gold">"ollama"</span>: { <span class="t-amber">"installed"</span>: <span class="t-blue">true</span>, <span class="t-amber">"running"</span>: <span class="t-blue">true</span>,
               <span class="t-amber">"models"</span>: [<span class="t-green">"deepseek-r1:8b"</span>, <span class="t-green">"llama3.2:3b"</span>] },
  <span class="t-gold">"python"</span>: { <span class="t-amber">"version"</span>: <span class="t-green">"3.10.14"</span>, <span class="t-amber">"executable"</span>: <span class="t-green">"/usr/bin/python3"</span> }
}</pre>
  </div>

  <!-- ── CONFIGURATION ──────────────────────────────────────── -->
  <div class="section" id="config">
    <div class="section-title"><span class="rune-icon">🔧</span> Configuration</div>
    <div class="section-underline"></div>

    <div class="sub-title">Change the AI Model</div>
    <p>In <code>prompt_processing.py</code>, line 8:</p>
    <pre data-label="prompt_processing.py">MODEL_NAME = <span class="t-green">"deepseek-r1:8b"</span>   <span class="t-grey"># ← change to any Ollama model</span></pre>
    <pre data-label="Compatible Models"><span class="t-gold">ollama pull</span> <span class="t-white">llama3.1:8b</span>        <span class="t-grey"># Meta Llama 3.1 — fast, capable</span>
<span class="t-gold">ollama pull</span> <span class="t-white">mistral:7b</span>         <span class="t-grey"># Mistral 7B — efficient</span>
<span class="t-gold">ollama pull</span> <span class="t-white">deepseek-r1:14b</span>    <span class="t-grey"># Larger, slower, more accurate</span></pre>

    <div class="sub-title">Change Output Filename</div>
    <p>In <code>output_pdf.py</code>, line 18:</p>
    <pre data-label="output_pdf.py">OUTPUT_FILE = <span class="t-green">"elden_ring_build.pdf"</span>   <span class="t-grey"># ← rename as desired</span></pre>

    <div class="sub-title">Adjust Model Parameters</div>
    <pre data-label="prompt_processing.py"><span class="t-grey"># Inside call_ollama():</span>
<span class="t-gold">"options"</span>: {
    <span class="t-amber">"temperature"</span>: <span class="t-blue">0.3</span>,    <span class="t-grey"># ↑ more creative  ↓ more precise</span>
    <span class="t-amber">"top_p"</span>:        <span class="t-blue">0.9</span>,
    <span class="t-amber">"num_predict"</span>:  <span class="t-blue">4096</span>,   <span class="t-grey"># max tokens in response</span>
}</pre>

    <div class="sub-title">Custom Ollama Host</div>
    <pre data-label="prompt_processing.py"><span class="t-grey"># Default: http://localhost:11434</span>
response = requests.post(<span class="t-green">"http://YOUR_HOST:11434/api/generate"</span>, ...)</pre>
  </div>

  <!-- ── TROUBLESHOOTING ────────────────────────────────────── -->
  <div class="section" id="troubleshoot">
    <div class="section-title"><span class="rune-icon">💀</span> Troubleshooting</div>
    <div class="section-underline"></div>

    <div class="trouble-card">
      <div class="trouble-title">⚠ Cannot connect to Ollama</div>
      <pre data-label="Fix"><span class="t-grey"># Make sure Ollama is running:</span>
<span class="t-gold">ollama serve</span>
<span class="t-grey"># Verify it responds:</span>
<span class="t-gold">curl http://localhost:11434</span></pre>
    </div>

    <div class="trouble-card">
      <div class="trouble-title">⚠ deepseek-r1:8b not found</div>
      <pre data-label="Fix"><span class="t-gold">ollama pull deepseek-r1:8b</span>
<span class="t-grey"># Verify:</span>
<span class="t-gold">ollama list</span></pre>
    </div>

    <div class="trouble-card">
      <div class="trouble-title">⚠ ModuleNotFoundError: No module named 'rich'</div>
      <pre data-label="Fix"><span class="t-gold">pip install rich requests reportlab psutil</span>
<span class="t-grey"># or</span>
<span class="t-gold">pip install -r requirements.txt</span></pre>
    </div>

    <div class="trouble-card">
      <div class="trouble-title">⚠ Generation takes too long</div>
      <p style="font-size:13px;margin:0 0 10px">CPU-only can take 3–8 minutes for <code>deepseek-r1:8b</code>. With CUDA GPU (8 GB+ VRAM), generation drops to ~30–60 seconds.</p>
      <pre data-label="Check GPU"><span class="t-gold">python3 systemdetection.py</span>
<span class="t-grey"># Look for: "cuda": { "available": true }</span></pre>
    </div>

    <div class="trouble-card">
      <div class="trouble-title">⚠ Model returns invalid JSON</div>
      <p style="font-size:13px;margin:0 0 10px">The tool has three layers of JSON recovery: direct parse → markdown fence extraction → outermost <code>{ }</code> scan. If all fail, simplify your build prompt and try again.</p>
    </div>

    <div class="trouble-card" style="border-color:var(--gold-deep);border-left-color:var(--gold-dim)">
      <div class="trouble-title" style="color:var(--gold)">✓ f-string Backslash Error (Fixed)</div>
      <p style="font-size:13px;margin:0;color:var(--grey)">A Python 3.10 compatibility issue with backslashes inside f-strings — <strong style="color:var(--off-white)">already fixed</strong> in the current version. Ensure you have the latest files.</p>
    </div>
  </div>

  <!-- ── CREDITS ────────────────────────────────────────────── -->
  <div class="section" id="credits">
    <div class="section-title"><span class="rune-icon">⚜</span> Credits</div>
    <div class="section-underline"></div>
    <div class="credits">
      <div class="credits-title">⚔ Cypher Elden Ring Build Guide ⚔</div>
      <div class="credits-sub">Built with dark gold and Tarnished determination.</div>
      <div class="divider"><div class="divider-line"></div><span class="divider-rune" style="font-size:12px">✦</span><div class="divider-line"></div></div>
      <div class="credits-grid">
        <div class="credit-item">
          <div class="credit-label">🧠 AI Engine</div>
          <div class="credit-val">deepseek-r1:8b via Ollama</div>
        </div>
        <div class="credit-item">
          <div class="credit-label">✨ CLI Framework</div>
          <div class="credit-val">Rich by Will McGugan</div>
        </div>
        <div class="credit-item">
          <div class="credit-label">📜 PDF Engine</div>
          <div class="credit-val">ReportLab Open Source</div>
        </div>
        <div class="credit-item">
          <div class="credit-label">🎮 Lore & World</div>
          <div class="credit-val">Elden Ring © FromSoftware / Bandai Namco</div>
        </div>
        <div class="credit-item">
          <div class="credit-label">⚡ LLM Runtime</div>
          <div class="credit-val">Ollama — ollama.com</div>
        </div>
        <div class="credit-item">
          <div class="credit-label">📖 Story</div>
          <div class="credit-val">George R.R. Martin × Hidetaka Miyazaki</div>
        </div>
      </div>
      <div class="divider"><div class="divider-line"></div><span class="divider-rune" style="font-size:12px">✦</span><div class="divider-line"></div></div>
      <p style="font-size:11px;color:var(--grey);font-family:'Cinzel',serif;letter-spacing:0.1em">This is a fan project. Not affiliated with FromSoftware, Bandai Namco, or DeepSeek AI.</p>
    </div>
  </div>

  <!-- ── FOOTER ─────────────────────────────────────────────── -->
  <div class="divider"><div class="divider-line"></div><span class="divider-rune">⚜</span><div class="divider-line"></div></div>
  <footer class="footer">
    <div class="footer-quote">
      "May your runes guide thee, and may the grace of gold ever shine upon your path, Tarnished."
    </div>
    <div style="height:12px"></div>
    <div class="footer-sub">Cypher Elden Ring Build Guide &nbsp;·&nbsp; deepseek-r1:8b &nbsp;·&nbsp; Ollama &nbsp;·&nbsp; Python 3.10</div>
    <div style="height:8px"></div>
    <div style="font-family:'IM Fell English',serif;font-style:italic;color:var(--gold-dim);font-size:13px">
      "The Elden Ring is shattered. But your build guide need not be."
    </div>
  </footer>

</div><!-- end .page -->

</body>
</html>
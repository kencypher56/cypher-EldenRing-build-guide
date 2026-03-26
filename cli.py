"""
cli.py - Rich CLI with Elden Ring-themed dialogues, colors, icons, and menus
"""

import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.prompt import Prompt, Confirm
from rich.rule import Rule
from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.style import Style

console = Console()

# ── Elden Ring Color Palette ──────────────────────────────────────────────────
GOLD       = "bold yellow"
AMBER      = "yellow"
CRIMSON    = "bold red"
ASH_WHITE  = "bold white"
GREY       = "dim white"
TEAL       = "bold cyan"
RUNE_GLOW  = "bold bright_yellow"
SHADOW     = "bright_black"

# ── Elden Ring ASCII Art / Symbols ───────────────────────────────────────────
ELDEN_LOGO = r"""
   ███████╗██╗     ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗███╗   ██╗ ██████╗ 
   ██╔════╝██║     ██╔══██╗██╔════╝████╗  ██║    ██╔══██╗██║████╗  ██║██╔════╝ 
   █████╗  ██║     ██║  ██║█████╗  ██╔██╗ ██║    ██████╔╝██║██╔██╗ ██║██║  ███╗
   ██╔══╝  ██║     ██║  ██║██╔══╝  ██║╚██╗██║    ██╔══██╗██║██║╚██╗██║██║   ██║
   ███████╗███████╗██████╔╝███████╗██║ ╚████║    ██║  ██║██║██║ ╚████║╚██████╔╝
   ╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

DIVIDER_RUNE = "⚜"
SWORD        = "⚔"
SHIELD       = "🛡"
RUNE         = "✦"
SKULL        = "💀"
FIRE         = "🔥"
SCROLL       = "📜"
STAR         = "★"
ARROW        = "➤"

# ── Elden Ring Dialogues ─────────────────────────────────────────────────────
GREETINGS = [
    "Ah, a Tarnished... you've awakened at last.",
    "By grace of gold, your path is illuminated.",
    "The Erdtree calls to you, Tarnished. What is your desire?",
    "Welcome, bearer of the fractured grace.",
]

ERRORS = [
    f"{SKULL} Alas... the path ahead is sealed. Heed the warning.",
    f"{FIRE} The flame rejects your input. Try again, Tarnished.",
    f"{SKULL} Invalid entry — even the Mad Tongue Alberich would not make such a mistake.",
    f"{FIRE} The Two Fingers whisper of invalid data. Reconsider.",
]

FAREWELLS = [
    "The flame fades… your session ends. May your runes guide you.",
    "Farewell, Tarnished. The Elden Ring awaits your return.",
    "Grace has faded from this place... until we meet again.",
]

LOADING_MSGS = [
    f"{RUNE} Consulting the Two Fingers...",
    f"{RUNE} Channeling the power of the Erdtree...",
    f"{RUNE} The demigods deliberate your fate...",
    f"{RUNE} Sorcery takes time, Tarnished. Patience...",
    f"{RUNE} Your build is being forged in the crucible...",
]

SUCCESS_MSGS = [
    f"{STAR} Your legend has been inscribed upon the Elden Ring.",
    f"{STAR} Grace shines upon your build, Tarnished.",
    f"{STAR} The build guide has been etched into the golden order.",
]


def clear_screen():
    console.clear()


def print_banner():
    """Print the Elden Ring ASCII banner."""
    console.print(Text(ELDEN_LOGO, style=GOLD, justify="center"))
    console.print(
        Align.center(
            Text(f"{DIVIDER_RUNE * 3}  BUILD GUIDE GENERATOR  {DIVIDER_RUNE * 3}", style=AMBER)
        )
    )
    console.print(
        Align.center(Text("Powered by deepseek-r1:8b · Ollama", style=GREY))
    )
    console.print()


def print_rule(title: str = ""):
    if title:
        console.print(Rule(f"[{AMBER}] {DIVIDER_RUNE} {title} {DIVIDER_RUNE} [/{AMBER}]", style=AMBER))
    else:
        console.print(Rule(style=AMBER))


def print_panel(content: str, title: str = "", style: str = GOLD):
    console.print(
        Panel(
            content,
            title=f"[{style}]{title}[/{style}]" if title else None,
            border_style=AMBER,
            padding=(1, 3),
        )
    )


def print_npc_dialogue(dialogue: str, npc: str = "Finger Reader Enia"):
    """Display a dialogue box styled like an in-game NPC message."""
    text = Text()
    text.append(f"\n  {npc}\n", style=GOLD)
    text.append(f'  “{dialogue}”\n', style=ASH_WHITE)
    console.print(
        Panel(text, border_style=AMBER, padding=(0, 2), box=box.DOUBLE_EDGE)
    )


def print_error(message: str):
    """Display an Elden Ring-styled error message."""
    import random
    prefix = random.choice(ERRORS)
    console.print(f"\n  [{CRIMSON}]{prefix}[/{CRIMSON}]")
    console.print(f"  [{GREY}]↳ {message}[/{GREY}]\n")


def print_success(message: str):
    """Display a success message."""
    import random
    suffix = random.choice(SUCCESS_MSGS)
    console.print(f"\n  [{RUNE_GLOW}]{STAR} {message}[/{RUNE_GLOW}]")
    console.print(f"  [{GOLD}]{suffix}[/{GOLD}]\n")


def print_info(message: str):
    console.print(f"  [{TEAL}]{ARROW} {message}[/{TEAL}]")


def print_greeting():
    """Show a random greeting dialogue."""
    import random
    print_npc_dialogue(random.choice(GREETINGS))
    console.print()


def print_farewell():
    """Show a farewell message on exit."""
    import random
    console.print()
    print_npc_dialogue(random.choice(FAREWELLS), npc="Grace")
    console.print()


def confirm_prompt(question: str, default: bool = True) -> bool:
    """Ask a yes/no confirmation in Elden Ring style."""
    return Confirm.ask(f"  [{GOLD}]{RUNE} {question}[/{GOLD}]", default=default)


def display_class_menu(classes: list[str]) -> str:
    """Show a styled class selection menu and return choice."""
    table = Table(
        title=f"[{GOLD}]{SWORD} Choose Your Starting Class {SWORD}[/{GOLD}]",
        box=box.DOUBLE_EDGE,
        border_style=AMBER,
        header_style=GOLD,
        show_lines=True,
    )
    table.add_column("#", style=GREY, justify="center", width=4)
    table.add_column("Class", style=ASH_WHITE, min_width=16)
    table.add_column("Description", style=GREY, min_width=40)

    class_descs = {
        "Vagabond":   "A knight in exile. Melee-focused, high vigor.",
        "Warrior":    "Dual wielder. Dex-oriented, light and fast.",
        "Hero":       "Mighty warrior. Strength-focused brute.",
        "Bandit":     "Cunning outlaw. Dex + Arcane synergy.",
        "Astrologer": "Scholar of stars. Intelligence sorcerer.",
        "Prophet":    "Outcast prophet. Faith incantation user.",
        "Samurai":    "Far Eastern warrior. Balanced Dex build.",
        "Prisoner":   "Jailed mage-warrior. Int/Dex hybrid.",
        "Confessor":  "Church spy. Faith + Strength blend.",
        "Wretch":     "Pitiful start. All stats equal — pure chaos.",
    }

    for i, cls in enumerate(classes, 1):
        desc = class_descs.get(cls, "A path through the Lands Between.")
        table.add_row(str(i), cls, desc)

    console.print(table)
    console.print()
    return table


def display_stat_summary(stats: dict):
    """Display current stats in a formatted table."""
    table = Table(
        title=f"[{GOLD}]{RUNE} Current Character Stats {RUNE}[/{GOLD}]",
        box=box.SIMPLE_HEAVY,
        border_style=AMBER,
        header_style=GOLD,
        show_lines=False,
        min_width=40,
    )
    table.add_column("Attribute", style=GOLD, min_width=16)
    table.add_column("Value", style=RUNE_GLOW, justify="center", width=8)

    stat_icons = {
        "Vigor":        "❤",
        "Mind":         "💧",
        "Endurance":    "⚡",
        "Strength":     "💪",
        "Dexterity":    "🗡",
        "Intelligence": "✨",
        "Faith":        "☀",
        "Arcane":       "🔮",
    }

    for stat, val in stats.items():
        icon = stat_icons.get(stat, "•")
        table.add_row(f"{icon}  {stat}", str(val))

    console.print(table)
    console.print()


def display_build_summary(class_name: str, stats: dict, prompt: str):
    """Show a full summary before processing."""
    print_rule("Build Configuration")
    console.print(f"  [{GOLD}]{SWORD} Class:[/{GOLD}] [{ASH_WHITE}]{class_name}[/{ASH_WHITE}]")
    console.print()
    display_stat_summary(stats)
    console.print(f"  [{GOLD}]{SCROLL} Build Prompt:[/{GOLD}]")
    console.print(
        Panel(prompt[:300] + ("..." if len(prompt) > 300 else ""),
              border_style=GREY, padding=(0, 2))
    )
    console.print()


def spinner_context(message: str):
    """Return a Rich progress spinner context manager."""
    return Progress(
        SpinnerColumn(style=GOLD),
        TextColumn(f"[{AMBER}]{message}[/{AMBER}]"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    )


def progress_bar(total: int, description: str):
    """Return a progress bar context."""
    return Progress(
        SpinnerColumn(style=GOLD),
        TextColumn(f"[{AMBER}]{description}[/{AMBER}]"),
        BarColumn(bar_width=30, style=AMBER, complete_style=GOLD),
        TextColumn("[{task.percentage:>3.0f}%]", style=GREY),
        TimeElapsedColumn(),
        console=console,
    )


def animate_thinking(seconds: int = 2, message: str = None):
    """Show an animated 'thinking' spinner for a few seconds."""
    import random
    msg = message or random.choice(LOADING_MSGS)
    with Progress(
        SpinnerColumn(spinner_name="aesthetic", style=GOLD),
        TextColumn(f"[{AMBER}]{msg}[/{AMBER}]"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("", total=seconds * 10)
        for _ in range(seconds * 10):
            time.sleep(0.1)
            progress.advance(task)


def print_system_info(info: dict):
    """Display detected system info."""
    table = Table(
        title=f"[{GOLD}]⚙ System Detection[/{GOLD}]",
        box=box.SIMPLE,
        border_style=AMBER,
        show_header=False,
    )
    table.add_column("Key", style=GOLD, min_width=18)
    table.add_column("Value", style=ASH_WHITE)

    os_i = info.get("os", {})
    table.add_row("OS", f"{os_i.get('system','?')} {os_i.get('release','')}")

    cpu_i = info.get("cpu", {})
    table.add_row("CPU", cpu_i.get("name", "Unknown"))
    if cpu_i.get("logical_cores"):
        table.add_row("CPU Cores", str(cpu_i["logical_cores"]))

    cuda_i = info.get("cuda", {})
    if cuda_i.get("available"):
        devices = cuda_i.get("devices", [])
        for d in devices:
            table.add_row("GPU", d.get("name", "Unknown"))
        table.add_row("CUDA", "[bold green]Available ✓[/bold green]")
    else:
        table.add_row("GPU/CUDA", "[dim]Not detected — CPU mode[/dim]")

    ollama_i = info.get("ollama", {})
    status = "[bold green]Running ✓[/bold green]" if ollama_i.get("running") else "[bold red]Not running[/bold red]"
    table.add_row("Ollama", status)
    if ollama_i.get("models"):
        table.add_row("Models", ", ".join(ollama_i["models"][:5]))

    console.print(table)
    console.print()


def handle_keyboard_interrupt():
    """Graceful CTRL+C handler."""
    console.print()
    print_farewell()
    sys.exit(0)
"""
run.py - Main entry point for Cypher Elden Ring Build Guide Generator
"""

import sys
import os
import time

# Ensure current directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        from rich.console import Console
        from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
        console = Console()
    except ImportError:
        print("ERROR: Required packages not installed.")
        print("Please run: python setup.py")
        sys.exit(1)

    # ── Import modules ────────────────────────────────────────────────────────
    try:
        import cli
        import systemdetection as sysdet
        from input import get_all_inputs
        from prompt_processing import generate_build
        from output_pdf import generate_pdf, OUTPUT_FILE
    except ImportError as e:
        console.print(f"[bold red]Import error: {e}[/bold red]")
        console.print("[yellow]Run python setup.py to install dependencies.[/yellow]")
        sys.exit(1)

    # ── Welcome ───────────────────────────────────────────────────────────────
    cli.clear_screen()
    cli.print_banner()
    cli.print_greeting()

    # ── System Detection ──────────────────────────────────────────────────────
    cli.print_rule("System Detection")
    cli.print_info("Detecting system hardware and software...")
    sys_info = sysdet.get_full_system_info()
    cli.print_system_info(sys_info)

    # Check Ollama is running
    ollama_info = sys_info.get("ollama", {})
    if not ollama_info.get("running"):
        cli.print_error(
            "Ollama does not appear to be running.\n"
            "  Start it with: ollama serve\n"
            "  Then in another terminal: ollama pull deepseek-r1:8b"
        )
        if not cli.confirm_prompt("Continue anyway? (Ollama may still respond)", default=False):
            cli.print_farewell()
            sys.exit(0)

    # Check model availability
    model_info = sysdet.detect_model("deepseek-r1:8b")
    if not model_info.get("available"):
        cli.print_error(
            "deepseek-r1:8b model not found in Ollama.\n"
            "  Pull it with: ollama pull deepseek-r1:8b"
        )
        if not cli.confirm_prompt("Attempt to continue anyway?", default=False):
            cli.print_farewell()
            sys.exit(0)
    else:
        cli.print_info("deepseek-r1:8b model detected. The Two Fingers are ready.")

    console.print()

    # ── Collect User Inputs ───────────────────────────────────────────────────
    try:
        user_data = get_all_inputs()
    except KeyboardInterrupt:
        cli.handle_keyboard_interrupt()

    class_name  = user_data["class"]
    stats       = user_data["stats"]
    build_prompt = user_data["prompt"]

    # ── Generate Build ────────────────────────────────────────────────────────
    cli.print_rule("Generating Build")
    cli.print_npc_dialogue(
        "The demigods are consulted... your fate is being woven into the golden order.",
        npc="Two Fingers"
    )
    console.print()

    # Stream tokens to console (optional, shows model thinking)
    token_buffer = []
    thinking_shown = False

    def on_token(token: str):
        nonlocal thinking_shown
        token_buffer.append(token)
        # Suppress <think> chain-of-thought from showing raw
        if not thinking_shown and len(token_buffer) < 5:
            return

    build_data = None
    with Progress(
        SpinnerColumn(style="bold yellow"),
        TextColumn("[yellow]The Erdtree channels your destiny...[/yellow]"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("Generating", total=None)
        try:
            build_data = generate_build(
                class_name=class_name,
                stats=stats,
                build_prompt=build_prompt,
                on_token=on_token,
            )
            progress.update(task, completed=True)
        except RuntimeError as e:
            progress.stop()
            cli.print_error(str(e))
            cli.print_farewell()
            sys.exit(1)
        except ValueError as e:
            progress.stop()
            cli.print_error(f"Build parsing failed: {e}")
            cli.print_farewell()
            sys.exit(1)
        except KeyboardInterrupt:
            progress.stop()
            cli.handle_keyboard_interrupt()

    console.print()
    cli.print_info(f"Build '{build_data.get('build_name', 'Unknown')}' generated successfully.")
    console.print()

    # ── Generate PDF ──────────────────────────────────────────────────────────
    cli.print_rule("Generating PDF")
    cli.print_npc_dialogue(
        "Your legend shall be etched upon parchment... the guide is being forged.",
        npc="Roderika"
    )
    console.print()

    with Progress(
        SpinnerColumn(style="bold yellow"),
        TextColumn("[yellow]Inscribing your build guide into the golden order...[/yellow]"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("PDF", total=None)
        try:
            output_path = generate_pdf(build_data, OUTPUT_FILE)
            progress.update(task, completed=True)
        except Exception as e:
            progress.stop()
            cli.print_error(f"PDF generation failed: {e}")
            import traceback
            console.print(traceback.format_exc())
            cli.print_farewell()
            sys.exit(1)
        except KeyboardInterrupt:
            progress.stop()
            cli.handle_keyboard_interrupt()

    console.print()

    # ── Done ──────────────────────────────────────────────────────────────────
    cli.print_rule("Complete")
    abs_path = os.path.abspath(output_path)
    cli.print_success(f"Build guide saved: {abs_path}")

    _build_name = build_data.get("build_name", "Tarnished's Path")
    cli.print_npc_dialogue(
        f"Your build, '{_build_name}', "
        f"has been etched into the Elden Ring. "
        f"Open '{OUTPUT_FILE}' to claim your destiny.",
        npc="Melina"
    )
    console.print()

    # Show quick summary
    console.print(f"  [bold yellow]Quick Summary:[/bold yellow]")
    console.print(f"  [yellow]  Build:[/yellow] [white]{build_data.get('build_name')}[/white]")
    console.print(f"  [yellow]  Class:[/yellow] [white]{class_name}[/white]")
    console.print(f"  [yellow]  Primary:[/yellow] [white]{build_data.get('primary_attribute')}[/white]")
    console.print(f"  [yellow]  PDF:[/yellow] [cyan]{abs_path}[/cyan]")
    console.print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            from cli import handle_keyboard_interrupt
            handle_keyboard_interrupt()
        except Exception:
            print("\n\nThe flame fades… your session ends.\n")
            sys.exit(0)
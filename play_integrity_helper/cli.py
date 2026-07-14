"""CLI entry point for play-integrity-helper."""
import click
import sys
from rich.console import Console
from .checker import IntegrityChecker
from .config_gen import ConfigGenerator
from .device import DeviceManager

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """play-integrity-helper - Pass Play Integrity checks on cloud phones."""
    pass

@main.command()
@click.option("--device", required=True, help="Device IP:PORT (e.g. 192.168.1.100:5555)")
def check(device):
    """Check current Play Integrity status of a device."""
    console.print(f"[bold blue]Connecting to device:[/bold blue] {device}")
    checker = IntegrityChecker(device)
    result = checker.check()
    console.print(f"[bold green]Device Integrity:[/bold green] {result.get('device', 'unknown')}")
    console.print(f"[bold green]Basic Integrity:[/bold green] {result.get('basic', 'unknown')}")
    console.print(f"[bold green]CTS Profile:[/bold green] {result.get('cts', 'unknown')}")

@main.command()
@click.option("--model", required=True, help="Device model (e.g. Pixel 6)")
@click.option("--manufacturer", required=True, help="Manufacturer (e.g. Google)")
@click.option("--output", default="pif.json", help="Output config file")
def config(model, manufacturer, output):
    """Generate PlayIntegrityFix pif.json config for your device."""
    console.print(f"[bold blue]Generating config for:[/bold blue] {manufacturer} {model}")
    gen = ConfigGenerator(model, manufacturer)
    cfg = gen.generate()
    gen.save(output)
    console.print(f"[bold green]Config saved to:[/bold green] {output}")

@main.command()
@click.option("--device", required=True, help="Device IP:PORT")
@click.option("--config", required=True, help="Path to pif.json")
def push(device, config):
    """Push config file to device via ADB."""
    console.print(f"[bold blue]Pushing config to device:[/bold blue] {device}")
    dm = DeviceManager(device)
    dm.push_config(config)
    console.print("[bold green]Config pushed successfully![/bold green]")
    console.print("[yellow]Please reboot the device and re-run 'check'.[/yellow]")

@main.command()
@click.option("--device", required=True, help="Device IP:PORT")
def verify(device):
    """Verify Play Integrity status after configuration."""
    console.print("[bold blue]Verifying Play Integrity...[/bold blue]")
    checker = IntegrityChecker(device)
    result = checker.check()
    if result.get("device") == "PASS":
        console.print("[bold green]✓ Device passed Play Integrity checks![/bold green]")
    else:
        console.print("[bold red]✗ Device did not pass. Check troubleshooting in README.[/bold red]")

if __name__ == "__main__":
    main()

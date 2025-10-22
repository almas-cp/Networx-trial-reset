import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
import subprocess
import time
import psutil

console = Console()

def find_networx_executable():
    """Find the NetWorx executable path from running processes or common locations"""
    # Check if NetWorx is running and get its path
    for proc in psutil.process_iter(['name', 'exe']):
        try:
            if proc.info['name'] and 'networx.exe' in proc.info['name'].lower():
                return proc.info['exe']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # Common installation paths
    common_paths = [
        r"C:\Program Files\NetWorx\networx.exe",
        r"C:\Program Files (x86)\NetWorx\networx.exe",
        r"C:\Program Files\SoftPerfect\NetWorx\networx.exe",
        r"C:\Program Files (x86)\SoftPerfect\NetWorx\networx.exe",
    ]
    
    for path in common_paths:
        if Path(path).exists():
            return path
    
    return None

def stop_networx_process():
    """Stop the NetWorx process if it's running"""
    killed = False
    for proc in psutil.process_iter(['name', 'pid']):
        try:
            if proc.info['name'] and 'networx.exe' in proc.info['name'].lower():
                console.print(f"[yellow]⚠ Found running process:[/yellow] NetWorx (PID: {proc.info['pid']})")
                proc.terminate()
                proc.wait(timeout=5)
                killed = True
                console.print("[green]✓ NetWorx process terminated[/green]")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
            console.print(f"[red]✗ Error stopping process: {e}[/red]")
    
    return killed

def start_networx_process(exe_path):
    """Start the NetWorx process"""
    if exe_path and Path(exe_path).exists():
        try:
            subprocess.Popen([exe_path], shell=True)
            console.print(f"[green]✓ NetWorx restarted[/green]")
            return True
        except Exception as e:
            console.print(f"[red]✗ Error starting NetWorx: {e}[/red]")
            return False
    else:
        console.print("[red]✗ NetWorx executable not found[/red]")
        return False

def update_networx_config(db_path=r'C:\ProgramData\SoftPerfect\NetWorx\NetWorx.db3'):
    """
    Updates the NetWorx database CONFIG table with current system date and reminder date.
    - TrialDate: Updates to current date
    - NextReminder: Updates to current date + 30 days
    
    Parameters:
    - db_path: Full path to the NetWorx database file
    """
    
    try:
        # Check if file exists
        if not Path(db_path).exists():
            console.print(f"[bold red]✗ Error:[/bold red] Database file not found at:\n  {db_path}", style="red")
            return False
        
        # Get current date and date 30 days from now
        current_date = datetime.now().strftime('%Y-%m-%d')
        reminder_date = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        
        # Display header
        console.print()
        console.print(Panel.fit(
            "[bold cyan]NetWorx Database Updater[/bold cyan]\n"
            "[dim]Updating trial and reminder dates[/dim]",
            border_style="cyan"
        ))
        console.print()
        
        # Find NetWorx executable first
        networx_exe = find_networx_executable()
        if networx_exe:
            console.print(f"[dim]NetWorx location: {networx_exe}[/dim]\n")
        
        # Stop NetWorx process
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[yellow]Stopping NetWorx process...", total=None)
            was_running = stop_networx_process()
            progress.update(task, completed=True)
            time.sleep(1)  # Wait for process to fully terminate
        
        console.print()
        
        # Show dates
        date_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        date_table.add_column("Date Type", style="cyan", no_wrap=True)
        date_table.add_column("Value", style="green")
        date_table.add_row("Current Date", current_date)
        date_table.add_row("Reminder Date (+30 days)", reminder_date)
        console.print(date_table)
        console.print()
        
        # Connect to database with progress indicator
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Connecting to database...", total=None)
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            progress.update(task, completed=True)
            time.sleep(0.3)
        
        # Create results table
        results_table = Table(show_header=True, header_style="bold yellow", box=box.ROUNDED)
        results_table.add_column("Parameter", style="cyan", no_wrap=True)
        results_table.add_column("Old Value", style="red")
        results_table.add_column("New Value", style="green")
        results_table.add_column("Status", justify="center")
        
        # Update TrialDate
        cursor.execute("SELECT PARAM_VALUE FROM CONFIG WHERE PARAM_NAME = 'TrialDate'")
        trial_row = cursor.fetchone()
        
        if trial_row:
            old_trial = trial_row[0]
            cursor.execute("UPDATE CONFIG SET PARAM_VALUE = ? WHERE PARAM_NAME = 'TrialDate'", (current_date,))
            results_table.add_row("TrialDate", old_trial, current_date, "[green]✓[/green]")
        else:
            results_table.add_row("TrialDate", "[dim]not found[/dim]", "[dim]—[/dim]", "[red]✗[/red]")
        
        # Update NextReminder
        cursor.execute("SELECT PARAM_VALUE FROM CONFIG WHERE PARAM_NAME = 'NextReminder'")
        reminder_row = cursor.fetchone()
        
        if reminder_row:
            old_reminder = reminder_row[0]
            cursor.execute("UPDATE CONFIG SET PARAM_VALUE = ? WHERE PARAM_NAME = 'NextReminder'", (reminder_date,))
            results_table.add_row("NextReminder", old_reminder, reminder_date, "[green]✓[/green]")
        else:
            results_table.add_row("NextReminder", "[dim]not found[/dim]", "[dim]—[/dim]", "[red]✗[/red]")
        
        # Commit changes
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Committing changes...", total=None)
            conn.commit()
            progress.update(task, completed=True)
            time.sleep(0.3)
        
        console.print()
        console.print(results_table)
        console.print()
        
        # Close database connection
        cursor.close()
        conn.close()
        
        # Success message
        console.print(Panel.fit(
            "[bold green]✓ Database updated successfully![/bold green]\n"
            f"[dim]File: {Path(db_path).name}[/dim]",
            border_style="green"
        ))
        
        console.print()
        
        # Restart NetWorx if it was running
        if was_running or networx_exe:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("[cyan]Restarting NetWorx...", total=None)
                time.sleep(1)  # Small delay before restart
                start_networx_process(networx_exe)
                progress.update(task, completed=True)
                time.sleep(0.3)
        
        return True
        
    except sqlite3.Error as e:
        console.print()
        console.print(Panel(
            f"[bold red]Database Error:[/bold red]\n{str(e)}",
            border_style="red",
            title="Error"
        ))
        # Restart NetWorx even on error
        if networx_exe:
            start_networx_process(networx_exe)
        return False
    except FileNotFoundError:
        console.print()
        console.print(Panel(
            f"[bold red]File Not Found:[/bold red]\n{db_path}",
            border_style="red",
            title="Error"
        ))
        return False
    except Exception as e:
        console.print()
        console.print(Panel(
            f"[bold red]Unexpected Error:[/bold red]\n{str(e)}",
            border_style="red",
            title="Error"
        ))
        # Restart NetWorx even on error
        if networx_exe:
            start_networx_process(networx_exe)
        return False

# Main execution
if __name__ == "__main__":
    console.print("\n[bold]NetWorx Database Patcher[/bold]", style="cyan")
    console.print("[dim]═" * 50 + "[/dim]\n")
    
    # Update NetWorx database
    update_networx_config()
    
    console.print()

import feedparser
from newspaper import Article
import os
import random
import tempfile
import subprocess
from rich.console import Console
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def view_in_vim(text):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".txt") as tmp:
        tmp.write(text)
        tmp.flush()
        tmp_name = tmp.name
    subprocess.run(["nvim", "-R", "+set nowrap", "+set number", tmp_name])
    os.unlink(tmp_name)

# --- Setup ---
feeds_file = "feeds.txt"

# Load RSS feed URLs
rss_urls = []
with open(feeds_file, 'r') as f:
    rss_urls = [line.strip() for line in f if line.strip()]

# Load already read articles
read_articles = set()
if os.path.exists("read_articles.txt"):
    with open("read_articles.txt", "r") as f:
        read_articles = set(line.strip() for line in f if line.strip())

# Load saved articles
saved_articles = []
if os.path.exists("saved_articles.txt"):
    with open("saved_articles.txt", "r") as f:
        saved_articles = [line.strip() for line in f if line.strip()]

# Load config options
config = {"spacing": "single"}  # Default config
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key.strip()] = value.strip()

# Spinner list
spinner_list = ["dots", "earth", "bouncingBall", "line", "moon", "weather"]
spinner_style = config.get("spinner", "random")

# Pick spinner
if spinner_style == "random":
    chosen_spinner = random.choice(spinner_list)
else:
    chosen_spinner = spinner_style

# --- Main Menu ---
console.print("\n[bold bright_cyan]Choose an option:[/bold bright_cyan]")
console.print("[bold #fabd2f]1.[/bold #fabd2f] Read New Articles")
console.print("[bold #fabd2f]2.[/bold #fabd2f] Read Saved Articles")
console.print("[bold #fabd2f]3.[/bold #fabd2f] Re-Read Past Articles")
console.print("[bold #fabd2f]4.[/bold #fabd2f] Exit\n")

menu_choice = input("\nEnter your choice (1/2/3/4): ").strip()

if menu_choice == "1":
    pass  # Placeholder for full Read New Articles block

elif menu_choice == "2":
    pass  # Placeholder for full Read Saved Articles block

elif menu_choice == "3":
    if not read_articles:
        console.print("\n[bold red]No read articles available.", style="bold red")
        exit()

    output = "\nRead Articles:\n\n"
    read_list = list(read_articles)
    for i, link in enumerate(read_list):
        output += f"{i + 1}. {link}\n"

    view_in_vim(output)

    reread_choice = int(input("\nWhich article number to re-read? ")) - 1

    if 0 <= reread_choice < len(read_list):
        url = read_list[reread_choice]
        console.print(f"\nFetching article from: [blue]{url}[/blue]")

        with Progress(SpinnerColumn(spinner_name=chosen_spinner), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            task = progress.add_task("[cyan]Downloading article...", total=None)
            article = Article(url, browser_user_agent='Mozilla/5.0')
            article.download()
            article.parse()
            progress.update(task, description="[green]Download complete!")

        words = article.text.split()
        word_count = len(words)
        reading_speed_wpm = 200
        estimated_minutes = max(1, (word_count + reading_speed_wpm - 1) // reading_speed_wpm)

        title_text = Text(f"{article.title} ({estimated_minutes} min read)", style="bold bright_yellow")
        output = "\n" + "="*80 + "\n"
        output += title_text.plain + "\n"
        output += "="*80 + "\n\n"

        paragraphs = article.text.split("\n")
        for para in paragraphs:
            if para.strip():
                output += para.strip() + "\n"
                if config.get("spacing", "single") == "double":
                    output += "\n"

        view_in_vim(output)
    else:
        console.print("Invalid selection.", style="bold red")

elif menu_choice == "4":
    console.print("\nGoodbye!", style="bold green")
    exit()

else:
    console.print("Invalid menu choice.", style="bold red")


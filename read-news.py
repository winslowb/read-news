import feedparser
from newspaper import Article
import os

# --- Setup ---

feeds_file = "feeds.txt"

# Load RSS feed URLs
rss_urls = []
with open(feeds_file, 'r') as f:
    for line in f:
        url = line.strip()
        if url:
            rss_urls.append(url)

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

# --- Menu ---

print("\nChoose an option:")
print("1. Read New Articles")
print("2. Read Saved Articles")
print("3. Exit")

menu_choice = input("\nEnter your choice (1/2/3): ").strip()

# --- New Articles Mode ---

if menu_choice == "1":
    # Collect new articles
    article_list = []
    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries:
            if entry.link not in read_articles and entry.link not in saved_articles:
                article_list.append({
                    'title': entry.title,
                    'link': entry.link
                })

    if not article_list:
        print("\nNo new articles available.")
        exit()

    # List articles
    print("\nAvailable New Articles:\n")
    for i, article in enumerate(article_list):
        print(f"{i + 1}. {article['title']}")

    # Ask what to do
    choice = input("\nPick an article number to READ, or type 's' to SAVE for later: ").strip()

    if choice.lower() == 's':
        save_choice = int(input("Which article number to save for later? ")) - 1
        if 0 <= save_choice < len(article_list):
            saved_article = article_list[save_choice]
            with open("saved_articles.txt", "a") as f:
                f.write(saved_article['link'] + "\n")
            print(f"\n[✓] Saved '{saved_article['title']}' for later!")
        else:
            print("Invalid selection.")
        exit(0)

    else:
        choice = int(choice) - 1
        if 0 <= choice < len(article_list):
            selected_article = article_list[choice]
            url = selected_article['link']

            # Fetch and display article
            print(f"\nFetching full article from: {url}")
            article = Article(url, browser_user_agent='Mozilla/5.0')
            article.download()
            article.parse()

            print("\n--- Article Title ---\n")
            print(article.title)

            print("\n--- Article Text ---\n")
            print(article.text)

            # Mark as read
            with open("read_articles.txt", "a") as f:
                f.write(url + "\n")
            print(f"\n[✓] Marked '{selected_article['title']}' as read.")
        else:
            print("Invalid selection.")

# --- Saved Articles Mode ---

elif menu_choice == "2":
    if not saved_articles:
        print("\nNo saved articles available.")
        exit()

    # List saved articles
    print("\nSaved Articles:\n")
    for i, link in enumerate(saved_articles):
        print(f"{i + 1}. {link}")

    saved_choice = int(input("\nWhich saved article number to read? ")) - 1

    if 0 <= saved_choice < len(saved_articles):
        url = saved_articles[saved_choice]
        print(f"\nFetching saved article from: {url}")

        article = Article(url, browser_user_agent='Mozilla/5.0')
        article.download()
        article.parse()

        print("\n--- Article Title ---\n")
        print(article.title)

        print("\n--- Article Text ---\n")
        print(article.text)

        # Mark as read
        with open("read_articles.txt", "a") as f:
            f.write(url + "\n")

        # Remove from saved
        saved_articles.pop(saved_choice)
        with open("saved_articles.txt", "w") as f:
            for link in saved_articles:
                f.write(link + "\n")

        print(f"\n[✓] Marked article as read and removed from saved list.")
    else:
        print("Invalid selection.")

# --- Exit ---

elif menu_choice == "3":
    print("\nGoodbye!")
    exit()

else:
    print("Invalid menu choice.")

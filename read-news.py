import feedparser
from newspaper import Article

# Read RSS feed URLs from feeds.txt
feeds_file = "feeds.txt"

rss_urls = []
with open(feeds_file, 'r') as f:
    for line in f:
        url = line.strip()
        if url:  # skip empty lines
            rss_urls.append(url)

# Parse all feeds and collect articles
article_list = []

print("\nAvailable Articles:\n")
for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        idx = len(article_list) + 1
        print(f"{idx}. {entry.title}")
        article_list.append({
            'title': entry.title,
            'link': entry.link
        })

# Select an article
try:
    choice = int(input("\nWhich article? (enter number) ")) - 1

    if choice < 0 or choice >= len(article_list):
        print("Invalid selection.")
        exit()

    url = article_list[choice]['link']
    print(f"\nFetching full article from: {url}")

    # Create the article object with a real browser user-agent
    article = Article(url, browser_user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')

    article.download()
    article.parse()

    print("\n--- Article Title ---\n")
    print(article.title)

    print("\n--- Article Text ---\n")
    print(article.text)

except Exception as e:
    print(f"Error: {e}")

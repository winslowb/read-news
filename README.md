
📖 read-news
Terminal-based RSS reader and article fetcher, built with Python!

This tool allows you to:
- Load and display articles from your favorite RSS feeds
- Select an article to fetch and read the full text
- Fetch articles using a real browser User-Agent to bypass basic anti-scraping blocks

🚀 Features
- Read RSS feed URLs from a feeds.txt file

- List all recent articles across multiple sources
- Download and parse full article content
- Simple terminal UI with numbered selections
- Automatically uses a realistic Chrome User-Agent

Install Python libraries:
~~~
pip install -r requirements 
~~~

📄 Usage
Clone the repo:

~~~
Copy
Edit
git clone https://github.com/YOUR_USERNAME/read-news.git
cd read-news
Add your favorite RSS feed URLs into feeds.txt (one per line).
~~~

Example feeds.txt:
~~~
https://feeds.a.dj.com/rss/RSSWSJD.xml
https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml
https://www.theverge.com/rss/index.xml
Run the script:
~~~

~~~
python3 read-news.py
Select an article number to read the full content.
~~~

⚠️ Notes
Some subscription-based sites (like WSJ) may still block access despite using a browser User-Agent.

If fetching fails, you’ll see an error message.

📬 Contributions
PRs, ideas, and issues are welcome!
Feel free to fork and customize the project for your own needs.


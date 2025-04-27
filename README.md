
# Term-News

**Term-News** is a fast, colorful, highly-readable newsreader that runs inside your terminal. 
It pulls full articles from your favorite RSS/Atom feeds and formats them beautifully using the Gruvbox color scheme.

Read, save, or re-read articles **without ever leaving your terminal**. 🚀

---

## Features

- 📚 **Read full articles directly inside your terminal** (no opening browsers)
- 🎨 **Gruvbox theme** for beautiful, clear formatting
- 🗂️ **Group articles by feed source** (ex: NPR, Ars Technica, etc.)
- ⏳ **Estimated reading time** displayed after title (ex: "(4 min read)")
- 💬 **Configurable paragraph spacing** (single or double)
- 🎡 **Animated spinners** while articles download (random or fixed)
- 🏷️ **Save articles for later** reading
- 🔄 **Re-read past articles** anytime
- 🧹 **Automatic tracking** of read and saved articles
- ⚙️ **Simple config file (`config.txt`)** for easy tweaks

---

## Installation

1. Clone this repo:

```bash
git clone https://github.com/YOUR_USERNAME/term-news.git
cd term-news
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create your `feeds.txt`:

Add RSS/Atom feed URLs (one per line):

```
https://feeds.arstechnica.com/arstechnica/index
https://feeds.npr.org/1001/rss.xml
https://www.theverge.com/rss/index.xml
```

4. (Optional) Create a `config.txt` to customize behavior:

Example:
```
spacing=single
spinner=earth
```

---

## Usage

Simply run:

```bash
python term-news.py
```

You'll see a menu:

```
Choose an option:
1. Read New Articles
2. Read Saved Articles
3. Re-Read Past Articles
4. Exit
```

Pick an article to read, save it for later, or re-read ones you've already enjoyed.

---


## Roadmap / Planned Features

- 🔍 Search articles by keyword
- 📦 Package as installable CLI app (`pip install term-news`)
- 🌟 Support alternate color themes (Solarized, Dracula)
- 📚 Auto-fetch full archives

---

## License

MIT License.

---

Built with ❤️ and coffee for people who love reading *real news* right inside the terminal.

---

> Feel free to fork, star, and contribute!

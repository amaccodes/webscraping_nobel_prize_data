# webscraping_nobel_prize_data

Scrape Nobel Prize winners from the official site, parse HTML into structured Python objects, analyze trends, and visualize the number of laureates by year — all from a single notebook.

---

## 🚀 What this project does

- **Requests** the page: `https://www.nobelprize.org/prizes/lists/all-nobel-prizes/all/`
- **Parses** prize cards (title, year, description, laureates & links) with BeautifulSoup
- **Builds** a clean Python **list of dicts** and a **Pandas DataFrame**
- **Analyzes** winners (repeat winners, winners per year)
- **Visualizes** award trends using **Matplotlib**

---

## 🧱 Tech stack

- Python (3.9+ recommended)  
- `requests` – fetch HTML  
- `beautifulsoup4` – parse HTML  
- `pandas` – tabular data  
- `numpy` – utilities  
- `matplotlib` – plots  
- `IPython.display` – pretty HTML display in notebooks

---

## 📦 Installation

```bash
# (optional) create & activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# install dependencies
pip install -U pip
pip install requests beautifulsoup4 pandas numpy matplotlib ipython

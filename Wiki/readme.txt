# 🌍 Wikipedia Web Scraping Project using Python

This project is a beginner-friendly **Web Scraping Project** built using **Python, Requests, BeautifulSoup, and Pandas**.  
The script scrapes language information from the official Wikipedia homepage and stores the extracted data into a CSV file.

---

## 🚀 Features

- Scrapes data from Wikipedia homepage
- Extracts:
  - 🌐 Language Name
  - 📝 Language Information
  - 🔗 Language Link
- Saves scraped data into CSV format
- Clean and beginner-friendly code structure

---

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas

---

## 📂 Project Structure

```bash
├── wiki.py
├── Wikipedia_Info.csv
└── README.md
```

---

## 📌 Website Used

Website: https://www.wikipedia.org/

This website is used for educational web scraping practice.

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install requests beautifulsoup4 pandas
```

---

### 2️⃣ Run the Python File

```bash
python wiki.py
```

---

### 3️⃣ Output

After running the script:

```bash
Wikipedia_Info.csv
```

will be created containing all scraped Wikipedia language data.

---

## 📊 Sample Output

| Language | Info | Link |
|---|---|---|
| English | 6,000,000+ articles | https://en.wikipedia.org/ |
| Español | 1,000,000+ artículos | https://es.wikipedia.org/ |

---

## 🧠 What I Learned

- Sending HTTP requests using `requests`
- Parsing HTML using `BeautifulSoup`
- Extracting website data using HTML tags and classes
- Working with lists and dictionaries
- Creating DataFrames using `pandas`
- Exporting scraped data into CSV format

---

## 📜 Code Overview

The script: :contentReference[oaicite:0]{index=0}

- Sends request to Wikipedia homepage
- Parses HTML content
- Finds all language containers
- Extracts language name, information, and links
- Stores extracted data inside a list
- Converts data into a DataFrame
- Saves final output into CSV format

---

## 📈 Future Improvements

- Scrape detailed data from each language page
- Add error handling
- Store data in SQL database
- Create dashboard using Plotly/Dash
- Automate scraping tasks

---

## 🙌 Author

Lucky Singh  
Aspiring Data Scientist 🚀

---

## ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and connect with me on LinkedIn!

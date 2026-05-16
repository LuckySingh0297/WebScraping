
# 💬 Quotes Web Scraping Project using Python

This project is a beginner-friendly **Web Scraping Project** built using **Python, Requests, BeautifulSoup, and Pandas**.  
The script scrapes quotes data from the website **Quotes to Scrape** and stores the extracted information into a CSV file.

---

## 🚀 Features

- Scrapes data from multiple pages
- Extracts:
  - 💬 Quote Text
  - ✍️ Author Name
  - 🏷️ Tags
- Saves data into a structured CSV file
- Clean and beginner-friendly code

---

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas

---

## 📂 Project Structure

```bash
├── quotes.py
├── Quotes_Info.csv
└── README.md
```

---

## 📌 Website Used

Website: https://quotes.toscrape.com/

This website is specially made for practicing web scraping.

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install requests beautifulsoup4 pandas
```

---

### 2️⃣ Run the Python File

```bash
python quotes.py
```

---

### 3️⃣ Output

After running the script:

```bash
Quotes_Info.csv
```

will be created containing all scraped quotes data.

---

## 📊 Sample Output

| Quote | Author | Tags |
|---|---|---|
| “The world as we have created it...” | Albert Einstein | change, deep-thoughts |
| “It is our choices...” | J.K. Rowling | abilities, choices |

---

## 🧠 What I Learned

- Sending HTTP requests using `requests`
- Parsing HTML using `BeautifulSoup`
- Extracting text data from websites
- Working with loops for multiple pages
- Creating DataFrames using `pandas`
- Exporting scraped data into CSV format

---

## 📜 Code Overview

The script: :contentReference[oaicite:0]{index=0}

- Sends requests to each page
- Parses HTML content
- Finds all quote containers
- Extracts quote text, author, and tags
- Stores data inside a list
- Converts data into a DataFrame
- Saves the final output into CSV format

---

## 📈 Future Improvements

- Add author profile scraping
- Store data in SQL database
- Create interactive dashboard
- Add error handling
- Automate scraping process

---

## 🙌 Author

Lucky Singh  
Aspiring Data Scientist 🚀

---

## ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and connect with me on LinkedIn!

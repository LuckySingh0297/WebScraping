import requests
from bs4 import BeautifulSoup
import pandas as pd

# Empty list
books_data = []

# Loop through all 50 pages
for page in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    # Request
    r = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all books
    books = soup.find_all('article', class_='product_pod')

    # Loop each book
    for book in books:

        # Title
        title = book.h3.a['title']

        # Price
        price = book.find('p', class_='price_color').text

        # Availability
        availability = book.find('p', class_='instock availability').text.strip()

        # Rating
        rating = book.find('p')['class'][1]

        # Append data
        books_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating
        })

# Convert into DataFrame
df = pd.DataFrame(books_data)

# Show first rows
print(df.head())

# Save CSV
df.to_csv("books_data.csv", index=False)

print("Scraping Completed Successfully!")
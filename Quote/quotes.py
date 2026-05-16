import requests
import pandas as pd
from bs4 import BeautifulSoup

quotes_info = []

for x in range(1, 11):   # quotes site has ~10 pages
    url = f"https://quotes.toscrape.com/page/{x}/"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    quotes = soup.find_all('div', class_="quote")

    for item in quotes:
        quote_text = item.find('span', class_='text').text.strip()
        author = item.find('small', class_='author').text.strip()

        tags = item.find_all('a', class_='tag')
        tag_list = [t.text for t in tags]

        all_quotes = {
            "Quote": quote_text,
            "Author": author,
            "Tags": ", ".join(tag_list)
        }

        quotes_info.append(all_quotes)

df = pd.DataFrame(quotes_info)
df.to_csv("Quotes_Info.csv", index=False)
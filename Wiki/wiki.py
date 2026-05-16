import requests
import pandas as pd
from bs4 import BeautifulSoup

wiki_info = []

url = "https://www.wikipedia.org/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# similar to find_all in your code
languages = soup.find_all('a', class_="link-box")

for item in languages:
    lang_name = item.find('strong').text.strip()
    lang_subtext = item.find('small').text.strip()
    lang_link = "https://www.wikipedia.org" + item['href']

    all_data = {
        "Language": lang_name,
        "Info": lang_subtext,
        "Link": lang_link
    }

    wiki_info.append(all_data)

df = pd.DataFrame(wiki_info)
df.to_csv("Wikipedia_Info.csv", index=False)
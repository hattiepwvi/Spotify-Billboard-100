import requests
from bs4 import BeautifulSoup
from pprint import pprint

date = input("which year do you want to travel to? Type hte date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
texts = soup.select("#title-of-a-story")
texts = [text.getText().replace('\n', '').replace('\t', '') for text in texts]
# for text in soup.select("li #title-of-a-story"):
#     heading = text.getText()
#     cleaned_heading = heading.replace('\n', '').replace('\t', '')
#     pprint(heading)
pprint(texts)


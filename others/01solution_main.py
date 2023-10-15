import requests
from bs4 import BeautifulSoup
from pprint import pprint

date = input("which year do you want to travel to? Type hte date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

pprint(song_names)


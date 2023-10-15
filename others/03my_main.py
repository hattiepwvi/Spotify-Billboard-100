import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"
CLIENT_SECRET = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"
REDIRECT_URI = 'yinyueshizhiyujiaojiaoshangtongdekaixinguo'  # 这个必须在Spotify Developer Dashboard中配置
USERNAME = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]

pprint(user_id)

date = input("which year do you want to travel to? Type hte date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

pprint(song_names)

uris = []

for song_name in song_names:
    results = sp.search(q=song_name, type='track')
    try:
        if results['tracks']['items']:
            uri = results['tracks']['items'][0]['uri']
            uris.append(uri)
    except:
        if results['tracks']['items'] is None:
            continue


print(uris)

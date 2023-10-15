import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"
CLIENT_SECRET = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"
REDIRECT_URI = 'http://example.com'  # 这个必须在Spotify Developer Dashboard中配置

sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, redirect_uri=REDIRECT_URI)

auth_url = sp_oauth.get_authorize_url()

token_info = sp_oauth.get_cached_token(auth_url)

sp = spotipy.Spotify(auth=token_info['access_token'])

playlists = sp.current_user_playlists()
for playlist in playlists['items']:
    print(f"Playlist: {playlist['name']}")



date = input("which year do you want to travel to? Type hte date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

pprint(song_names)


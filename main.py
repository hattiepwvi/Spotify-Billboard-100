import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"
CLIENT_SECRET = "yinyueshizhiyujiaojiaoshangtongdekaixinguo"
REDIRECT_URI = 'yinyueshizhiyujiaojiaoshangtongdekaixinguo'  
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

# pprint(song_names)

song_uris = []

year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
        # pprint(song_uris)
    except IndexError:
        pprint(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f'{date} Billboard 100'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist['id']
print(playlist)

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print(f'Added songs to playlist with ID: {playlist_id}')






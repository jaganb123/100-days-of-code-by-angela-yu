from bs4 import BeautifulSoup
import requests, datetime, json, os, spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

URL = "https://www.billboard.com/charts/hot-100/"
scope = "playlist-modify-private"

def load_secrets() : 
    with open("secrets.json") as file:
        # print(json.load(file).get("secret"))
        contents = json.load(file)
        os.environ["SPOTIPY_CLIENT_ID"] = contents["client"]
        os.environ["SPOTIPY_CLIENT_SECRET"] = contents["secret"]
        os.environ["SPOTIPY_REDIRECT_URI"] = "https://www.example.com"
        del contents
load_secrets()
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

user_id = spotify.me()['id']

while True:
    try:
        user_date = input("Enter the date inn YYYY-MM-DD format, to search all the hit songs in that day : ")
        date_check = datetime.datetime.strptime(user_date, "%Y-%m-%d")
        # print(user_date, date_check)
        break
    except Exception as e:
        print("You entered wrong date format, enter again or ctrl + c to quit..")
        print(e)

response = requests.get(f"{URL}/{user_date}/")
soup = BeautifulSoup(response.text, "html.parser")

song_title_chart =[song_div for song_div in soup.find(name="div", class_="u-max-width-970 lrv-u-margin-lr-auto").findAll(name="div", class_="o-chart-results-list-row-container")]
song_title = [" ".join(song.find("h3").string.split()) for song in song_title_chart]

print(f"total songs : {len(song_title)}")

def search_query(song):
    search_query = f"{song}, year='{date_check.year}', type='track'"
    return search_query
i = 0
def get_song_uri(json_str):
    global i 
    i += 1
    uri = None
    if len(json_str['tracks']['items']):
        album = json_str['tracks']['items']
        for obj in album:
            if obj['type'] == 'track':
                uri = obj['uri']
        print(f"got the match, song {i}")
        # print(uri)
        return uri
    else:
        print(f"No match, song {i}")
        return None

song_uri_list = [ get_song_uri(spotify.search(search_query(song))) for song in song_title]
song_uri_list = [song for song in song_uri_list if song != None]
print(song_uri_list)
print(f"song with uri and none: {len(song_uri_list)}")
playlist_name = f"{user_date} BillBoard 100"

user_action = "n" # input(f"Shall i create a playlist {playlist_name} ? Y/n")
if user_action in "Yy":
    spotify.user_playlist_create(user=user_id, name=playlist_name, public=False)

spotify.playlist_add_items(playlist_id="7vAPJs6Ylqwxxv4S9Mihoo", items=song_uri_list)

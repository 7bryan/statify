import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
if results is not None:
    for idx, item in enumerate(results["items"]):
        track = item["track"]
        print(idx, track["artists"][0]["name"], " - ", track["name"])

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="20fd408cacad49bfacfa228e1183c3da",
                                                           client_secret="1c9fb79aa2c14b9db4433b2d0475a4f7"))
tracks = []
my_playlist = "https://open.spotify.com/playlist/4oe5mqIVmjBHmFPFhSdjgb?si=4a42dd6ff6f44143"

playlist_link = my_playlist
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    tracks.append(track["track"]["album"]["name"])

x = 5
print(tracks[1:x])




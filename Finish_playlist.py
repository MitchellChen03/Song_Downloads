import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import urllib.request

from pytube import YouTube
import os


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="20fd408cacad49bfacfa228e1183c3da",
                                                           client_secret="1c9fb79aa2c14b9db4433b2d0475a4f7"))
downloads = []
loads = []

my_playlist = input("Please input the playlist link you wish to download: ")

playlist_link = my_playlist
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:

    album = track["track"]["album"]["name"]
    downloads.append(album)

    my_songs = [item.replace(" ", "") for item in downloads]
print(my_songs)

for i in my_songs:
    print(i)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + i)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video_ids)
    loads.append("https://www.youtube.com/watch?v=" + video_ids[0])
    print(loads)




# takes the list of youtube links, and goes on youtube to convert to mp3

for load in downloads:
    yt = YouTube(load)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

print("done")

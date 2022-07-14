import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import urllib.request

from pytube import YouTube
import os

playlist = []
downloads = []
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="Client id",
                                                           client_secret="Client id"))
# user chooses what they want to do




#this is for searching artists and how many songs to return

artist_search= input("What artist do you want to search for: ")
numofsongs = input("How many songs do you want: ")
numofsongs = int(numofsongs)


results = sp.search(q=artist_search, limit=numofsongs)
for idx, track in enumerate(results['tracks']['items']):
    playlist.append(track['name'])
print(playlist)


my_songs = [item.replace(" ", "") for item in playlist]


# takes the songs pulled from spodify artists into a list which is searched for on youtube which leaves us a link :)

for i in my_songs:
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + i)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    downloads.append("https://www.youtube.com/watch?v=" + video_ids[0])


print(downloads)


# takes the list of youtube links, and goes on youtube to convert to mp3

for load in downloads:
    yt = YouTube(load)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

print("done")
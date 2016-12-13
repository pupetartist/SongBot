#-*-encode:utf-8 -*-
from get import Musix
from get import Spotify


user = Musix()
user1 = Spotify()

lyrics = input("¿Qué canción buscas?")

res = user.getTrack(lyrics)
tracks = [i["track"]["track_name"] + " - " + i["track"]["artist_name"] for i in res["message"]["body"]["track_list"] if len(res["message"]["body"]["track_list"]) is not 0]

for song in tracks:

	res1 = user1.getDemo(song)
	
	if len(res1["tracks"]["items"]) == 0:
		print(song + " - demo not found")
	else:
		demo = res1["tracks"]["items"][0]["preview_url"]
		print(song + "-" + demo)
#-*-encode:utf-8 -*-
from apps.Finder.Apis.get import Musix, Spotify



user = Musix()
user1 = Spotify()

def getMusic():
	lyrics_demo = []

	#lyrics = input("¿Qué canción buscas?")

	lyrics = input()

	res = user.getTrack(lyrics)
	tracks = [i["track"]["track_name"] + " - " + i["track"]["artist_name"] for i in res["message"]["body"]["track_list"] if len(res["message"]["body"]["track_list"]) is not 0]

	for song in tracks:

		res1 = user1.getDemo(song)
	
		if len(res1["tracks"]["items"]) == 0:
			#print(song.encode('ascii', 'ignore').decode('ascii') + " - demo not found")
			pass
		else:
			demo = res1["tracks"]["items"][0]["preview_url"]
			#print(song.encode('ascii', 'ignore').decode('ascii') + "-" + demo)
			lyrics_demo.append({'letra':song.encode('ascii', 'ignore').decode('ascii'), 'demo':demo})
	return {'lyrics_demo':lyrics_demo}






	
	

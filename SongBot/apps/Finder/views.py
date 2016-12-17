#-*-encode:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from apps.Finder.Apis.get import Musix, Spotify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def getmusic(request):	
	
	
	lyrics = request.GET.get('q')
	if lyrics is not None and lyrics != '':
		user = Musix()
		user1 = Spotify()
		lyrics_demo = []
		#lyrics = input("¿Qué canción buscas?" 
		res = user.getTrack(lyrics)
		tracks = [i["track"]["track_name"] + " - " + i["track"]["artist_name"] \
					for i in res["message"]["body"]["track_list"] if len(res["message"]["body"]["track_list"]) \
					is not 0]
		for song in tracks:
			res1 = user1.getDemo(song)
			
			if len(res1["tracks"]["items"]) == 0:

				artista_cancion=song.split(' - ')
				lyrics_demo.append({'letra':song.encode('ascii', 'ignore').decode('ascii'), "demo":"-Sin demo", \
				'cancion':artista_cancion[0], 'artista':artista_cancion[1]} )

			else:
				artista_cancion=song.split(' - ')
				spotify_url = res1["tracks"]["items"][0]["external_urls"]["spotify"]
				demo = res1["tracks"]["items"][0]["preview_url"]
				img = res1["tracks"]["items"][0]["album"]["images"][1]["url"]
				lyrics_demo.append({'letra':song.encode('ascii', 'ignore').decode('ascii'), \
				'demo':demo, 'img':img, "spotify_url":spotify_url, 'cancion':artista_cancion[0], \
				'artista':artista_cancion[1]})
		context = {'lyrics': lyrics_demo}
		return render(request,'home.html', context)
	else:
		return render(request,'home.html')




	
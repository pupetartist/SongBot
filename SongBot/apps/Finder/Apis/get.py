#-*-encode:utf-8 -*-
import requests
import json
from apps.Finder.vies import getmusic

class Musix():
	i=page*10
	def __init__(self):
		self.url = "http://api.musixmatch.com/ws/1.1/"
		self.token = "a08b8cc21b558ca04935043a1edceca4"

	def getTrack(self, lyrics):
		self.url = "http://api.musixmatch.com/ws/1.1/track.search"
<<<<<<< HEAD:SongBot/apps/Finder/Apis/get.py
		parametros = {"apikey": self.token, "q_lyrics": lyrics, "page_size":10, "page":i }
=======
		parametros = {"apikey": self.token, "q_lyrics": lyrics, "page_size": "20"}
>>>>>>> 59ff552858713332670f47b59f61fb242ea049a9:SongBot/Apis/get.py
		resultado = requests.get(self.url, params = parametros).json()
		return resultado

class Spotify():

	def __init__(self):
		self.url = "https://api.spotify.com/v1/"

	def getDemo(self, song):
		self.url = "https://api.spotify.com/v1/search"
		parametros = {"q": song, "type": "track", "limit": "10", "offser":i}
		resultado = requests.get(self.url, params = parametros).json()
		return resultado

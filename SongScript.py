import spotipy
import spotipy.oauth2
import json

myid = "f15612ae930749cba6540f8965bf402c"
mysecret = "f109be37922b42b3885fa4dd62a699c7"

credentials = spotipy.oauth2.SpotifyClientCredentials(client_id=myid, client_secret=mysecret)
sp = spotipy.Spotify(client_credentials_manager=credentials)
sp.trace=False

feat = sp.audio_features(['5YEOzOojehCqxGQCcQiyR4'])

with open('features2016.txt', 'a') as file:
	file.write(json.dumps(feat))
	file.write('\n')

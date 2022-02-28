from django.shortcuts import render
import requests
from DashboardPage.forms import Lyrics

def WLyrics(request):
    if request.method == "POST":
        if "song" in request.POST:
            form = Lyrics(request.POST)
            if form.is_valid():
                author = form.cleaned_data.get('author')
                song = form.cleaned_data.get('song')
                url = "https://api.lyrics.ovh/v1/" + str(author) + "/" + str(song)
                r = requests.get(url).json()
                try:
                    lyrics = r["lyrics"]
                    return {"lyrics" : lyrics}
                except:
                    return {"lyrics": "Not found !"}
            return {"lyrics": "Not found !"}
            

        

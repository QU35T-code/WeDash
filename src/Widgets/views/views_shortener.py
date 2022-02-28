from django.shortcuts import render
import requests
from Widgets.forms import Shortener

def WShortener(request):
    if request.method == "POST":
        if "shortener" in request.POST:
            form = Shortener(request.POST)
            if form.is_valid():
                my_url = form.cleaned_data.get('shortener')
                url = "https://cleanuri.com/api/v1/shorten"
                data = {"url": my_url}
                r = requests.post(url, data=data)
                dict = r.json()
                try:
                    new_url = dict["result_url"]
                    my_context = {"shortener": new_url}
                    return my_context
                except:
                    return {"shortener": "Not found !"}   
            else:
                return {"shortener": "Error"}

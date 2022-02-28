import requests
from Widgets.forms import Hash

def Dehash(request):
    if request.method == "POST":
        if "hash" in request.POST:
            form = Hash(request.POST)
            if form.is_valid():
                md5 = form.cleaned_data.get('hash')
                url = "https://api.dehash.lt/api.php"
                params = {"search": md5}
                r = requests.get(url, params=params)
                dehash = r.text
                if ("ERROR 11" in dehash):
                    return {"dehash": "Not found !"}
                try:
                    my_context = {"dehash": dehash.split(":")[1]}
                    return my_context
                except:
                    return {"dehash": "Not found !"}
            else:
                return {"dehash": "Not found !"}

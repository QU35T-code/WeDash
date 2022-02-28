import requests

def WCat(request):
    if request.method == "POST":
        if "cat" in request.POST:
            url = "https://api.thecatapi.com/v1/images/search"
            r = requests.get(url)
            dict = r.json()
            try:
                link_cat = dict[0]["url"]
                return {"cat": link_cat}
            except:
                return {"cat": "Error !"}
        else:
            return {"cat": "Error !"}
    else:
        return {"cat": "Error !"}

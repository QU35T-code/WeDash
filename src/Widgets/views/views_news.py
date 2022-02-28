import requests
from Widgets.forms import News

def WNews(request):
    if request.method == "POST":
        if "keyword_choice" and "lang_choice" in request.POST:
            form = News(request.POST)
            if form.is_valid():
                keyword = form.cleaned_data['keyword_choice']
                lang = form.cleaned_data['lang_choice']
                url = "https://newsapi.org/v2/everything"
                api_key = "53af4256b828479e9dab539907d99faf"
                params = {"q": str(keyword), "from": "2021-11-22", "sortBy": "publishedAt", "language": str(lang), "apiKey": api_key}
                r = requests.get(url, params=params)
                dict = r.json()
                sample = dict["articles"]
                context = {
                    "form" : form,
                    "all_articles": sample,
                }
                return context
            else:
                return {"news": "Error"}
    form = News()
    return {"form": form}

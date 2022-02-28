import requests
from Widgets.forms import Crypto

def WCrypto(request):
    if request.method == "POST":
        if "crypto_choice" in request.POST:
            form = Crypto(request.POST)
            if form.is_valid():
                crypto = form.cleaned_data['crypto_choice']
                url = "https://data.messari.io/api/v1/assets/" + str(crypto) + "/metrics"                                          
                r = requests.get(url)                                                                                              
                dict = r.json()                                                                                                    
                data = dict["data"]
                symbol = data["symbol"]
                name = data["name"]
                price_usd = data["market_data"]["price_usd"]
                context = {
                    "form" : form,
                    "symbol": symbol,
                    "name": name,
                    "price": price_usd,
                }
                return context
            else:
                return {"crypto": "Error"}
    form = Crypto()
    return {"form": form}

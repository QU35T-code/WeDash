import requests
from Widgets.forms import Horoscope

def WHoroscope(request):
    if request.method == "POST":
        if "horoscope_choice" in request.POST:
            form = Horoscope(request.POST)
            if form.is_valid():
                sign = form.cleaned_data['horoscope_choice']
                url = "https://aztro.sameerkumar.website"
                params = {"sign": sign, "day": "today"}
                r = requests.post(url, params=params)
                dict = r.json()
                try:
                    date_range = dict["date_range"]
                    current_date = dict["current_date"]
                    description = dict["description"]
                    compatibility = dict["compatibility"]
                    mood = dict["mood"]
                    color = dict["color"]
                    lucky_number = dict["lucky_number"]
                    lucky_time = dict["lucky_time"]
                    context = {
                        "form" : form,
                        "date_range": date_range,
                        "current_date": current_date,
                        "description": description,
                        "compatiblity": compatibility,
                        "mood": mood,
                        "color": color,
                        "lucky_number": lucky_number,
                        "lucky_time": lucky_time,
                    }
                    return context
                except:
                    return {"horoscope": "Error"}
            else:
                return {"horoscope": "Error"}
    form = Horoscope()
    return {"form": form}

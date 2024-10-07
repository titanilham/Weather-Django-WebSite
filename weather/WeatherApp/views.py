
import requests
from django.shortcuts import render
from .config import API_KEY


def index(request):
    """Главная страница"""
    weather = ""
    error = ""
    city_name = ""

    if request.method == "POST":
        if city := request.POST.get("city"):
            try:
                response = requests.get(
                    f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no",
                    timeout=10
                )
                print(response.text)
                response.raise_for_status()
                data = response.json()
                weather = data["current"]["temp_c"]
                weather = round(float(weather))
                city_name = data["location"]["name"]
            except requests.RequestException as e:
                error = "Check city name"
            except KeyError:
                error = "Incorrect weather service response."

        else:
            error = "No city specified."
    return render(request, "index.html", {"weather": weather, "error": error, "city_name": city_name})

from locations import locations
import requests
import os
from dotenv import load_dotenv

load_dotenv()

for coord in locations:

        parameters = {
                "lat": coord["lat"],
                "lon": coord["lon"],
                "units": "metric",
                "cnt": 3,
                "appid": os.getenv("API_KEY")
            }


        weather_endpoint = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
        weather_endpoint.raise_for_status()
        weather_data = weather_endpoint.json()["list"] # retrieves directly the most important list from the json data.
        print(weather_data)

        forecast_list = []
        for data in weather_data:
                time = data["dt_txt"].split(" ")[1]
                weather_id = data["weather"][0]["id"]
                forecast_list.append({"time":time, "status": weather_id, "location": coord["name"]})










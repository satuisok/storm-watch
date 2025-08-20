import pandas as pd
import requests
import os
from dotenv import load_dotenv
from weather_data import fetch_forecast

load_dotenv()

storm_codes = pd.read_csv("storm_codes.csv")
code_dict = dict(zip(storm_codes["code"], storm_codes["description"]))

# This is a test list for the Telegram to prevent unnecessary api calls from the OW API
# forecast_list = [{'time': '12:00:00', 'status': 200, 'location': 'Koivusaari'}, {'time': '15:00:00', 'status': 500, 'location': 'Koivusaari'}, {'time': '18:00:00', 'status': 212, 'location': 'Koivusaari'}, {'time': '12:00:00', 'status': 500, 'location': 'Näköalapaikka'}, {'time': '15:00:00', 'status': 500, 'location': 'Näköalapaikka'}, {'time': '18:00:00', 'status': 500, 'location': 'Näköalapaikka'}]


forecast_list = fetch_forecast()

if forecast_list:
        for weather in forecast_list:
                # Send a Telegram message if the weather id is in storm codes.
                # The bot could be separated to its own separate function, but I'm lazy...
                if weather["status"] in code_dict:
                        message = f"Expect: {code_dict[weather['status']]} today at {weather['time']} in {weather['location']}!"
                        url = f"https://api.telegram.org/bot{os.getenv("TELEGRAM_API")}/sendMessage"
                        payload = {
                                'chat_id': os.getenv("TELEGRAM_BOT_ID"),
                                'text': message
                        }

                        response = requests.get(url, params=payload)
                        print(response.status_code)
else:
        print("Missing forecast.")


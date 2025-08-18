import pandas as pd
import requests
import os
from dotenv import load_dotenv
from weather_data import forecast_list

load_dotenv()

# This is a test list for the Telegram to prevent unnecessary api calls from the OW API
# forecast_list = [{'time': '12:00:00', 'status': 800}, {'time': '15:00:00', 'status': 212}, {'time': '18:00:00', 'status': 500}]

storm_codes = pd.read_csv("storm_codes.csv")
code_dict = dict(zip(storm_codes["code"], storm_codes["description"]))

for weather in forecast_list:
        # Send a Telegram message if the weather id is in storm codes
        if weather["status"] in code_dict:
                message = f"Expect: {code_dict[weather['status']]} today at {weather['time']} in {weather['location']}!"
                url = f"https://api.telegram.org/bot{os.getenv("TELEGRAM_API")}/sendMessage"
                payload = {
                        'chat_id': os.getenv("TELEGRAM_BOT_ID"),
                        'text': message
                }

                response = requests.get(url, params=payload)
                print(response.status_code)
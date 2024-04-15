import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

#nutritionix
gender = "female"
age = 21
weight_kg = 42
height_cm = 153

app_id = os.getenv('APP_ID')
api_key = os.getenv('API_KEY')
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
print("tell me which exercise you did: ")
query = input()
params = {"query" : query,
          "gender":gender,
          "age" : age,
          "weight_kg":weight_kg,
          "height_cm":height_cm}
header = {"x-app-id" : app_id,
          "x-app-key" : api_key,}
response = requests.post(url = nutritionix_endpoint, json = params, headers = header)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#sheety

sheety_endpoint = "https://api.sheety.co/8bd0b52fe6f435fb7b143335b3518a83/dataWorkoutTracker/sheet1"

for exercise in result['exercises']:
    sheet_inputs = {
        "sheet1" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories']
        }
    }
#no authentication
#sheet_resp = requests.post(url = sheety_endpoint, json=sheet_inputs)

#basic authentication
pw = os.getenv('PASS')
sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=("sumedha",pw))
print(sheet_response.text)






import requests, json, datetime

NUTRITIONX_APP_ID = "24128749"
NUTRITIONX_APP_KEY = "ad80928ecf41c2294b1ccef2ca463d1e"

NUTRITIONX_URL = "https://trackapi.nutritionix.com"
NUTRITIONX_EXERCISE_URL = f"{NUTRITIONX_URL}/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/8a0f13d5abe7fc3739822687ddf167a1/myWorkoutsPythonExercise/workouts"
SHEETY_TOKEN = "k#a(tIh7#0&LhSM"
SHEETY_HEADER = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
NUTRITIONX_HEADER = {
    "x-app-id": NUTRITIONX_APP_ID,
    "x-app-key": NUTRITIONX_APP_KEY,
    "x-remote-user-id": "0",
}
nutritionx_params = {
    "query": input("Please enter your exercises today... ")
}

def update_sheet(name, duration, calories):
    dt = datetime.datetime.now()
    post_message = {"workout": {
        'date': dt.strftime("%d/%m/%Y"),
        'time': dt.strftime("%H:%M:%S"),
        'exercise': name,
        'duration': str(duration),
        'calories': calories,
    }
    }
    res = requests.post(url=SHEETY_URL, json=post_message, headers=SHEETY_HEADER)
    # print(res.text)



response = requests.post(url=NUTRITIONX_EXERCISE_URL, json=nutritionx_params, headers=NUTRITIONX_HEADER)
# print(response.text)
data_json = response.json()
# print(data_json)
with open("output.json", "w") as file:
    json.dump(data_json, file, indent=2)
if len(data_json['exercises']) != 0:
    for i in data_json['exercises']:
        exercise_name = i['name']
        duration = i['duration_min']
        calories = i['nf_calories']
        # print(i)
        update_sheet(name=exercise_name, duration=duration, calories=calories)
else:
    print("invalid input")

# response = requests.get(url=SHEETY_URL)
# sheet_data = response.json()
# print(sheet_data)
# sample DATA {'workouts':
# [{'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2},
# {'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 3},
# {'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 4}]}

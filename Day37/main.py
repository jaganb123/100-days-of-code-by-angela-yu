import requests, datetime

pixela_url = "https://pixe.la/v1/users"
USERNAME = "jagan"
TOKEN = "pAV2S&nkb5fF%Z1"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=params)
# print(response.text)

pixela_graph_creation_url = f"{pixela_url}/{USERNAME}/graphs"
graph_id = "graph12"
graph_name = "Cycling Daily"

graph_create_json = {
    "id": graph_id,
    "name": graph_name,
    "unit": "kilometer",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Kolkata"
}
header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_graph_creation_url, json=graph_create_json, headers=header)
# print(response.text)

post_message_url = f"{pixela_graph_creation_url}/{graph_id}"
date = datetime.datetime.today()
date_str = date.strftime("%Y%m%d")
print(date_str, post_message_url)
post_message_params = {
    "date": date_str,
    "quantity": "9",
}

response = requests.post(url=post_message_url, json=post_message_params, headers=header)
print(response.text)
update_message_url = f"{post_message_url}/{date_str}"
print(update_message_url)

update_message_params = {
    "quantity": "5.5"
}

# response = requests.put(url=update_message_url, json=update_message_params, headers=header)
# print(response.text)

# delete_message_url = update_message_url
# response = requests.delete(url=delete_message_url, headers=header )
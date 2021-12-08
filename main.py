import requests

USERNAME = "joshualight"
TOKEN = "1234dsfhgjyutyre456yuj"
pixela_end_point = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_end_point, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "My Cycling Graph",
    "unit": "Km",

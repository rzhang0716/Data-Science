import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "***"

weather_params = {
    "lat":39.744430,
    "lon":-75.545100,
    "exclude":"current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
part_data = weather_data["hourly"][:12]
weather_id = []
# for i in part_data:
#     weather_id.append(i["id"])

# print(part_data[0]["weather"][0]["id"])

for i in range(12):
    dat = part_data[i]["weather"][0]["id"]
    weather_id.append(dat)
print(weather_id)

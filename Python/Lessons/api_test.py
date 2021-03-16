import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"metric","mode":"xml, html","q":"London,uk"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "cdf30a1f3dmshf7871afd94a41b6p1574ddjsn21517ae086ce"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
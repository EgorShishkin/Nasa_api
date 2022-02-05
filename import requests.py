import requests
link = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=DATE&api_key=API_KEY"
api_key = "07c78q1vzrqWcrWxqCtbJzh27p0ADSDZ4zuR8CeQ"
query_params = {"api_key": api_key, "earth_date": "2022-01-01"}
response = requests.get(link, params=query_params)
response
#response.json()
photos = response.json()["photos"]
print(f"Найдено {len(photos)} фотографий.")
photos[1]["img_src"]
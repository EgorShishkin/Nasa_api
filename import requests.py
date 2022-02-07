import requests
from datetime import date

today = str(date.today())
print(today) 
link = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
api_key = "LBdaecawyGyPbftYLxO1T3FxoKJsJBBFb5XgfaEV" #мой апи ключ, у каждого он свой, можно исп-ть demo-ключ
request_params = {"earth_date":"2019-06-03", "api_key":api_key} #тут можно прописать дату
response = requests.get(link, params=request_params)
response
response.json()
photos = response.json()["photos"]
print(f"Найдено {len(photos)} фотографий.")
for number in range(len(photos)):
    #if number!=0:
        photos[number]["img_src"]#выдает фото

import requests

url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

querystring = {"type":"get-recently-added-movies-bycountry","country":"us","page":"1"}

headers = {
    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
    'x-rapidapi-key': "26f4d84a4amsheb7875b5296fbf3p19f5eajsn0e70f5f77485"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
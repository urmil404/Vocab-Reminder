import requests

url = "https://aplet123-wordnet-search-v1.p.rapidapi.com/master"

querystring = {"word":"fuck"}

headers = {
    'x-rapidapi-key': "7084eecd5bmsh74a242975252cc5p134c73jsne8432e550977",
    'x-rapidapi-host': "aplet123-wordnet-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

x = response.decode("utf-8")
print(x)

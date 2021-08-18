
import requests
import random
global world

url_word = "https://random-word-api.herokuapp.com/word?number=" + \
    str(random.randint(1, 1))

response_word = requests.request("GET", url_word)
# print(response_word.status_code)

for word in response_word.json():
    print(f"word : {word}")

# find meaning of random word

url_meaning = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
response2_meaning = requests.request("GET", url_meaning)
data = response2_meaning.json()

try:
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    print(f"definition : {definition}")

    audio = data[0]['phonetics'][0]['audio']
    print(f"audio : {audio}")

except:
    print("No definition found")

import requests
import random
import time

# word = "Test Word"

def VocabReminder():
    url_word = "https://random-word-api.herokuapp.com/word?number=" + \
        str(random.randint(1, 1))
    response_word = requests.request("GET", url_word)

    print(response_word.json())
    word = response_word.json()[0]

    # find meaning of random word
    url_meaning = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response2_meaning = requests.request("GET", url_meaning)
    data = response2_meaning.json()

    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        audio = data[0]['phonetics'][0]['audio']
        print(f"definition : {definition}")
        print(f"audio : {audio}")
    except:
        print("No definition found")
        definition = "No definition found"
        audio = "No audio found"
    return [word, definition, audio]

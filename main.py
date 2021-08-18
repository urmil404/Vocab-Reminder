import time
from plyer import notification
from playsound import playsound
from vocab import *
# import vocab

print(vocab.word)


exit()
if __name__ == '__main__':
    while True:
        notification.notify(
            title=get_words.VocabReminder.word,
            message=get_words.VocabReminder.definition,
            app_icon="E:\\CODES\\Vocab-Reminder\\dictionary.ico",
            timeout=12
        )
        #	time.sleep(6)
        time.sleep(0.5*60)

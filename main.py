import time
from plyer import notification
from playsound import playsound
from vocab import *

# if __name__ == '__main__':
while True:
    word, definition, audio = VocabReminder()

    notification.notify(
        title=word,
        message=definition,
        app_icon="E:\\CODES\\Vocab-Reminder\\dictionary.ico",
        timeout=12
    )
    time.sleep(0.050*60)

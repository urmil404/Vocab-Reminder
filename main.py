import time
from plyer import notification
import get_words as w
from playsound import playsound

if __name__ == '__main__':
    while True:
        playsound(w.audio)
        notification.notify(
            title=w.word,
            message=w.meaning,
            timeout=12
        )
        #	time.sleep(6)
        time.sleep(5*60)

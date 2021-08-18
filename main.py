import time
from plyer import notification





if __name__ == '__main__':
    while True:
        notification.notify(
            title="Urmil",
            message="hello world!",
            app_icon="E:\\CODES\\Vocab-Reminder\\dictionary.ico",
            timeout=12
        )
        #	time.sleep(6)
        time.sleep(60*60)

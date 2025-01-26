import time
import random

from pynput.keyboard import Key, Controller, Listener


spamming = False

def on_press(key):
    global spamming
    if key == Key.tab:
        spamming = True

def on_release(key):
    global spamming
    if key == Key.tab:
        spamming = False

if __name__ == "__main__":
    print("Hold 'Tab' to spam press 'q'.")
    
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    
    while True:
        if spamming:
            Controller().press('q')
            time.sleep(random.uniform(.1, .2))
            Controller().release('q')
            time.sleep(random.uniform(.1, .2))
        else:
            time.sleep(.1)
            
import os
import sys
import time
import random
import cv2 as cv
import numpy as np

from mss import mss
from pynput.mouse import Button, Controller as MouseController, Listener as MouseListener
from pynput.keyboard import Key, Controller as KeyboardController, Listener as KeyboardListener


# Set affinity to all cores
total_cores = os.cpu_count()
all_cores = set(range(total_cores))
os.sched_setaffinity(0, all_cores)


# Variables
mouse_x, mouse_y = 0, 0
match_threshold = 0.8
stop_loot = False

monitor1 = {'top':320, 'left':900, 'width':70, 'height':20}
monitor2 = {'top':405, 'left':825, 'width':260, 'height':310}

# Load images
lootof_template = ['img/trigger/lootof.png']
item_templates = [
    'img/dump/t4/t4_1.png', 'img/dump/t4/t4_2.png', 'img/dump/t4/t4_3.png', 'img/dump/t4/t4_4.png', 'img/dump/t4/t4_5.png',
    'img/dump/t5/t5_1.png', 'img/dump/t5/t5_2.png', 'img/dump/t5/t5_3.png', 'img/dump/t5/t5_4.png', 'img/dump/t5/t5_5.png',
    'img/dump/t6/t6_1.png', 'img/dump/t6/t6_2.png', 'img/dump/t6/t6_3.png', 'img/dump/t6/t6_4.png', 'img/dump/t6/t6_5.png',
    'img/dump/t7/t7_1.png', 'img/dump/t7/t7_2.png', 'img/dump/t7/t7_3.png', 'img/dump/t7/t7_4.png', 'img/dump/t7/t7_5.png',
    'img/dump/t8/t8_1.png', 'img/dump/t8/t8_2.png', 'img/dump/t8/t8_3.png', 'img/dump/t8/t8_4.png', 'img/dump/t8/t8_5.png'
]
exclude_templates = [
    'img/exclude/t3_horse.png', 'img/exclude/t4_stag.png', 'img/exclude/t5_armored_horse.png', 'img/exclude/t5_graywolf.png', 
    'img/exclude/t5_swiftclaw.png', 'img/exclude/t6_wolf.png'
]
trash_templates = [
    'img/trash/empty.png', 'img/trash/t1_trash.png', 'img/trash/t2_trash.png', 'img/trash/t3_trash.png', 'img/trash/t4_trash.png',
    'img/trash/t5_trash.png', 'img/trash/t6_trash.png', 'img/trash/t7_trash.png', 'img/trash/t8_trash.png'
]
bug_templates = [
    'img/bug/bug1.png', 'img/bug/bug2.png'
]

item_templates.reverse()
exclude_templates.extend(trash_templates)
exclude_templates.extend(bug_templates)


# Functions
def on_press(key):
    global stop_loot
    if key == Key.esc:
        stop_loot = True

def on_release(key):
    global stop_loot
    if key == Key.esc:
        stop_loot = False

def on_mouse(x,y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, y

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def clicker(x, y, i, o):
    """ Perform the mouse move and click """
    mouse.position = (x + 24 + random.randint(1, 24), y + 24 + random.randint(1, 24))
    mouse_x, mouse_y = mouse.position

    if mouse_x < monitor2['left'] or mouse_x >= monitor2['left'] + i or mouse_y < monitor2['top'] or mouse_y >= monitor2['top'] + o:
       pass

    else:
        mouse.press(Button.left)
        time.sleep(.08)
        mouse.release(Button.left)
        time.sleep(.05)

def lootof() -> bool:
    """ Confirm the loot of in screen """
    lootof_screen = np.asarray(sct.grab(monitor1))
    _lootof = cv.matchTemplate(lootof_screen, lootof_img, cv.TM_CCOEFF_NORMED)

    # debug
    #cv.imshow('lootofscreen', lootof_screen)
    #cv.imshow('lootof', _lootof)

    _, max_val, _, _ = cv.minMaxLoc(_lootof)
    return max_val >= match_threshold

def lootbox() -> None:
    """ Scan the loot crate of a player """
    lootbox_screen = np.asarray(sct.grab(monitor2))
    _lootbox = cv.cvtColor(lootbox_screen, cv.COLOR_BGR2GRAY)

    # debug
    #cv.imshow('lootboxscreen', lootbox_screen)
    #cv.imshow('lootbox', _lootbox)

    for item in item_template:
        template_result = cv.matchTemplate(_lootbox, item, cv.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv.minMaxLoc(template_result)

        if stop_loot:
            return None

        if max_val >= match_threshold:
            item_x, item_y = max_loc[0], max_loc[1]
            item_left, item_top = item_x, item_y
            item_right = min(item_x + 64, _lootbox.shape[1])
            item_bottom = min(item_y + 64, _lootbox.shape[0])
            
            if item_right >= _lootbox.shape[1] or item_bottom >= _lootbox.shape[0]:
                continue
            
            exclude_match_found = False
            item_region = _lootbox[item_top:item_bottom, item_left:item_right]

            for exclude in exclude_template:
                exclude_result = cv.matchTemplate(item_region, exclude, cv.TM_CCOEFF_NORMED)
                _, exclude_max_val, _, _ = cv.minMaxLoc(exclude_result)

                if exclude_max_val >= match_threshold:
                    exclude_match_found = True
                    break

            if not exclude_match_found:
                x, y = monitor2['left'] + item_x, monitor2['top'] + item_y
                clicker(x, y, _lootbox.shape[1], _lootbox.shape[0])
                return None
            
def run():
    """ Main runtime """
    mouse_listener.start()
    keyboard_listener.start()
    
    while True:
        try:
            lootpixelresult = lootof()

            if lootpixelresult == True:
                keyboard.press(Key.shift)
                time.sleep(.1)
                
                while lootpixelresult:
                    if stop_loot:
                        continue
                    
                    lootbox()
                    lootpixelresult = lootof()
            
                keyboard.release(Key.shift)

            time.sleep(.1)
            if cv.waitKey(1) & 0xFF == ord("q"):
                cv.destroyAllWindows()
                keyboard_listener.stop()
                mouse_listener.stop()
                break

        except Exception as e:
            keyboard.release(Key.shift)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            print(f"error occurred: {e}")
            pass

        
# Load essentials
lootof_img = cv.imread(resource_path(lootof_template[0]), cv.IMREAD_UNCHANGED)
item_template = [cv.imread(resource_path(path), cv.IMREAD_GRAYSCALE) for path in item_templates]
exclude_template = [cv.imread(resource_path(path), cv.IMREAD_GRAYSCALE) for path in exclude_templates]

sct = mss()
mouse = MouseController()
keyboard = KeyboardController()
mouse_listener = MouseListener(on_mouse = on_mouse)
keyboard_listener = KeyboardListener(on_press=on_press, on_release = on_release)

if __name__ == "__main__":
    print('Press Hold ESC to Pause Looting, Running!')
    run()

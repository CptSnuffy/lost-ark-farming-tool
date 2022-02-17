import json
import threading
import time

from pynput import keyboard as kb
from pynput.keyboard import Controller

#Note to self if abilities are not firing from loaded json dictionary use .lower as they are capital letters for formatting purposes
#Add button that explains how to edit keyconfig.json for custom use

class FarmLogic():
    
    def load_config():
        with open('keyconfig.json') as json_file:
            data = json.load(json_file)
            return data
    
    def press_key(key_to_press = 'R', time_to_wait = 30):
        global kill_thread

        while kill_thread is False:
            keyboard.press(key_to_press)
            time.sleep(time_to_wait)

    def on_press(self):
        global kill_thread

        load_settings = self.load_config()
        time_to_wait = load_settings['TIMETOWAIT']
        key_to_press = load_settings['SELECTEDKEY']

        t1 = threading.Thread(target=self.press_key(key_to_press, time_to_wait))

        try:
            if  kill_thread:
                kill_thread = False
                t1.start()
        except AttributeError:
            pass
            
        if kill_thread is False:
            kill_thread = True
            try:
                t1.join()
            except RuntimeError:
                pass


keyboard = Controller()
kill_thread = True

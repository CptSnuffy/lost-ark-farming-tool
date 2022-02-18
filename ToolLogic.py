import json
import threading
import time

from pynput import keyboard as kb
from pynput.keyboard import Controller

#Note to self if abilities are not firing from loaded json dictionary use .lower as they are capital letters for formatting purposes
#Add button that explains how to edit keyconfig.json for custom use

class FarmLogic():
    
    kill_thread = False

    def load_config():
        with open('keyconfig.json') as json_file:
            data = json.load(json_file)
            return data
    
    def press_key(key_to_press = 'R', time_to_wait = 30):
        global kill_thread

        while kill_thread is False:
            print('thread start')
            print(time_to_wait)
            print(key_to_press)
            keyboard.press(key_to_press)
            time.sleep(time_to_wait)

    @classmethod
    def on_press(self, time_to_wait = 31, key_to_press = 'g'):
        global kill_thread

        #load_settings = self.load_config()
        # time_to_wait = load_settings['TIMETOWAIT']
        # key_to_press = load_settings['SELECTEDKEY']

        #We skip right over the while loop and immediately kill new threads provide fix
        t1 = threading.Thread(target=self.press_key(key_to_press, time_to_wait))

        try:
            if  kill_thread:
                kill_thread = False
                print('sleeping')
                print(kill_thread)
                time.sleep(5)
                t1.start()

            elif kill_thread is False:
                kill_thread = True
            try:
                t1.join()
                print('thread killed')
            except RuntimeError as e:
                print(e)
        except AttributeError as e:
            print(e)
            
        


keyboard = Controller()
kill_thread = True

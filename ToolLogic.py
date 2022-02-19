import json
import threading
import time

from pynput import keyboard as kb
from pynput.keyboard import Controller

#Note to self if abilities are not firing from loaded json dictionary use .lower as they are capital letters for formatting purposes
#Add button that explains how to edit keyconfig.json for custom use

kill_thread = True

class FarmLogic():
    
    def load_config():
        with open('keyconfig.json') as json_file:
            data = json.load(json_file)
            return data
    
    def press_key(self, key_to_press = 'R', time_to_wait = 30, kill_thread = False):
        kill_thread = False
        while True:
            print(kill_thread)
            keyboard.press(str(key_to_press))
            time.sleep(int(time_to_wait))
            if kill_thread:
                return

    @classmethod
    def on_press(self,  key_to_press = 'r', time_to_wait = 31):
        global kill_thread
        kill_thread = not kill_thread

        #load_settings = self.load_config()
        # time_to_wait = load_settings['TIMETOWAIT']
        # key_to_press = load_settings['SELECTEDKEY']

        #We skip right over the while loop and immediately kill new threads provide fix
        t1 = threading.Thread(target=self.press_key(key_to_press, time_to_wait, kill_thread))

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


#FarmLogic.on_press()

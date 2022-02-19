import json
import time

from pynput import keyboard
from pynput.keyboard import Controller

kill_thread = True

class FarmLogic():
    

    #Toggles global variable to break out of while loop in new threads
    def toggle_bool():
        global kill_thread
        kill_thread = not kill_thread


    #Loads profiles from keyconfig.json
    def load_config():
        with open('keyconfig.json') as json_file:
            data = json.load(json_file)
            return data
    
    #Presses the selected key at the desired increment; defaults to r every 30 seconds
    def press_key(self, key_to_press = 'R', time_to_wait = 30):
        global kill_thread
        while True:
            print(kill_thread)
            keyboard.press(str(key_to_press))
            time.sleep(int(time_to_wait))
            if kill_thread:
                return

keyboard = Controller()


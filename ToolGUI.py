import itertools
import random
import threading
import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, OptionMenu, StringVar
from tkinter.constants import BOTH, LEFT, RIGHT, X

from ToolLogic import FarmLogic

kill_gui_thread = True
class ToolClient():
    

    #Contains various functions and assignments to set up GUI
    def window_setup(self):
        

        titles = [
                  'Collectibles Made Easy',
                  'Did you know this is against TOS?',
                  'Snuffy\'s Ark Farming Tool',
                  'I can farm just like any other human',
                  'BDSM',
                  'Default CUBE GF',
                  'AFMT',
                  '2003',
                  'Broom Boy Propoganda Machine',
                  'The Gold Hoe',
                  'Sue Berry',
                  'Donna Rush',
                  '25 grams of Benadryl'
                                                        ]


        selected_title = titles[random.randint(0, len(titles)-1)]


        #Math for moving window around by title bar
        def move_window(event):
                root_window.geometry('+{0}+{1}'.format(event.x_root-250, event.y_root))


        #Function starts new thread for key presses so GUI does not freeze
        def start_stop():
            global kill_gui_thread
            kill_gui_thread = not kill_gui_thread
            farm_logic = FarmLogic()
            FarmLogic.toggle_bool()
            key_to_select = key_selection.get().lower().strip()
            time_to_wait = int(wait_string.get())
            t2 = threading.Thread(target=farm_logic.press_key, args= (key_to_select,time_to_wait))

            if kill_gui_thread:
                entry_box.configure(state='normal')
            elif kill_gui_thread is False:
                entry_box.configure(state='disabled')
                t2.start()

        #Function loads keys from keyconfig.json
        def load_keys(profile):
            #the arg passed in as profile is a string that contains the name of the preset (Default, Custom One, Custom Two)
            key_selection.set('')
            key_select_config['menu'].delete(0, 'end')
            key_list = FarmLogic.load_config()
            key_list = key_list.get(profile)
            print(key_list)
            for key in key_list:
                key_select_config.children['menu'].add_command(label=key, command=lambda add_key=key: key_selection.set(add_key))
            key_selection.set(key_list[0])


        #Creates root window and overrides defaults and creates new elements to place on root window
        root_window = tk.Tk()
        root_window.overrideredirect(True)
        title_bar = Frame(root_window,bg ='#292726', relief='flat', bd=2, highlightthickness=0)
        close_button = Button(title_bar, text='X', bg='#292726', activebackground='red', relief='flat', font='bold',fg='white', highlightthickness=0, command=root_window.destroy)
        window = Canvas(root_window,bg ='#343130', highlightthickness=0)
        start_stop_button = Button(window, text='Start/Stop',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=start_stop)
        title_label=Label(title_bar, text=selected_title, bg='#292726', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5')

        #NOTE TO SELF
        #The * operator will unpack values from a dict or list
        #For this program we unpack a returned list element in our optionmenus to populate it with all available options

        #key_selection is defined up here because the command in profile_select_config relies on this variable being assigned
        key_selection = StringVar()

        #Initializes and configures profile
        profile_selection = StringVar()
        profile_selection.set('Default')
        profile_options = FarmLogic.load_config()
        print(type(profile_options))
        profile_select_config = OptionMenu(window, profile_selection, *dict(itertools.islice(profile_options.items(),4)),  command=load_keys)
        profile_select_config.configure(bg='#343130', highlightthickness=0, relief='flat', font='bold', fg='#c4c4c4', activebackground='#383534', activeforeground='#4764f5')
        profile_select_config["menu"].configure(bg='#524d4b', fg='#e8e8e8', activebackground='#877e7b')


        #Initializes keys based on profile
        key_selection.set('R')
        key_options = profile_options[profile_selection.get()]
        key_select_config = OptionMenu(window, key_selection, *key_options)
        key_select_config.configure(bg='#343130', highlightthickness=0, relief='flat', font='bold', fg='#c4c4c4', activebackground='#383534', activeforeground='#4764f5')
        key_select_config["menu"].configure(bg='#524d4b', fg='#e8e8e8', activebackground='#877e7b')

        #Entry box
        wait_string = StringVar()
        wait_string.set(profile_options.get('TIMETOWAIT'))
        entry_box = Entry(window, textvariable=(wait_string), width=6)


        #Root winow
        root_window.geometry('500x250+600+200')
        root_window.title('Collectibles Made Easy')
        root_window['background'] = '#343130'

        #Places elements on specific coordinates
        key_select_config.place(x=95, y=75)
        entry_box.place(x=100,y=110)

        #Packs elements and places some on anchor points
        entry_box.pack
        start_stop_button.pack(side=RIGHT)
        profile_select_config.pack(side=LEFT)
        key_select_config.pack


        #Packs root window and places on achor points
        title_bar.pack(expand=0, fill=X)
        title_label.pack(expand=0, side=LEFT)
        close_button.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)


        #Binds mouse motion for dragging window
        title_bar.bind('<B1-Motion>', move_window)

        #Makes window remain on top of all other windows all the time (there is no minimize button and program does not appear in taskbar)
        root_window.attributes("-topmost", True)
        
        return root_window


    #This function is called by other classes to open the GUI
    def tool_menu(self):
        root_window = self.window_setup()
        root_window.mainloop()

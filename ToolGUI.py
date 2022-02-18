import tkinter as tk
from tkinter import Button, Canvas, Frame, OptionMenu, StringVar
from tkinter.constants import BOTH, RIGHT, X
import itertools
from gevent import config

from ToolLogic import FarmLogic


class ToolClient():
    
    def window_setup(self):

        instance_logic = FarmLogic()

        def move_window(event):
                root_window.geometry('+{0}+{1}'.format(event.x_root-250, event.y_root))

        def file_select():  
            pass
        
        def encrypt():
            pass
        
        def decrypt():
            pass
        
        root_window = tk.Tk()

        root_window.overrideredirect(True)

        title_bar = Frame(root_window,bg ='#292726', relief='flat', bd=2, highlightthickness=0)
        close_button = Button(title_bar, text='X', bg='#292726', activebackground='red', relief='flat', font='bold',fg='white', highlightthickness=0, command=root_window.destroy)

        window = Canvas(root_window,bg ='#343130', highlightthickness=0)
        
        select_button = Button(window, text='Select File',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=file_select)
        encrypt_button = Button(window, text='Encrypt',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=encrypt)
        decrypt_button = Button(window, text='Decrypt',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=decrypt)


        config_text = StringVar()
        config_text.set('Default')
        options = FarmLogic.load_config()
        select_config = OptionMenu(window, config_text, *dict(itertools.islice(options.items(),4)))
        select_config.configure(bg='#343130', highlightthickness=0, relief='flat', font='bold', fg='#c4c4c4', activebackground='#383534', activeforeground='#4764f5')
        select_config["menu"].configure(bg='#524d4b', fg='#e8e8e8')
        #use ["menu"] to edit the drop down section
        print(select_config.keys())

        root_window.geometry('500x250+600+200')
        root_window.title('Encryption')
        root_window['background'] = '#343130'

        select_config.place(x=75,y=90)
        encrypt_button.place(x=375,y=90)
        decrypt_button.place(x=225,y=90)

        select_config.pack
        encrypt_button.pack
        decrypt_button.pack

        title_bar.pack(expand=0, fill=X)
        close_button.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)

        title_bar.bind('<B1-Motion>', move_window)

        root_window.attributes("-topmost", True)
        
        return root_window
    def tool_menu(self):
        print('fired')
        root_window = self.window_setup()
        root_window.mainloop()

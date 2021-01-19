import pyautogui
from tkinter import *
from random import randint

def on_close():
    gui.destroy()

def caffeine():
    print ('Process is active')
    pyautogui.write(str(randint(1, 9)), interval=0.25)
    pyautogui.press('Backspace')
    gui.after(5000, caffeine)

gui = Tk()
Label(gui, text='Hello World! you have taken caffeine in your system.\n Close to disable').pack()
gui.wait_visibility()
gui.after(1, caffeine)
gui.protocol("WM_DELETE_WINDOW", on_close)
gui.mainloop()
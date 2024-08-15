import pyautogui
from tkinter import Tk, Label
from random import randint

def on_close():
    # Properly terminate the Tkinter GUI loop
    gui.quit()

def caffeine():
    print('Process is active')
    try:
        # Simulate typing a random digit and then pressing 'Backspace'
        pyautogui.write(str(randint(1, 9)), interval=0.25)
        pyautogui.press('backspace')
    except pyautogui.FailSafeException:
        print("PyAutoGUI fail-safe triggered.")
    # Schedule the next execution of the caffeine function
    gui.after(5000, caffeine)

# Create and configure the Tkinter window
gui = Tk()
gui.title('Caffeine Monitor')
Label(gui, text='Hello World! You have taken caffeine in your system.\nClose to disable', font=('arial', 12)).pack(padx=20, pady=20)

# Ensure the window is visible before starting the caffeine function
gui.after(1000, caffeine)
gui.protocol("WM_DELETE_WINDOW", on_close)

# Run the Tkinter event loop
gui.mainloop()

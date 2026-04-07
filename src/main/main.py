from tkinter import *
from tkinter import ttk
import toggle_key

WIDTH, HEIGHT = 380, 420

def pause_and_resume_auto_clicker(start, root, frame):
    if start == False:
        # enable_hotkey = Button(root, text="Start")
        ttk.Label(frame, text="Stopped.").grid(column=0, row=0)
    elif start == True:
        ttk.Label(frame, text="Started.").grid(column=0, row=0)

def init_tkinter(root, button):
    button.pack()
    root.mainloop()

def main():
    root = Tk()
    root.title("Auto Clicker")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    # frame_window = ttk.Frame(root, padding=10)
    # frame_window.grid()

    # start_auto_clicker = BooleanVar()
    # start_auto_clicker.set(False)
    # pause_and_resume_auto_clicker(start_auto_clicker, root, frame_window)
    button = Button(root, text="Start", command=toggle_key.main)


    init_tkinter(root, button)

if __name__ == "__main__":
    main()
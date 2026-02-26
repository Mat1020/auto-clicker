# Code from a friend

import tkinter as tk

root = tk.Tk()
root.title("window")
root.geometry("500x500")
thing = tk.IntVar()
thing.set(0)
def increase():
    current_value = thing.get()
    thing.set(current_value + 1)

thingy = tk.Label(root, text="hell owrld")
button = tk.Button(root, text="clicl me plz", command=increase)
number = tk.Label(root, textvariable=thing)

thingy.pack()
button.pack()
number.pack()


root.mainloop()
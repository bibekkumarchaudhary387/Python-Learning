from tkinter import *

def check_name():
    name = entry.get().strip()
    if name == "":
        label.config(text="Please enter your name.")
    else:
        label.config(text=f"Hello, {name}!")

root = Tk()
entry = Entry(root)
entry.pack()

button = Button(root, text="Check", command=check_name)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()

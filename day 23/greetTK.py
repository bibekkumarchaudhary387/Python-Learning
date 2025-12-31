import tkinter as tk

root = tk.Tk()
root.title("Greeting")
root.geometry("300x300")

def greet():
    print("Hello Bibek")

btn = tk.Button(root, text="Greet Me", command=greet).pack()

root.mainloop()
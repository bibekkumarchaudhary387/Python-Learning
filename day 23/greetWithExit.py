import tkinter as tk

root = tk.Tk()
root.title("Greeting")
root.geometry("300x300")

def greet():
    print("Hello Bibek")

btn1 = tk.Button(root, text="Greet Me", command=greet).pack()
btn2 = tk.Button(root, text="Exit", command=root.destroy).pack()

root.mainloop()
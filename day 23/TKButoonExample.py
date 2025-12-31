import tkinter as tk
main = tk.Tk()
main.geometry("500x500")

def hello():
    print("Hello New WOrld!!!")

btn = tk.Button(main, text="RUn the FUnction", command=hello).pack()
main.mainloop()
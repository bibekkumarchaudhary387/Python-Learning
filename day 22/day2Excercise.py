import tkinter as tk

# create the window

root = tk.Tk()
root.title("Welcome App")
root.geometry("500x500")

#creating label

header = tk.Label(root, text="Welcome to day 22", font=(50), bg="green")

#put on screen
header.pack()

#gives infinite loop
header.mainloop()
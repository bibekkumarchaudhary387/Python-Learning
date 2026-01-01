import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

def save_text():
    value = entry.get()     # save text into a variable
    print("Saved value:", value)

button = tk.Button(root, text="Save", command=save_text)
button.pack()

root.mainloop()

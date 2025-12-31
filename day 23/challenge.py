import tkinter as tk

root =tk.Tk()
root.title("Counting System")
root.geometry("300x300")

count = 0

def on_click():
    global count
    count += 1
    print(f"Count is {count}")

btn = tk.Button(root, text="Click to COunt", command=on_click).pack()
root.mainloop()
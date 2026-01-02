import tkinter as tk

def show_message(msg):
    print(msg)

root = tk.Tk()
root.title("Lambda Example")

btn = tk.Button(root, text="Click Me",
                command=lambda: show_message("Hello Tkinter"))
btn.pack(padx=20, pady=20)

root.mainloop()

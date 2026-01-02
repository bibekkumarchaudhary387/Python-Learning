import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

tk.Button(root, text="Show Alert",
          command=lambda: messagebox.showinfo("Info", "This is Tkinter")
          ).pack(padx=20, pady=20)

root.mainloop()

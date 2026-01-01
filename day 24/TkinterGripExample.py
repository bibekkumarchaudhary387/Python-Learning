import tkinter as tk

root = tk.Tk()
root.title("The input Box")
root.geometry("300x300")

label1 = tk.Label(root, text="Usernamee:").grid(row=0,column=0)
input1 = tk.Entry(root).grid(row=0,column=1)

label2 = tk.Label(root, text="Password").grid(row=1,column=0)
input2 = tk.Entry(root).grid(row=1,column=1)
root.mainloop()
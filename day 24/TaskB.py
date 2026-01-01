import tkinter as tk

root = tk.Tk()
root.title("2x2 Grid")
root.geometry("200x200")

label1 = tk.Label(root, text="Hy i am first", bg="red").grid(row=0, column=0)
label2 = tk.Label(root, text="Hy i am Second", bg="green").grid(row=0, column=1)
label3 = tk.Label(root, text="Hy i am Third", bg="yellow").grid(row=1, column=0)
label4 = tk.Label(root, text="Hy i am Fourth", bg="blue").grid(row=1, column=1)

root.mainloop()

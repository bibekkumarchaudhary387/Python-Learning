import tkinter as tk

root = tk.Tk()
root.title("Color checker")
root.geometry("300x300")

def reset():
     root.config(bg = "white")

def apply_color():
    try:
        valid_color = color_in.get().strip()
        if valid_color == "":
               label.config(text="Please enter a color name")
        else:
              root.config(bg=f"{valid_color}")
    except:
        label.config(text="PLease ente a valid color name")

label1 = tk.Label(root, text="Enter a color:")
label1.pack()
color_in = tk.Entry(root)
color_in.pack()

btn1 = tk.Button(root, text="Apply Color", command=apply_color)
btn1.pack()

btn2 = tk.Button(root, text="Reset", command=reset)
btn2.pack()

label = tk.Label(root, text='')
label.pack()

root.mainloop()

import tkinter as tk

root = tk.Tk()

def button_click(welcome):
    the_value = the_screen.get()
    the_screen.delete(0, tk.END) #clearing the screen
    the_screen.insert(0, welcome)

the_screen = tk.Entry(root)
the_screen.grid(row=0, column=0)

for i in range(1,4):
    button = tk.Button(root, text=f"Button {i}", command=lambda x=i: button_click(x)).grid(row=i, column=0)

root.mainloop()
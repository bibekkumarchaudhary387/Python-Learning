import tkinter as tk

def clear():
    the_screen.delete(0, tk.END)

def operation():
    value = the_screen.get()
    the_screen.delete(0, tk.END)
    answer = eval(value)
    the_screen.insert(0, answer)

def button_clicked(number):
    the_screen.insert(tk.END, number)

root = tk.Tk()
root.title("The Calculator")




the_screen = tk.Entry(root)
the_screen.grid(row=0, column=0, columnspan=4)

one = tk.Button(root, text="1", command= lambda: button_clicked(1)).grid(row=1, column=0)
two = tk.Button(root, text="2", command= lambda: button_clicked(2)).grid(row=1, column=1)
tree = tk.Button(root, text="3", command= lambda: button_clicked(3)).grid(row=1, column=2)
cls = tk.Button(root, text="C", command=clear).grid(row=1, column=3)

four = tk.Button(root, text="4", command= lambda: button_clicked(4)).grid(row=2, column=0)
five = tk.Button(root, text="5", command= lambda: button_clicked(5)).grid(row=2, column=1)
six = tk.Button(root, text="6", command= lambda: button_clicked(6)).grid(row=2, column=2)
add = tk.Button(root, text="+", command= lambda: button_clicked("+")).grid(row=2, column=3)

seven = tk.Button(root, text="7", command= lambda: button_clicked(7)).grid(row=3, column=0)
eigth = tk.Button(root, text="8", command= lambda: button_clicked(8)).grid(row=3, column=1)
nine = tk.Button(root, text="9", command= lambda: button_clicked(9)).grid(row=3, column=2)
sub = tk.Button(root, text="-", command= lambda: button_clicked("-")).grid(row=3, column=3)

ten = tk.Button(root, text="0", command= lambda: button_clicked(0)).grid(row=4, column=0)
mul = tk.Button(root, text="x" , command= lambda: button_clicked("*")).grid(row=4, column=1)
div = tk.Button(root, text="/" , command= lambda: button_clicked("/")).grid(row=4, column=2)
eqq = tk.Button(root, text="=", command=operation).grid(row=4, column=3)

root.mainloop()
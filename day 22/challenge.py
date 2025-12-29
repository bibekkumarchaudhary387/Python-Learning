import tkinter as tk

main = tk.Tk()
main.title("Conference Badge")
main.configure(bg='black') # Set window background to black

# Label 1
label1 = tk.Label(main, 
                 text="HELLO MY NAME IS",
                 bg="red", 
                 fg="white",
                 font=("Arial", 12))
label1.pack(pady=20) # External padding (space outside the label)

# Label 2
label2 = tk.Label(main,
                  text="BIBEK KUMAR CHAUDHARY",
                  bg="white",
                  fg="black",
                  font=("Arial", 20, "bold"))
label2.pack(pady=20)

main.mainloop() # Always run the loop on the main window
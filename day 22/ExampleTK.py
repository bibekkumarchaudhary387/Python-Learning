import tkinter as tk

# 1. Create the main window
root = tk.Tk()
root.title("My First App")
root.geometry("400x300") # Width x Height

# 2. Create a Widget (Label)
# We attach it to 'root'
header = tk.Label(root, text="Hello Python!", font=("Arial", 24))

# 3. Place it on the screen
header.pack() # .pack() just drops it in the center top

# 4. Run the loop (This must be the last line!)
root.mainloop()
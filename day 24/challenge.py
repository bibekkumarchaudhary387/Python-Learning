import tkinter as tk

def login_detail():
    SecureEmail = EmailInput.get()
    SecurePassword = PasswordInput.get()
    print(f"---Login Detail--- \nUsernamer: {SecureEmail} \n Passoword: {SecurePassword}")

root = tk.Tk()
root.title("Secure Login")

MainLabel = tk.Label(root, text="Welcome to System").grid(row=0, column=0, columnspan=2) #the header

#email
email = tk.Label(root, text="Email:").grid(row=1, column=0)
EmailInput = tk.Entry(root)
EmailInput.grid(row=1,column=1)

#password
PassowordLabel = tk.Label(root, text="Password:").grid(row=2, column=0)
PasswordInput = tk.Entry(root)
PasswordInput.grid(row=2, column=1)

#login button
login_button = tk.Button(root, text="Login", bg="black", fg="white", font=("Arial", 10), command=login_detail).grid(row=3, column=0, columnspan=2)

root.mainloop()
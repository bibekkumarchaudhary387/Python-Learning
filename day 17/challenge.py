#Daily Challenge: "The Banking System"
#Scenario: Create a simple bank account that tracks money.

#Instructions:
#Create a class BankAccount.
#__init__:
#Takes owner (name) and balance (starting money).
#Method deposit(amount):
#Add amount to self.balance.
#Print: "Deposited $[amount]. New Balance: $[balance]".
#Method withdraw(amount):
#Check if amount > self.balance.
#If yes: Print "Insufficient Funds!".
# #Else: Subtract amount and print "Withdrew $[amount]. New Balance: $[balance]".
# Test it:
# Create an account for "Bibek" with $1000.
# Deposit $5000
# Withdraw $200.
# Withdraw $5000 (Try to break it!).

class BankAccount:
    def __init__(self, name, amount):
            self.name = name
            self.amount = amount
    def Deposit(self,new_amount):
          self.amount += new_amount
          print(f"{new_amount} is added on {self.name} bank account. \nTotal Balance is {self.amount}")
    def Withdraw(self, new_amount):
          self.amount -= new_amount
          print(f"{new_amount} is succesfully withdraw. \n Remaining Balance {self.amount}")

name = input("Enter yout name: ")
amount = int(input("Enter starting amount: "))
p1 = BankAccount(name,amount)

while True:
      user = input("Type (d for deposit, w for withdraw and e for exit) :")

      if user.lower() == "d":
            new_amount = int(input("How much you want to deposit: "))
            p1.Deposit(new_amount)
      elif user.lower() == "w":
            new_amount = int(input("How much you want to Withdraw: "))
            if new_amount > p1.amount:
                  print("Insufficient Balance")
            elif new_amount <= p1.amount:
                  p1.Withdraw(new_amount)
            else:
                  print("Invalid Input")
      elif user.lower() == "e":
            break
      else:
            print("Invalid Input")
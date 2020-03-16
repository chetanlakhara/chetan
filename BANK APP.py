
# BankAccount class 
class Bankaccount: 
    def __init__(self):
        self.balance=5000
        self.name=input("enter your name:")
        self.account_no=int(input("enter your account no: "))
        print("hello welcome to deposit and withraw machine")
	    
# Function to deposite amount 
    def deposit(self):  
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount 
        print("\n Amount Deposited:", amount) 

# Function to withdraw the amount 
    def withdraw(self): 
        amount = float(input("Enter amount to be withdrawn: ")) 
        if self.balance >= amount: 
            self.balance -= amount 
            print("\n You Withdraw:", amount) 
        else: 
            print("\n Insufficient balance  ")
            # Functin to display the amount 
    def display(self): 
        print("\n Net Available Balance =" ,self.balance)
        print("\n name of the account holder :", self.name)
        print("\n account no :",self.account_no)
        # creating an object of class 
 
   
# Calling functions with that class object
s=Bankaccount()
s.deposit() 
s.withdraw() 
s.display() 

            


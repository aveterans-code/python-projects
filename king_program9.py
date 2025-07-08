"""
Program name: king_program9.py
Program Description: Bank Account
Author: Geoff King
Date Created: April 25, 2024

Notes: Imports the python time library

"""
import time
#class for BankAccount 
class BankAccount:
    #constructor method
    def __init__(self, name):
        self._aBalance = 0
        self._aName = name

    #method for deposit
    def deposit(self, amount):
        #if statement to check amount deposit
        if amount < 0:
            #print error message
            print(f"UNABLE to deposit ${amount:0.2f} into", self._aName)
        else:
            #adds amount to account
            self._aBalance += amount
            #prints deposit statement
            print(f"Depositing ${amount:0.2f} into", self._aName)

    #method for withdraw
    def withdraw(self, amount):
        #if statement to check amount of withdrawl
        if amount > self._aBalance:
            #error message
            print(f"NOT enough funds to withdraw ${amount:0.2f} from", self._aName)
        else:
            #subtracts amount from account
            self._aBalance -= amount
            #prints withdrawl statement
            print(f"withdrawing ${amount:0.2f} from", self._aName)

    #method for getBalance 
    def getBalance(self):
        #returns current balance of account
        return self._aBalance

    #method for transfer with parameters amount and to
    def transfer(self, amount, to):
        #prints transfer info
        print(f"Transfering ${amount:0.2f} from", self._aName, "to", to._aName)
        #points to withdrawl method for transfer
        self.withdraw(amount)
        #points to deposit method for transfer
        to.deposit(amount)

    #method to return a string/account balances
    def __str__(self):
        #returns account balances for an account as a string
        return f"{self._aBalance} in account {self._aName}"
 
#creates main function
def main():
    #prints intro
    print("This program simulates bank account transactions\n")
    #Create instance of BankAccount() called MyChecking
    MyChecking = BankAccount("MyChecking")
    #Create instance of BankAccount() called Savings
    Savings = BankAccount("Savings")
    #Print the starting balance for MyChecking & Savings
    print("Starting balances:")
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Deposit $500 into MyChecking
    MyChecking.deposit(500)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Deposit $100 into Savings
    Savings.deposit(100)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Transfer $150 from MyChecking to Savings
    MyChecking.transfer(150, Savings)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Deposit $-50 into MyChecking (error message)
    MyChecking.deposit(-50)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Withdraw $600 from MyChecking (error message)
    MyChecking.withdraw(600)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Withdraw $250 from MyChecking
    MyChecking.withdraw(250)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Withdraw $100 from Savings
    Savings.withdraw(100)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    #Transfer $75 from Savings to MyChecking
    Savings.transfer(75, MyChecking)
    #prints balances
    print(f"MyChecking: ${MyChecking.getBalance():0.2f}, Savings: ${Savings.getBalance():0.2f}\n")
    
    #adds a dividing line
    print("-------------------------------")
    #prints Author's name, course, & program
    print("Geoff King")
    print("CIS 110 ")
    #prints the current date and time
    print(time.ctime())
    #adds a dividing line
    print("-------------------------------")

if __name__ == '__main__':
    main()


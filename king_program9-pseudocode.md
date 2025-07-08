Geoff King
CIS 110
Assignment 9 – BankAccount
April 25, 2024
IPO
I –
P – Transferring money between and in/out of accounts
O – The starting balance, transfers, and ending balances of the accounts

Pseudocode
• Import time
• Create class BankAccount
	o Create constructor method (self, name)
		▪ Set aBalance = 0
		▪ Set aName = name
	o Create method to deposit money with parameter amount (self, amount)
		▪ If amount less than 0, print error message
		▪ If amount greater than zero, deposit money
		▪ Print when money is deposited
	o Create method to withdraw money, with parameter amount (self, amount)
		▪ If amount is greater than aBalance, print error message
		▪ If not greater than balance, withdraw the money
		▪ Print when money is withdrawn
	o Create method to get the balance
		▪ Returns aBalance
	o Create transfer method with parameters amount and to (self, amount, to)
		▪ Pass withdraw method
		▪ Pass deposit method
		▪ If no errors, print transfer message
	o Create message to return a string with the current account and balance
		▪ return balance
	o Create the main function
		▪ Print intro
		▪ Create instance of BankAccount() called MyChecking
		▪ Create instance of BankAccount() called Savings
		▪ Print the starting balance for MyChecking, Savings
		▪ Deposit $500 into MyChecking
		▪ Print balances
		▪ Deposit $100 into Savings
		▪ Print balances
		▪ Transfer $150 from MyChecking to Savings
		▪ Print balances
		▪ Deposit $-50 into MyChecking (error message)
		▪ Print balances
		▪ Withdraw $600 from MyChecking (error message)
		▪ Print balances
		▪ Withdraw $250 from MyChecking
		▪ Print balances
		▪ Withdraw $100 from Savings
		▪ Print balances
		▪ Transfer $75 from Savings to MyChecking
		▪ Print balances
• Print name and class info
End main()
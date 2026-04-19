class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
 
    def display(self):
         print(self.name, self.balance)
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
    
s1 = BankAccount('Gsmasha', 10000)
 
s2 = BankAccount('Dolce', 10)
 
s1.display()
s2.display()
 
s1.withdraw(100)
s2.deposit(500)
 
s1.display()
s2.display()

from abc import ABC , abstractmethod

class Customer() : 
    def __init__(self , name , email) : 
        self.name = name 
        self.__email = email 
        
        
        
    def display_info(self) :  
        return f"Name : {self.name} , Email : {self.__email}"
        
        
        
class Account(ABC) : 
    def __init__(self , account_number, owner , balance) :
        self.account_number = account_number 
        self.owner = owner 
        self._balance = balance
        
        
    def deposit(self , amount): 
        if amount <= 0 : 
            return "The amound should be positive." 
          
        try : 
            self._balance += amount 
        except TypeError : 
            return "cant add amount "

    @abstractmethod
    def withdraw(self, amount): 
        pass
        
    
    @property
    def balance(self): 
        return self._balance
        
        
    
    def __str__(self) : 
        return f"Account {self.account_number} | {self.owner.name} | Balance : {self._balance} DH"
        
    


class SavingsAccount(Account) : 
    
    def __init__(self , account_number, owner , balance, interest_rate) : 
        
        super().__init__(account_number, owner , balance)
        self.interest_rate = interest_rate
        
        
        
    def add_interest(self) : 
        if self.interest_rate < 0 : 
            return "you cant add an interest rate"
        
    
        self._balance *= (1 + self.interest_rate)
        
    
    def withdraw(self, amount) : 
        if  amount > self.balance : 
            return f"You cant withdraw this amount . "
        if  amount < 0 : 
            return "You cant withdraw a negative number . "
                
                
        try : 
            self._balance -= amount 
                    
        except TypeError : 
            return "Enter a valid number . "
                   
    
    
    
class CheckingAccount(Account) : 
    max_limit_under_Zero = -100
    def __init__(self ,account_number, owner , balance ):
        
        super().__init__(account_number, owner , balance)
        
    
    
    def withdraw(self , amount) : 
        cls = self.__class__
        if amount > self._balance and (self._balance - amount) > cls.max_limit_under_Zero: 
            self._balance -= amount 
            
    
    
    
    
class Bank() : 
    
    def __init__(self) : 
        self.accounts = list()
        
        
    def add_account(self, account:Account) : 
        self.accounts.append(account)
        
    
    def remove_account() : 
        pass
   

    
    def find_account(): 
        pass


    def show_accounts(self): 
        for account in self.accounts : 
            print(account)






customer = Customer("Amine", "amine@example.com")

savings = SavingsAccount(
    "SA001",
    customer,
    5000,
    0.05
)

checking = CheckingAccount(
    "CA001",
    customer,
    2000
)

bank = Bank()

bank.add_account(savings)
bank.add_account(checking)

savings.deposit(1000)
savings.add_interest()

checking.withdraw(2500)

bank.show_accounts()

## we can use __eq__() and return the account balance == other balance . and when comparing two account we will see if they have same balance . 
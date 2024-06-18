class Account:
    def __init__(self, account_holder, account_number, balance):
           self.account_holder=account_holder
           self.account_number=account_number 
           self.balance=balance

    def deposit(self,amount):
          self.balance += amount  
          print(f"{self.account_holder} deposits ${amount}.\nThe cuurent balance is : {self.balance} ")      

    def withdraw(self,amount):
          if self.balance >= amount:
              self.balance -= amount  
              print(f"{self.account_holder} withdraw ${amount}.\nThe current balance is : {self.balance}")      
          else:  
             print("You do not have enough amount to withdraw.")      

    def get_balance(self):
            return self.balance

    def __str__(self):
         return (f"Account Holder: {self.account_holder},"
                f"Account Number: {self.account_number},"
                f"Current Balance: {self.balance}")


class Bank:
     def __init__(self):
          self.accounts=[]

     def add_account(self,account): 
           self.accounts.append(account)
           print(f"Account for {account.account_holder} added successfully.") 

     def find_account(self,account_number):  
          for account in self.account:
               if account.account_number== account_number:
                    return account
               else:
                    print("Account not found")
               return None        
           
     def list_accounts(self):
           if not self.accounts:
            print("No accounts in the bank.")
           else:
            for account in self.accounts:
                print(account)  


if __name__ == "__main__":
 bank= Bank()                
 acc1 = Account("Smith", "659403", 1000)
 acc2 = Account("John", "269060", 5000)
 acc3 = Account("David", "935420", 7000)

 print("\nDetails of added accounts:")
 bank.add_account(acc1)
 bank.add_account(acc2)
 bank.add_account(acc3)


 #Perform Transcations
 print("\nCurrent Account Details:")
 acc1.deposit(1200)
 acc2.withdraw(1000)
 acc3.deposit(2000)

 print(f"\n{acc1.account_holder} new_balance: {acc1.get_balance()}")
 print(f"{acc2.account_holder} new_balance: {acc2.get_balance()}")
 print(f"{acc3.account_holder} new_balance: {acc3.get_balance()}")
 print("\nList of All Bank Accounts:")
 bank.list_accounts()



from datetime import datetime
from Saving_account import SavingAccount
from Current_Account import CurrentAccount
from CustomerClass import Customer
from TransactionClass import Transaction
import os
import json

#saving the customer information in a file
def save_customers(customers):
    with open ("customer.txt", "w") as file:
        for customer in customers:
            file.write(f"{customer.name}, {customer.address},{customer.contact_info}\n")

#load customer information from the files
def load_customers():
    if not os.path.exists("customers.txt"):
        return []
    customers = []
    
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                customer_data = line.strip().split(',')
                customer = Customer(customer_data[0], customer_data[1], customer_data[2])
    except IOError as e:
        print(f"error loading customer:{e}")


# Save saving account information to file
def save_saving_accounts (accounts):
    try:
      with open ('saving_accounts.txt', 'w') as file:
         for account in accounts:
             if isinstance(account, SavingAccount):
                 file.write(f"{account.account_number},{account.balance},{account.customer}\n")
    except IOError as e:
        print(f"Error saving saving_accounts: {e}")


# Load saving account information from file
def load_saving_accounts(customers):
   if not os.path.exists('saving_accounts.txt'):
         return []
   accounts = []
   try:
      with open('saving_accounts.txt', 'r') as file:
           for line in file:
               account_data = line.strip().split(',')
               customer = next((c for c in customers if c.name == account_data[2]), None)
               if customer:
                    account = SavingAccount(account_data[0], float(account_data[1]), customer)
                    accounts. append (account)
                    customer. add_account(account)
   except IOError as e:
       print(f"Error loading saving_accounts: {e}")
   return accounts
# Save current account information  in a file
def save_current_accounts(accounts) :
   try:
      with open ("current_accounts.txt", "w") as file:
          for account in accounts:
              if isinstance (account, CurrentAccount):
                    file.write(f"{account.account_number}, {account.balance}, {account.customer},{account.overdrawLimit}")
   except  IOError as e:
      print(f"Error saving current _account")

#load information from a file
def load_current_accounts(customers):
    if not os.path.exists ("Current_accounts.txt"):
        return[]
    accounts = []
    try:
        with open ("current_accounts.txt", "r") as file:
            for line in file:
                account_data = line.strip().split(',')
                customer = next((c for c in customers if c.name == account_data[2]), None)
                if customer:
                    account = CurrentAccount (account_data[0], float(account_data[2]), float(account_data[2]))
                    accounts.append(account)
    except IOError as e:
        print(f"Error loading current _accounts: {e}")
    return accounts
#save transaction in a file
def save_tranaction(transaction):
    try:
        next_id=1
        if os.path.exists("transaction.txt"):
           with open ("transaction.txt", "r") as  file:
               lines= file.readlines()
               if lines:
                   last_line= lines[-1].strip()
                   if last_line:
                       next_id=int(last_line.split(",")[0])+1
                       
        with open ("transaction.txt","r") as file:
            for transaction in transaction:
                transaction.transaction_id=next_id
                next_id += 1
                file.write(f"{transaction.tranaction_id},{transaction.timestamp},{transaction.account.account_number}")

    except IOError as e:
        print(f"error saving transaction; {e}")


#load transsaction information from a file
def load_transactions(account):
     if not os.path.exists("transaction.txt"):
         return[]
     transactions= []
     try:
         with open ("transaction.txt","r") as  file:
            for line in file:
                transaction_data = line.strip().split(',')
                account= next((a for a in account if a.account_number == transaction_data[1]), None)
                if account:
                    transaction = Transaction(
                        int(transaction_data[0]),
                        account,
                        transaction_data[2],
                        float(transaction_data[3])
                    )
                    transaction.timestamp = datetime.fromisformat(transaction_data[4])
                    transaction.append(transaction)
     except IOError as e:
         print(f"Error loading transaction : {e}")
     return transactions

                
 

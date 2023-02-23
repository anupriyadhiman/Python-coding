#Build a banking system which has the following functionalities :: 
# 2.1 Add account for a new user 
# 2.2 Add money to the account 
# 2.3 Withdraw money from the account 
# 2.4 Display balance for a particular user

def account_add():
    name = str(input("Enter the name of the user: "))
    account_no = int(input("Enter the account number: "))
    balance = int(input("Enter balance: "))
    account_info = {
        "name": name,
        "account_no": account_no,
        "balance": balance
    }
    return account_info

def add_money(account_info):
    money_deposit = int(input("Enter the amount to be added: "))
    account_info["balance"] = account_info["balance"] + money_deposit
    return account_info

def withdraw_money(account_info):
    wdrw_money = int(input("Enter the amount need to be withdrawn:"))
    account_info["balance"] = account_info["balance"] - wdrw_money
    return account_info

def display(account_info):
    print("Name:", account_info["name"])
    print("Account number:", account_info["account_no"])
    print("Balance:", account_info["balance"])

def main():
    account_info = account_add()
    while True:
        print("1. Add account for a new user")
        print("2. Add money to the account")
        print("3. Withdraw money from the account")
        print("4. Display balance for a particular user")
        print("5. Exit")    
        choice = int(input("Enter your choice: "))
        if choice == 1:
            account_add()
        elif choice == 2:
            add_money(account_info)
        elif choice == 3:
            withdraw_money(account_info)
        elif choice == 4:
            display(account_info)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
        main()
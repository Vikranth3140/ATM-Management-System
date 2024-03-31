from services.account_service import create_account, get_account, deposit, withdraw

def main_menu():
    print("\nATM Management System")
    print("1. Create new account")
    print("2. Check account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        pin = input("Enter PIN: ")
        create_account(name, pin)
        print("Account created successfully!")
        
    elif choice == '2':
        account_id = int(input("Enter account ID: "))
        account = get_account(account_id)
        if account:
            print(f"Account Details: ID {account['account_id']}, Name {account['name']}, Balance {account['balance']}")
        else:
            print("Account not found.")
            
    elif choice == '3':
        account_id = int(input("Enter account ID: "))
        amount = float(input("Enter amount to deposit: "))
        if deposit(account_id, amount):
            print("Deposit successful.")
        else:
            print("Deposit failed.")
            
    elif choice == '4':
        account_id = int(input("Enter account ID: "))
        amount = float(input("Enter amount to withdraw: "))
        if withdraw(account_id, amount):
            print("Withdrawal successful.")
        else:
            print("Insufficient funds or account not found.")
            
    elif choice == '5':
        exit()

if __name__ == "__main__":
    while True:
        main_menu()
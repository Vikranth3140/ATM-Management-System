from services.account_service import create_account, get_account, deposit, withdraw, search_account, list_all_accounts

def main_menu():
    print("\nATM Management System")
    print("1. Create new account")
    print("2. Check account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Search for an account")
    print("6. Display all accounts")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        pin = input("Enter PIN: ")
        account_id = create_account(name, pin)
        print(f"Account created successfully! Account ID is {account_id}")

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
        name = input("Enter account name to search: ")
        accounts = search_account(name)
        for account in accounts:
            print(f"ID: {account['account_id']}, Name: {account['name']}, Balance: {account['balance']}")

    elif choice == '6':
        accounts = list_all_accounts()
        for account in accounts:
            print(f"ID: {account['account_id']}, Name: {account['name']}, Balance: {account['balance']}")

    elif choice == '7':
        exit()

if __name__ == "__main__":
    while True:
        main_menu()
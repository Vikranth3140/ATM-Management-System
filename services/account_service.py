from db.database import get_db_connection

def create_account(name, pin):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO accounts (name, pin, balance) VALUES (%s, %s, 0)", (name, pin))
    db.commit()
    cursor.close()
    db.close()

def get_account(account_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM accounts WHERE account_id = %s", (account_id,))
    account = cursor.fetchone()
    cursor.close()
    db.close()
    return account

def update_balance(account_id, amount):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + (%s) WHERE account_id = %s", (amount, account_id))
    db.commit()
    cursor.close()
    db.close()

def withdraw(account_id, amount):
    account = get_account(account_id)
    if account and account['balance'] >= amount:
        update_balance(account_id, -amount)
        return True
    return False

def deposit(account_id, amount):
    if amount > 0:
        update_balance(account_id, amount)
        return True
    return False
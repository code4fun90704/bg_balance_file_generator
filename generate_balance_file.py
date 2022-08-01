from account import Account
account = Account()

def generate_balance_file():
    new_bal = account.get_balance()
    with open("balance.txt", "w") as f:
        f.write(str(new_bal))
# from teste.bank.bank_functions import account_withdraw, account_deposit


def account_withdraw(account, tax=0.5):
    value = float(input('Enter the amount to withdraw Mr. or Mrs.: '))
    if value <= account['balance']:
        account['balance'] = account['balance'] - (value + tax)
        print(f'New balance: {account["balance"]}')
    else:
        print(f' Insufficient balance to withdraw')
    return account


def account_deposit(account):
    value = float(input(f'Enter the amount to deposit Mr. or Mrs. {account["name"]} : '))
    account['balance'] = account['balance'] + value
    print(f'New balance: {account["balance"]}')
    return account


account = {'accountNumber:': 12345, 'name': "Jane Doe", 'balance': 1200.00}
bank_exit = False
normal_tax = 0.1

while not bank_exit:
    mode = input("Choose a mode: W = withdraw or D = deposit ")
    if mode.lower() == "w":
        account_withdraw(account, normal_tax)
        # account_withdraw()  with the already set value of 0.5 if no tax value is passed
    if mode.lower() == "d":
        account_deposit(account)
    else:
        exit_choice = input("Would you like to exit? Y or N ")
        if exit_choice.lower() == 'y':
            bank_exit = True

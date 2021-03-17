def account_withdraw(account,tax=0.5):
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
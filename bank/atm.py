import account_func

account = account_func.Account('1234-5', 'Jane Doe', 0.00, 50000)
other_account = account_func.Account('4234-4', 'John Doyle', 0.00, 20000)
bank_exit = False

while not bank_exit:
    print(f'Welcome Mr. Mrs. {account.name}')
    account.display_balance()
    mode = input("Choose a mode: W = withdraw, D = deposit  or T - Transfer \n")
    if mode.lower() == "d":
        deposit_value = float(input('Inform the amount to deposit into your own account:'))
        if account.deposit(deposit_value):
            print(f'Depositing the amount: {deposit_value}')
        else:
            print('Error - Service Unavailable')
        print(f'New balance:  {account.balance}')
    if mode.lower() == "w":
        withdraw_value = float(input('Inform the amount to withdraw from your own account:'))
        if account.withdraw(withdraw_value):
            print(f'Withdrawing the amount: {withdraw_value}')
        else:
            print('Insufficient Balance')
        print(f'Balance:  {account.balance}')
    if mode.lower() == "t":
        transfer_value = float(input('Inform the amount to transfer to another account: '))
        if account.transfer(transfer_value, other_account):
            print(f'Transfer sucessful into account: {other_account.number} value: {transfer_value}')
    else:
        exit_choice = input("Would you like to exit? Y or N ")
        if exit_choice.lower() == 'y':
            bank_exit = True

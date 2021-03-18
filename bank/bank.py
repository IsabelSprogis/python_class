import bank.bank_functions
account = {'accountNumber:': 12345, 'name': "Jane Doe", 'balance': 1200.00}
bank_exit = False
normal_tax = 0.1

while not bank_exit:
    mode = input("Choose a mode: W = withdraw or D = deposit ")
    if mode.lower() == "w":
        bank.account_withdraw(account, normal_tax)
        # account_withdraw()  with the already set value of 0.5 if no tax value is passed
    if mode.lower() == "d":
        bank.account_deposit(account)
    else:
        exit_choice = input("Would you like to exit? Y or N ")
        if exit_choice.lower() == 'y':
            bank_exit = True

import checking_account
import savings_account


account = checking_account.Account('1234-5', 'Jane Doe', 0.00, 50000)
savings = savings_account.Account('1234-5', 'Jane Doe', 100000.00, 200000000, 'checking')
other_account = checking_account.Account('4234-4', 'John Doyle', 0.00, 20000, 'savings')
bank_exit = False

print(checking_account.Account.get_acc_qty())

while not bank_exit:
    # account.print_dir()  printa atributos e metodos da classe
    print(f'Welcome Mr. Mrs. {account.name}')
    account.display_balance()
    mode = input("Choose a mode: W = withdraw, D = deposit, T - Transfer or R - refresh \n")
    if mode.lower() == "d":
        deposit_value = float(input('Inform the amount to deposit into your own account:'))
        if account.deposit(deposit_value):
            print(f'Depositing the amount: {deposit_value}')
        else:
            print('Error - Service Unavailable')
        print(f'New balance:  {account.get_balance()}')
    elif mode.lower() == "w":
        withdraw_value = float(input('Inform the amount to withdraw from your own account:'))
        if account.withdraw(withdraw_value):
            print(f'Withdrawing the amount: {withdraw_value}')
        else:
            print('Insufficient Balance')
        print(f'Balance:  {account.get_balance()}')
    elif mode.lower() == "t":
        transfer_value = float(input('Inform the amount to transfer to another account: '))
        if account.transfer(transfer_value, other_account):
            print(f'Transfer sucessful into account: {other_account.number} value: {transfer_value}')
    elif mode.lower() == "r":
        print(account.refresh(0.01))
        print(savings.refresh(0.05))
    else:
        exit_choice = input("Would you like to exit? Y or N ")
        if exit_choice.lower() == 'y':
            bank_exit = True

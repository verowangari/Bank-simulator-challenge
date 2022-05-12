# With initial balances 0
BALANCES = {'Wanjiru':0, 'Juma':0, 'Linda':0}

def bank_program():
    # Reading the input file
    with open('Input_Text.txt', 'r') as logs:
        data = logs.readlines()
        account_logs = []
        for logs in data:
            log = logs.split(':') # Split with a :
            account_logs.append(log) 
        
        for log in account_logs:
            if log[0] == 'DEPOSIT':
                if log[1] in BALANCES:
                    # float for decimal numbers
                    amount = float(BALANCES[log[1]]) + float(log[2])
                    BALANCES[log[1]] = amount
                    print('Deposit successful:', BALANCES)

            elif log[0] == 'WITHDRAW' and log[1] in BALANCES:
                if float(BALANCES[log[1]]) >= float(log[2]):
                    amount = float(BALANCES[log[1]]) - float(log[2])
                    BALANCES[log[1]] = amount
                    print('Withdrawal was successful:', BALANCES)
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
                else:
                    print('There is insufficient balance:', BALANCES)
            elif log[0] == 'TRANSFER' and log[1] in BALANCES and log[2] in BALANCES:
                if float(BALANCES[log[1]]) >= float(log[3]):
                    BALANCES[log[1]] = float(BALANCES[log[1]])-float(log[3])
                    BALANCES[log[2]] = float(BALANCES[log[2]])+float(log[3])
                    print('The transfer successful:', BALANCES)
                else:
                    print('Insufficient balance:', BALANCES)
        print("\n")
        print('The final Account balances: ',BALANCES)
        return BALANCES

bank_program()
    
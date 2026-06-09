balance = 1500

while True:
    choice = int(input("***Enter Your Choice***"\
                       "\n 1.Check Balance"\
                       "\n 2.Deposit"\
                       "\n 3.Withdraw"\
                       "\n 4.Exit : "))
    if(choice == 1):
        print("==================================")
        print("Current Balance :",balance)
        print("==================================")
    elif(choice == 2):
        deposit_amt = int(input("Enter amount you want to deposit : "))
        if(deposit_amt > 0):
            balance += deposit_amt
            print("==================================")
            print(deposit_amt,"Amount Successfully Deposit In Account")
            print("==================================")
        else:
            print("==================================")
            print("Enter Valid Amount")
            print("==================================")
    elif(choice == 3):
        withdraw_amt = int(input("Enter amount you want to withdraw : "))
        if(withdraw_amt > 0):
            if(withdraw_amt > balance):
                print("==================================")
                print("Insufficient Funds!!!")
                print("==================================")
            else:
                balance -= withdraw_amt
                print("==================================")
                print(withdraw_amt,"Amount Successfully Withdraw From Account")
                print("==================================")
        else:
            print("==================================")
            print("Please Withdraw Valid Amount!")
            print("==================================")
    elif(choice == 4):
        break
    else:
        print("==================================")
        print("Incorrect Choice!!!")
        print("==================================")
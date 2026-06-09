# Build a simple calculator

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = int(input("*** Enter your operator ***"\
           "\n 1.Addition "\
           "\n 2.Subtraction "\
           "\n 3.Multiplication "\
           "\n 4.Division :- "))
if(op == 1):
    add = num1 + num2
    print("=========================")
    print("Addition of",num1,"and",num2,"=",add)
    print("=========================")
elif(op == 2):
    sub = num1 - num2
    print("=========================")
    print("Subtraction of",num1,"and",num2,"=",sub)
    print("=========================")
elif(op == 3):
    mul = num1 * num2
    print("=========================")
    print("Multiplication of",num1,"and",num2,"=",mul)
    print("=========================")
elif(op == 4):
    if(num2 != 0):
        div = num1 / num2
        print("=========================")
        print("Division of",num1,"and",num2,"=",div)
        print("=========================")
    else:
        print("=========================")
        print("Value Should Be Greater Than 0")
        print("=========================")
else:
    print("=========================")
    print("Incorrect Choice For Operator")
    print("=========================")
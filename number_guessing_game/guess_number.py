# Build A Simple Number Guessing Game

attempt = 0
while True:
    user_number = int(input("Enter Number : "))
    attempt += 1
    secret_number = 45
    if(user_number == secret_number):
        print("====================")
        print("Correct Guessing!")
        print("After",attempt,"attempt you guess correct number!")
        break
    elif(user_number < secret_number):
        print("====================")
        print("Too Low!")
    elif(user_number > secret_number):
        print("====================")
        print("Too High!")
    print(attempt,"attempts Done!")

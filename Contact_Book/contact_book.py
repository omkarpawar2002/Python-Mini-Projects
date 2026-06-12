# Build A Contact Book Application :
"""
Create a Contact Book application that stores and manages contacts using a dictionary.
"""

contacts = {}

while True:
    choice = int(input("***ENTER CHOICE***"\
                       "\n 1.ADD CONTACT "\
                       "\n 2.SEARCH CONTACT "\
                       "\n 3.UPDATE CONTACT "\
                       "\n 4.DELETE CONTACT "\
                       "\n 5.SHOW ALL CONTACTS "\
                       "\n 6.TOTAL CONTACTS "\
                       "\n 7.EXIT :- "))
    if(choice == 1):
        numbers = int(input("Enter how many contacts you want to add :- "))
        print("========================")
        for i in range(numbers):
            name = input("Enter your name :- ").lower()
            if(name not in contacts):
                contact_number = int(input("Enter your contact number :- "))
                contacts[name] = str(contact_number)
            else:
                print("========================")
                print(f"{name} Already Exists")
                print("========================")
                break
    elif(choice == 2):
        name = input("Search contact name :- ").lower()
        if(name in contacts):
            print("========================")
            print(f"Name : {name}\nContact : {contacts[name]}")
            print("========================")
        else:
            print("========================")
            print("Contact Not Found")
            print("========================")
    elif(choice == 3):
        name = input("Enter name :- ").lower()
        if(name in contacts):
            new_number = int(input("Enter New Number :- "))
            contacts[name] = str(new_number)
        else:
            print("========================")
            print("Can Not Found In Contacts")
            print("========================")
    elif(choice == 4):
        name = input("Enter name :- ").lower()
        if(name in contacts):
            print("========================")
            contacts.pop(name)
            print(f"{name} Deleted Successfully!!")
            print("========================")
        else:
            print("========================")
            print("Can Not Found In Contacts")
            print("========================")
    elif(choice == 5):
        print("========================")
        for name,contact in contacts.items():
            print(f"Name : {name}\nContact : {contact}")
        print("========================")
    elif(choice == 6):
        print("========================")
        print(f"Total Contacts : {len(contacts)}")
        print("========================")
    elif(choice == 7):
        print("========================")
        print("Thank You For Using Contact Book!!!")
        print("========================")
        break
    else:
        print("========================")
        print("Incorrect Choice!!")
        print("========================")
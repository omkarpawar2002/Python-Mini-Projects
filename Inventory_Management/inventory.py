"""
Inventory Management System : 
Create a Python application to manage products and their stock information.
"""

inventory = []
while True:
    choice = int(input("***ENTER YOUR CHOICE***"\
                       "\n 1.ADD PRODUCT "\
                       "\n 2.VIEW PRODUCT "\
                       "\n 3.REMOVE PRODUCT "\
                       "\n 4.VIEW ALL PRODUCTS "\
                       "\n 5.UPDATE STOCK "\
                       "\n 6.TOTAL PRODUCTS "\
                       "\n 7.EXIT :- "))
    if(choice == 1):
        numbers = int(input("Enter how many items you want to buy :- "))
        for item in range(numbers):
            product = {}
            print("===================")
            product_id = int(input("Enter Product Id :- "))
            product_name = input("Enter Product Name :- ")
            product_price = float(input("Enter Product Price :- "))
            stock_quantity = int(input("Enter how many stocks you want :- "))
            product.update({"product_id":product_id,"product_name":product_name,"product_price":product_price,"stock":stock_quantity})
            inventory.append(product)
    elif(choice == 2):
        if(inventory):
            check_id = int(input("Enter Id :- "))
            for product in inventory:
                if(check_id == product["product_id"]):
                    print("===================")
                    for key,value in product.items():
                        print(f"{key.title()} = {value}")
                    break
                else:
                    continue
            else:
                print("===================")
                print("No Match Found To View Product!!")                    
                print("===================")                    
        else:
            print("===================")
            print("No Product Available While Searching!!")
            print("===================")
    elif(choice == 3):
        if(inventory):
            check_id = int(input("Enter Id :- "))
            for product in inventory:
                if(check_id == product["product_id"]):
                    print("===================")
                    inventory.remove(product)
                    print("Product Remove Successfully From Inventory!!")
                    print("===================")
                    break
                else:
                    continue
            else:
                print("===================")
                print("No Match Found While Deleting!!")                    
                print("===================")                    
        else:
            print("===================")
            print("No Product Available To Delete!!")
            print("===================")
    elif(choice == 4):
        if(inventory):
            for product in inventory:
                print("===================")
                for key,value in product.items():
                    print(f"{key.title()} = {value}")
        else:
            print("===================")
            print("Inventory Is Empty!!")
            print("===================")
    elif(choice == 5):
        if(inventory):
            check_id = int(input("Enter Id :- "))
            for product in inventory:
                if(check_id == product["product_id"]):
                    update_stock = int(input("How many stocks you want :- "))
                    product["stock"] = update_stock   
                    print("===================")
                    print("Stock Updated Successfully!!")                    
                    print("===================")                     
                    break
                else:
                    continue
            else:
                print("===================")
                print("No Match Found While Updating Stock!!")                    
                print("===================")                    
        else:
            print("===================")
            print("No Product Available For Update!!")
            print("===================")
    elif(choice == 6):
        print("===================")
        print(f"Total Products Available In Inventory = {len(inventory)}")
        print("===================")
    elif(choice == 7):
        print("===================")
        print("Thank You For Visiting Out Inventory!!!")
        print("===================")
        break
    else:
        print("===================")
        print("Incorrect Choice!!")
        print("===================")
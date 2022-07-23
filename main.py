# import dbOperation
import adminMenu1

noExit = True

while noExit:
    print("\nChoose an option for login \n 1-Admin \n 2-Customer \n 3-Exit")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print('\nWrong selection!! Try again.')
        continue

    if choice == 2:
        print("Welcome to Logistic System.")  # remove this after adding code for customer
        list_item = ["T-shirt", "Pents", "Jackets", "Shoose", "Tracks"]  # after databse
        while True:
            print("what you want to buy:")
            for item_index in range(len(list_item)):
                print(item_index, "  " , list_item[item_index])  # print from dartabase
            choose = input("what you want to buy:")
            quantity = input("how much you wnat to buy")
            if choose == 0:
                break

            # -----------check for quanity in database

    if choice == 3:
        print("Exit")
        noExit = False
    else:
        loginId = input("Enter login Id: ").lower()
        password = input("Enter password: ")
        # user = dbOperation.checkLoginId(loginId)
        # user = adminOperations.checkLoginId(loginId) # generic function can go in a different py file?

        user = True #to pass the validation

        if not user:  # User not found
            print('User not found!')
        elif choice == 1:  # admin(1)
            adminMenu1.adminMenu()
        else:  # customer(2)
            print("ucgb")








                #customer_input=input("what you would buy : 1) T-shirt \n2) Pents \n3) Jackets \n4) Shoose \n 5) Tracks \n\n Press 0 for EXIT")
                # if customer_input == 0:
                #     choose = 1
                #     continue
                # if customer_input == 1:
                #     quantity = input("Insert how many t-shirt you would buy :")
                #     if quantity > total_item1 :
                #         print("sorry product is not available ")
                # if customer_input == 1:
                #     quantity = input("Insert how many t-shirt you would buy :")
                #     if quantity > total_item1 :
                #         print("sorry product is not available ")

        #   Create new file, import and call function here to display the customer options
# import dbOperation
import adminMenu1
import customerOperations

noExit = True

while noExit:
    print("\nChoose an option for login \n 1-Admin \n 2-Customer \n 3-Exit")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print('\nWrong selection!! Try again.')
        continue

    if choice == 2:
        print("Welcome to Logistic System.")
        list_item = ["T-shirt", "Pents", "Jackets", "Shoose", "Tracks"]  # fetch databse
        cart = []
        while True:
            print("what you want to buy:")
            for item_index in range(len(list_item)):
                print(item_index, "  " , list_item[item_index])
            choose = int(input("what you want to buy:"))
            quantity = int(input("how much you wnat to buy"))
            customerOperations.add_to_cart(cart,choose,quantity)
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

        #   Create new file, import and call function here to display the customer options
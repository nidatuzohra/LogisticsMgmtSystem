# import dbOperation
import adminMenu1
import customerOperations
import customer

noExit = True

while noExit:
    print("\nChoose an option for login \n 1-Admin \n 2-Customer \n 3-Exit")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print('\nWrong selection!! Try again.')
        continue

    if choice == 2:
       customer.customer()

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
            print(" ")

import adminOperations
import adminMenu
import customerOperations
import customer

noExit = True

while noExit:
    print("\nChoose an option for login \n 1-Admin \n 2-Customer \n 3-Exit")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print('\nWrong selection!! Try again.', ValueError)
        continue

    if choice == 3:
        print("Exit")
        noExit = False

    elif choice == 1 or choice == 2:
        loginId = input("Enter login Id: ").lower()
        password = input("Enter password: ")
        user = adminOperations.check_login_id(loginId)

        if not user:  # User not found
            print('User not found!')
        else:
            userAuth = adminOperations.checkPswd(loginId, password, choice)
            if userAuth:
                if choice == 1:  # admin(1)
                    adminMenu.adminMenu()
                else:  # customer(2)
                    customer.customer(loginId)
            else:
                print('Wrong password!')


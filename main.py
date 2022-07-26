import adminOperations
import adminMenu

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
    else:
        loginId = input("Enter login Id: ").lower()
        password = input("Enter password: ")
        user = adminOperations.check_login_id(loginId)
        print("user", user)

        if not user:  # User not found
            print('User not found!')
        else:
            userAuth = adminOperations.checkPswd(loginId, password)
            if(userAuth):
                if choice == 1:  # admin(1)
                    adminMenu.adminMenu()
                else:  # customer(2)
                    print("Show customer options")  # remove this after adding code for customer
                #   Create new file, import and call function here to display the customer options
            else:
                print('Wrong password!')

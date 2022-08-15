import adminOperations
import adminMenu
import customer

noExit = True

while noExit:
    print('*****     ================\                 *****')
    print('*****     |----------||@  \\\   ___          *****')
    print('*****     |____|_____|||_/_\\\_|___|_        *****')
    print('*****     <|  ___\    ||     | ____  |      *****')
    print('*****     <| /    |___||_____|/    | |      *****')
    print('*****     ||/  O  |__________/  O  |_||     *****')
    print('*****        \___/ DASH BOARD \___/         *****')
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

        if not user:  # User not found
            print('User not found!')
        else:
            userAuth = adminOperations.checkPswd(loginId, password, choice)
            if userAuth:
                if choice == 1:  # admin(1)
                    print('\n      __               \n /\  |  \  |\/| | |\ | \n/~~\ |__/  |  | | | \| ')
                    adminMenu.adminMenu()
                else:  # customer(2)
                    print('\n __        __  ___  __         ___  __  \n/  ` |  | /__`  |  /  \  |\/| |__  |__) ')
                    print('\__, \__/ .__/  |  \__/  |  | |___ |  \ ')
                    customer.customer(loginId)
            else:
                print('Wrong password!')


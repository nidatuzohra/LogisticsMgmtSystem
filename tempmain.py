import dbOperation
import encryptPassword

noExit = True

while noExit:
    print("\nChoose an option \n 1-SignUp \n 2-Login \n 3-Exit")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print('\nWrong selection!! Try again.')
        continue

    if choice == 3:
        print("Exit")
        noExit = False
    else:
        loginId = input("Enter login Id: ").lower()
        password = input("Enter password: ")
        user = dbOperation.checkLoginId(loginId)

        if choice == 1 and user:        # SignUp and user found
            print('User already exist!')
        elif choice == 2 and not user:  # Login and user not found
            print('User not found!')
        else:
            if choice == 1:             # SignUp and user not found
                encPws = encryptPassword.encrypt(password)
                dbOperation.saveInDB(loginId, encPws)
            else:                       # Login and user found
                encPws = encryptPassword.encrypt(password)
                checkPswd = dbOperation.checkPswd(loginId, encPws)
                if not checkPswd:  # wrong password
                    print('Wrong password!')
                else:  # correct password
                    dbOperation.updateInDB(loginId, encPws)

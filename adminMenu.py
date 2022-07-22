import dbOperation


def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("User input is Number")
    else:
        print("User input is string")


noExit = True

while noExit:
    print("\nChoose an option for login \n 1-Admin \n 2-Customer \n 3-Exit")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print('\nWrong selection!! Try again.')
        continue

    if choice == 3:
        print("Exit")
        noExit = False
    else:
        # loginId = input("Enter login Id: ").lower()
        # password = input("Enter password: ")
        # user = dbOperation.checkLoginId(loginId)
        # user = adminOperations.checkLoginId(loginId) # generic function can go in a different py file?

        if choice == 0:  # User not found
            print('User not found!')
        elif choice == 1:  # admin(1)
            noExit = True
            while noExit:
                print(
                    "\nChoose an option  \n 11-Add Product \n 22-Update product Quantity \n 33-Add Vehicle \n 44-Add Location \n 55-Generate Reports \n 66-Main menu")
                try:
                    choice = int(input("Select an option: "))
                except ValueError:
                    print('\nWrong selection!! Try again.')
                    continue

                if choice == 11:  # admin(11)
                    print("You have selected Add Product option")
                    print("***ADD PRODUCT***")
                    error_entry = True
                    while error_entry:
                        try:
                            Name = input(" Enter Product Name: ")
                            Name = Name.strip().lower()
                            Name = str(Name)
                            if Name != '':
                                try:
                                    Price = input(" Enter Price: ")
                                    Price = float(Price)
                                    Quantity = input(" Enter Quantity: ")
                                    Quantity = int(Quantity)
                                except ValueError:
                                    print("Provide appropriate value")
                                    continue
                            else:
                                print("Provide appropriate value")
                                continue
                        except ValueError:
                            print("Provide appropriate value")
                            continue

                        if Price == '' or Quantity == '':
                            print("Provide appropriate value")
                            continue
                        else:
                            dbOperation.save_product(Name, Price, Quantity)
                            error_entry = False
                            break
                elif choice == 22:  # admin(22)
                    print("You have selected Update product Quantity option")
                    print("***Update Product Quantity***")
                    error_entry = True
                    while error_entry:
                        try:
                            Product_Id = input(" Enter Product ID: ")
                            Product_Id = int(Product_Id)
                        except ValueError:
                            print("Provide appropriate value")
                            continue

                        if Product_Id == '':
                            print("Provide appropriate value")
                            continue
                        else:
                            dbOperation.update_product_qty(Product_Id)
                            error_entry = False
                            break

                elif choice == 33:  # admin(33)
                    print("You have selected Add Vehicle option")
                    print("***ADD VEHICLE***")
                    error_entry = True
                    while error_entry:
                        try:
                            Vehicle_Type = input(" Enter Vehicle Name: ")
                            Vehicle_Type = Vehicle_Type.strip().lower()
                            Vehicle_Type = str(Vehicle_Type)
                        except ValueError:
                            print("Provide appropriate value")
                            continue

                        if Vehicle_Type == '':
                            print("Provide appropriate value")
                            continue
                        else:
                            dbOperation.save_vehicle(Vehicle_Type)
                            error_entry = False
                            break

                elif choice == 44:  # admin(44)
                    print("You have selected Add Location option")
                    print("***Add Location***")
                    error_entry = True
                    while error_entry:
                        try:
                            Add_Location = input(" Enter Add Location: ")
                            Add_Location = Add_Location.strip().lower()
                            Add_Location = str(Add_Location)
                        except TypeError:
                            print("Provide appropriate value")
                            continue

                        if Add_Location == '':
                            print("Provide appropriate value")
                            continue
                        else:
                            dbOperation.save_location(Add_Location)
                            error_entry = False
                            break

                elif choice == 55:  # admin(55)
                    print("You have selected Generate report option")
                    print("***Generating report***")
                    dbOperation.generate_report()
                elif choice == 66:  # admin(66)
                    print("You have selected Main Menu option")
                    break
                else:
                    print("Invalid response.Provide appropriate value")
                    continue
        else:  # customer(2)
            print("Show customer options")  # remove this after adding code for customer

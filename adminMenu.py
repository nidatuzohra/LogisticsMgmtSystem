import adminOperations
import re


def adminMenu():
    noAdminExit = True

    while noAdminExit:
        print(
            "\nChoose an option  \n 1-Add Product \n 2-Update product Quantity \n 3-Add Vehicle \n 4-Add Location \n 5-Generate Reports \n 6-Create customer \n 7-Logout")
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print('\nWrong selection!! Try again.')

        if choice == 1:  # admin(1)
            print("You have selected Add Product option")
            print("***ADD PRODUCT***")
            error_entry = True
            while error_entry:
                try:
                    Name = input(" Enter Product Name: ")
                    Name = Name.strip().lower()
                    Name = str(Name)
                except TypeError:
                    print("Provide appropriate value")
                    continue
                check = re.compile(r'[a-zA-Z]*$')
                if check.match(Name) and Name != '':
                    error_entry = False
                    break
                else:
                    print("Provide appropriate value(only characters)")
                    continue

            error_entry1 = True
            while error_entry1:
                try:
                    Price = input(" Enter Price: ")
                    Price = float(Price)
                except ValueError:
                    print("Provide appropriate value")
                    continue

                if Price == ' ':
                    print("Provide appropriate value")
                    continue
                else:
                    error_entry1 = False
                    break

            error_entry2 = True
            while error_entry2:
                try:
                    Quantity = int(input(" Enter Quantity: "))
                except ValueError:
                    print("Provide appropriate value")
                    continue

                if Quantity == '':
                    print("Provide appropriate value")
                    continue
                else:
                    adminOperations.save_product(Name, Price, Quantity)
                    print('%s Products added successfully', Quantity)
                    error_entry2 = False
                    break

        elif choice == 2:  # admin(2)
            # TODO Show all the products here
            print("You have selected Update product Quantity option")
            print("***Update Product Quantity***")
            print("Please select Product ID from Below List")
            prod_list = adminOperations.show_all_product()
            print("ID    ITEMS          PRICE          QUANTITY")
            for i in prod_list:
                print(i[0], " | ", i[1], "          ", i[2], "          ", i[3])
            error_entry3 = True
            while error_entry3:
                try:
                    Product_Id = input(" Enter Product ID: ")
                    Product_Id = int(Product_Id)
                except ValueError:
                    print("Provide appropriate value")
                    continue

                id_check = adminOperations.check_product_id(Product_Id)
                print(id_check)
                if not id_check:
                    print("Id is not present in database")
                    continue
                else:
                    error_entry4 = True
                    while error_entry4:
                        try:
                            Product_Qty = input(" Enter Product Qty: ")
                            Product_Qty = int(Product_Qty)
                        except ValueError:
                            print("Provide appropriate value")
                            continue

                        if Product_Qty == ' ':
                            print("Product quantity cannot be null.")
                            continue
                        else:
                            adminOperations.admin_update_product_qty(Product_Id, Product_Qty)
                            print("Successfully Updated the {0} quantity for Product ID {1}.".format(Product_Qty,
                                                                                                     Product_Id))
                            error_entry3 = False
                            break

        elif choice == 3:  # admin(3)
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
                    adminOperations.save_vehicle(Vehicle_Type)
                    print(" %s is added successfully", Vehicle_Type)
                    error_entry = False
                    break

        elif choice == 4:  # admin(4)
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
                    adminOperations.save_location(Add_Location)
                    print(" %s is added successfully", Add_Location)
                    error_entry = False
                    break

        elif choice == 5:  # admin(5)
            print("You have selected Generate report option")
            print("***Generating report***")
            adminOperations.generate_report()
        elif choice == 6:  # admin(6)
            print("You have selected Create customer option")
            # TODO Create customer
        elif choice == 7:  # admin(7)
            print("Exit, Add logout code")
            noAdminExit = False
        else:
            print("Invalid response.Provide appropriate value")

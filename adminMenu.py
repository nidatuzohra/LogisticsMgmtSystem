import adminOperations
import re
import customerOperations
import utils
import reportsMenu


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

                if Price == ' ' or Price == "0" or Price < 1:
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

                if Quantity == ' ' or Quantity == "0" or Quantity < 1:
                    print("Provide appropriate value")
                    continue
                else:
                    adminOperations.save_product(Name, Price, Quantity)
                    print('{} Product added successfully'.format(Name))
                    error_entry2 = False
                    break

        elif choice == 2:  # admin(2)
            # TODO Show all the products here
            print("You have selected Update product Quantity option")
            print("***Update Product Quantity***")
            print("Please select Product ID from Below List")
            list_item = customerOperations.show_product()
            options = {}
            role = "A"
            utils.print_menu(list_item, options, role)
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

                        if Product_Qty == ' ' or Product_Qty == "0" or Product_Qty < 1:
                            print("Provide appropriate value(>0)")
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
            error_entry5 = True
            while error_entry5:
                try:
                    Vehicle_Type = input(" Enter Vehicle Name: ")
                    Vehicle_Type = Vehicle_Type.strip().lower()
                    Vehicle_Type = str(Vehicle_Type)
                except ValueError:
                    print("Provide appropriate value")
                    continue

                v_check = re.compile(r'[a-zA-Z]*$')
                if v_check.match(Vehicle_Type) and Vehicle_Type != '':
                    adminOperations.save_vehicle(Vehicle_Type)
                    print("{} is added successfully".format(Vehicle_Type))
                    error_entry5 = False
                    break
                else:
                    print("Provide appropriate value(Character only)")
                    continue

        elif choice == 4:  # admin(4)
            print("You have selected Add Location option")
            print("***Add Location***")
            error_entry6 = True
            while error_entry6:
                try:
                    Add_Location = input(" Enter Add Location: ")
                    Add_Location = Add_Location.strip().lower()
                    Add_Location = str(Add_Location)
                except TypeError:
                    print("Provide appropriate value")
                    continue

                Loc_check = re.compile(r'[a-zA-Z]*$')
                if Loc_check.match(Add_Location) and Add_Location != '':
                    adminOperations.save_location(Add_Location)
                    print(" {} is added successfully".format(Add_Location))
                    error_entry6 = False
                    break
                else:
                    print("Provide appropriate value")
                    continue

        elif choice == 5:  # admin(5)
            reportsMenu.showReportsOptions()
            # adminOperations.generate_report()
        elif choice == 6:  # admin(6)
            print("You have selected Create customer option")
            # TODO Create customer
            print("***Create Customer***")
            error_entry7 = True
            while error_entry7:
                try:
                    Email_Id = input(" Enter Email: ")
                    Email_Id = str(Email_Id)
                except ValueError:
                    print("Provide appropriate value")
                    continue

                val_email = re.compile(r'[\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b]*$')
                if not val_email.match(Email_Id):
                    print("Provide a valid email Id(example@gmail.com)")
                    continue
                else:
                    id = adminOperations.check_login_id(Email_Id)
                    if not Email_Id:
                        print("Email Id cannot be blank.")
                    else:
                        if id:
                            print("User is already exist")
                            continue
                        else:
                            error_entry8 = True
                            while error_entry8:
                                try:
                                    Password = input(" Enter Password: ")
                                    Password = str(Password)
                                except TypeError:
                                    print("Provide appropriate value")
                                    continue

                                if not Password:
                                    print("Provide appropriate value")
                                    continue
                                else:
                                    error_entry9 = True
                                    while error_entry9:
                                        try:
                                            Fst_Name = input(" Enter First Name: ")
                                            Lst_Name = input(" Enter Last Name: ")
                                            Fst_Name = str(Fst_Name)
                                            Lst_Name = str(Lst_Name)
                                        except TypeError:
                                            print("Provide appropriate value")
                                            continue

                                        if not Fst_Name or not Lst_Name:
                                            print("Provide appropriate value")
                                            continue
                                        else:
                                            adminOperations.save_customer(Email_Id, Password, Fst_Name, Lst_Name)
                                            print("Customer added successfully {0}.".format(Email_Id))
                                            error_entry7 = False
                                            error_entry8 = False
                                            error_entry9 = False
                                            break

        elif choice == 7:  # admin(7)
            print("Exit, Add logout code")
            noAdminExit = False
        else:
            print("Invalid response.Provide appropriate value")

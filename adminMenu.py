import adminOperations

def adminMenu():
    noAdminExit = True

    while noAdminExit:
        print("\nChoose an option  \n 1-Add Product \n 2-Update product Quantity \n 3-Add Vehicle \n 4-Add Location \n 5-Generate Reports \n 6-Create customer \n 7-Logout")
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
                    if Name != '':
                        try:
                            Price = input(" Enter Price: ")
                            Price = float(Price)
                            Quantity = int(input(" Enter Quantity: "))
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
                    adminOperations.save_product(Name, Price, Quantity)
                    print('Product added')
                    error_entry = False
                    break
        elif choice == 2:  # admin(2)
            #TODO Show all the products here
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
                    # TODO Validate if productId exists or not
                    print("Provide appropriate value")
                    continue
                else:
                    adminOperations.update_product_qty(Product_Id)
                    error_entry = False
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
                    # TODO Show success message
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
                    # TODO Show success message
                    error_entry = False
                    break

        elif choice == 5:  # admin(5)
            print("You have selected Generate report option")
            print("***Generating report***")
            adminOperations.generate_report()
        elif choice == 6:  # admin(6)
            print("You have selected Create customer option")
            # TODO Create customer
            # adminOperations.save_customer('customer@example.com', 'pwd12345', 'John', 'Smith')
        elif choice == 7:  # admin(7)
            print("Exit, Add logout code")
            noAdminExit = False
        else:
            print("Invalid response.Provide appropriate value")
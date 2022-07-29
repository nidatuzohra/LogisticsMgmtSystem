import adminOperations
import customerOperations

def customer():
    print("Welcome to Logistic System.")
    list_item = customerOperations.show_product()
    cart = []
    options = []
    print("\nChoose option \n 1-Select products \n 2-Logout \n")
    cust_choice = int(input('Select an option'))

    custExit = True
    while custExit:
        if cust_choice == 2:
            custExit = False
        else:
            while True:
                print("Id   ITEMS    PRICE   QUANTITY")
                dash = '-' * 33
                print(list_item)
                print(dash)
                for prodItem in (list_item):
                    if prodItem[3] > 0 :
                        # print(idx)
                        print('{:<5d}{:<10s}{:<10.2f}{:<5d}'.format(prodItem[0], prodItem[1], prodItem[2], prodItem[3]))
                        options.append(prodItem[0])
                print(dash)
                correct_option = True
                while correct_option:
                    try:
                        choose = int(input("Enter Item code: "))
                        if choose in options:
                            quantity = int(input("Insert Item Quantity: "))
                            correct_option = False
                        else:
                            print("OPPS!! Please select valid option \n ")
                            continue
                    except ValueError:
                        print("OPPS!! Character value is not allow Please select Integer Number")
                        print("Please, try again \n")
                        continue

                    value_check = customerOperations.add_to_cart(cart, choose, quantity)
                    if value_check == False:
                        print("Sorry, Quantity is not Available")
                        quantity = 0
                        again_buy = input("Would you like to Buy another product? Y/N : ")
                        if (again_buy == 'n' or again_buy == 'N' or again_buy == 'No'):
                            print("Thank You for visit !!")
                            quit()
                        else:
                            again_ask = 0
                            break   # add exit menu
                break_loop = input("\nWould you like to add more? Y/N: ")
                list_item = customerOperations.show_product()
                if(break_loop == 'n' or break_loop == 'N' or break_loop == 'No'):
                    break

            vehicles = customerOperations.show_vehicle()
            print("\nAvailable Transportaion Options\n",dash)
            list_vehicle_no = []
            for vehicle in vehicles:
                print(vehicle[0], " ", vehicle[1])
                list_vehicle_no.append(vehicle[0])
            print(dash)
            selected_vehicle = customerOperations.fetch_value(list_vehicle_no,"Select your delivery mode: ")


            print("\nAvailble countries for Services ")
            country_list = customerOperations.show_location()
            list_country_no = []
            for county in country_list:
                print(county[0], "  ", county[1])
                list_country_no.append(county[0])
            origin_country = customerOperations.fetch_value(list_vehicle_no,"Select Pickup Country: ")
            destination_country = customerOperations.fetch_value(list_vehicle_no,"Select Destination country: ")
            if origin_country == destination_country :
                print("Sorry To inform You, This service only for International")
                quit()

            print("\nPlease Provide Your personal details for order")
            first_name = input("Enter your first name: ")
            last_name = input("Enter Your last name: ")
            contact_no = int(input("Enter your phone Number: "))
            user_id=adminOperations.create_customer_details(first_name,last_name)

            print()
            print("------   LOGISTIC SYSTEM   ------")
            print("Name: ", first_name, " ", last_name)
            print("Contact: ",contact_no)
            total = 0
            cross= 'x' * 33
            print(cross)
            for item in cart:
                print('{:<5d}{:<10s}{:<10.2f}{:<5d}'.format(prodItem[0], prodItem[1], prodItem[2], prodItem[3]))
                total += item[3]
            print(cross)
            print("Total Amount : ",total)
            print("\nyour order is almost done \n \n---------   PAYMENT     ---------")
            pay = int(input("1) credit/debit card \n2) cash on delivery\nHow would you like to Pay:"))
            if pay == 1:
                card_no = int(input("Enter credit or debit card number: "))
            confirm = input("\nPayment Confirm? Y/N : ")

            if (confirm == 'y' or confirm == 'Y' or confirm == 'YES' or confirm == 'Yes'):
                adminOperations.store_order_details(user_id,selected_vehicle, origin_country, destination_country, total)

            if (confirm == 'n' or confirm == 'N' or confirm == 'NO' or confirm == 'no'):
                adminOperations.rollback()

            print("\nOrder is successfully ")
import adminOperations
import customerOperations
import utils

def customer(email_id):
    print("Welcome to Logistic System.")
    print("\nChoose an option \n 1-Select products \n 2-Logout")
    cust_choice = int(input('Select an option: '))
    custExit = True
    while custExit:
        list_item = customerOperations.show_product()
        cart = []
        options = {}
        if cust_choice == 2:
            custExit = False
        else:
            while True:
                utils.print_menu(list_item, options)
                choose = utils.check_value("Enter Item code: ",options)
                quantity = utils.check_value("Insert Item Quantity: ",[])
                product_item = options[choose]
                value_check = customerOperations.add_to_cart(cart, product_item, quantity)

                if value_check == False:
                    print("Sorry, Quantity is not Available\nPlease select Product again")
                    continue

                break_loop = input("\nWould you like to add more? Y/N: ")
                list_item = customerOperations.show_product()
                if(break_loop == 'n' or break_loop == 'N' or break_loop == 'No' or break_loop == 'NO'):
                    break

            vehicles = customerOperations.show_vehicle()
            print("\nAvailable transportation options\n")
            utils.print_dash()
            list_vehicle_no = []
            for vehicle in vehicles:
                print(vehicle[0], " ", vehicle[1])
                list_vehicle_no.append(vehicle[0])
            utils.print_dash()
            selected_vehicle = customerOperations.fetch_value(list_vehicle_no,"Select your delivery mode: ")

            while True:
                print("\nAvailable countries")
                utils.print_dash()
                country_list = customerOperations.show_location()
                list_country_no = []
                for county in country_list:
                    print(county[0], "  ", county[1])
                    list_country_no.append(county[0])
                utils.print_dash()
                origin_country = customerOperations.fetch_value(list_vehicle_no, "Select pickup: ")
                destination_country = customerOperations.fetch_value(list_vehicle_no, "Select destination: ")
                if origin_country == destination_country:
                    print("Sorry pickup and destination can't be same!")
                else:
                    break

            total = utils.print_invoice(cart)

            print("\nYour order is almost done \n \n---------   PAYMENT     ---------")
            confirm = utils.check_value("Would you like to confirm the payment?\n1)YES \n2)NO\nSelect option: ",[1,2])
            if confirm == 1:
                customerOperations.store_order_details(email_id,selected_vehicle, origin_country, destination_country, total)
                print("Transaction successful!!!")
                print("Order has been placed!!!")
                custExit = False
            if confirm == 2:
                customerOperations.rollback_qty(cart)
                print("Transaction failed!")
                print("Thank you visit again!!!")
                custExit = False
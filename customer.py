import  customerOperations

def customer():
    print("Welcome to Logistic System.")
    # list_item = ["T-shirt", "Pents", "Jackets", "Shoose", "Tracks"]  # dictionary add and add database
    list_item = customerOperations.show_product()
    cart = []
    while True:
        print("what you want to buy:")
        print("     ITEMS   PRICE  QUANTITY")
        for item_index in (list_item):
            print(item_index[0], "  ", item_index[1], "  ", item_index[2], "  ", item_index[3])
        choose = input("what you want to buy:")
        quantity = int(input("how much you wnat to buy"))
        # cart.append(choose)   #fatch from databse
        customerOperations.add_to_cart(cart, choose, quantity)
        break_loop = input("would you like to add more? Y/N")
        if(break_loop == 'n' or break_loop == 'N' or break_loop == 'No'):
            break

    vehicles = customerOperations.show_vehicle()
    for vehicle in vehicles:
        print(vehicle[0], "  ", vehicle[1])
    selected_vehicle = input("Select your delivery mode")

    print("Select country number from below list")
    country_list = customerOperations.show_location()
    for county in country_list:
        print(county[0], "  ", county[1])
    send_parsel_country = int(input())

    first_name = input("Enter your first name: ")
    last_name = input("Enter Your last name: ")
    send_parsel_address = input("Address for delivery : ")  # address add?

    print("---------   INVOICE    ------")
    print("Name: ", first_name, " ", last_name)
    print("Address:", send_parsel_address)
    print(cart)
    # for item in range(len(cart)) :
    #     print(item,item[item][1])
    print("your order is almost done \n How would you like to pay:")
    pay = int(input("1)credit/debit card  2) cash on delivery"))
    if pay == 1:
        card_no = int(input("Enter credit or debit card number:"))
    confirm = input("Payment Conform?")
    customerOperations.end_user(confirm)
    print("Order is successfully ")
    customerOperations.end_user(1)
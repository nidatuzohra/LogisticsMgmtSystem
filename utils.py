# Common functions will be defined here
def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("User input is Number")
    else:
        print("User input is string")

def check_value(statment,options=[]):
    while True:
        try:
            value = int(input(statment))
            if len(options) != 0:
                if value in options:
                    return value
                else:
                    print("OPPS!! Please select valid option \n ")
                    continue
            else:
                return value
        except ValueError:
            print("OPPS!! Character value is not allow Please select Integer Number")
            print("Please, try again \n")
            continue

def print_desh():
    dash = '-' * 33
    print(dash)

def print_menu(list_item,options):
    print("NO   ITEMS    PRICE   QUANTITY")
    print_desh()
    count = 1
    for prodItem in list_item:
        if prodItem[3] > 0:
            print('{:<5d}{:<10s}{:<10.2f}{:<5d}'.format(count, prodItem[1], prodItem[2], prodItem[3]))
            options[count] = prodItem[0]
            count += 1
    print_desh()
    return options

def print_invoice(cart):
    print()
    print("------   LOGISTIC SYSTEM   ------")
    total = 0
    cross = 'x' * 33
    print(cross)
    for item in cart:
        print('{:<5d}{:<10s}{:<5d}{:<10.2f}'.format(item[0], item[1], item[2], item[3]))
        total += item[3]
    print(cross)
    print("Total Amount : ", total)
    return total


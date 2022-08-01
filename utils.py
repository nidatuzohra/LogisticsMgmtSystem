import customerOperations

# Common functions will be defined here
def check_value(statement, options=[]):
    while True:
        try:
            value = int(input(statement))
            if len(options) != 0:
                if value in options:
                    return value
                else:
                    print("OOPS!! Please select a valid option \n ")
                    continue
            elif value < 1:
                print("Invalid value.")
                continue
            else:
                return value
        except ValueError:
            print("OOPS!! Character value is not allowed, please select a number")
            print("Please, try again \n")
            continue


def print_dash():
    dash = '-' * 33
    print(dash)


def print_menu(list_item, options, role="C"):
    print("NO.   ITEMS    PRICE   QUANTITY")
    print_dash()
    count = 1
    for prodItem in list_item:
        if role == "C" and prodItem[3] > 0 or role == "A":
            print('{:<5d}{:<10s}{:<10.2f}{:<5d}'.format(count, prodItem[1], prodItem[2], prodItem[3]))
            options[count] = prodItem[0]
            count += 1
    print_dash()
    return options


def print_invoice(cart):
    print()
    print("------   LOGISTICS SYSTEM   ------")
    total = 0
    cross = 'x' * 33
    print(cross)
    for item in cart:
        print('{:<5d}{:<10s}{:<5d}{:<10.2f}'.format(item[0], item[1], item[2], item[3]))
        total += item[3]
    print(cross)
    print("Total Amount : ", total)
    return total

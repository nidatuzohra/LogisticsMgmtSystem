def check(statment):
    correct_option = True
    while correct_option:
        try:
            question = input(statment)
            if len(question) > 2:
                return question
            else:
                print("\nOPPS!! Name should be more than 2 character is allowed\nplease try again\n ")
                continue
        except ValueError:
            print("OPPS!! Please insert proper value ")
            print("Please, try again \n")
            continue

def signup():
    first_name = check("Enter your first name: ")
    last_name = check("Enter Your last name: ")
    customer_emil_id = check("Enter your E-mail: ")
    customer_password = check("Enter Password: ")



# Common functions will be defined here

def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("User input is Number")
    else:
        print("User input is string")
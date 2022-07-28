import sqlite3
import adminOperations

connection = sqlite3.connect("logisticsdb.db")

# Function that checks availability and adds product to the cart
def add_to_cart(cart, product_id, qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = int(cursor.fetchone()[0])
    if qty > product_qty:
        return False
    else:
        cursor.execute("SELECT * FROM PRODUCT WHERE ID= '%s'" % product_id)
        product_details = cursor.fetchone()
        print(product_details[2])
        cart.append([product_details[0], product_details[1], qty, qty * product_details[2]])
        adminOperations.update_product_qty(product_id, qty)
        return cart

def show_product():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PRODUCT")
    available_product = cursor.fetchall()
    if available_product is None:
        return False
    else:
        return available_product

def show_vehicle():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM VEHICLE")
    available_vehicle = cursor.fetchall()
    if available_vehicle is None:
        return -1
    else:
        return available_vehicle

def fetch_value(total_value,statment):
    correct_no = True
    while correct_no:
        try:
            # selected_no = int(input("Select your delivery mode: "))
            selected_no = int(input(statment))
            if selected_no in total_value:
                return selected_no
                correct_option = False
            else:
                print("OPPS!! Please Insert proper Product Number\n ")
                continue
        except ValueError:
            print("OPPS!! Character value is not allow Please select Integer Number")
            print("Please, try again \n")
            continue

def show_location():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM LOCATION")
    available_country = cursor.fetchall()
    if available_country is None:
        return -1
    else:
        return available_country

# -------------------------------------------------------------------------------
# connection.close()

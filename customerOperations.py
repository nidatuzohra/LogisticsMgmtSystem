import sqlite3
import adminOperations

connection = sqlite3.connect("logisticsdb.db")

# Function that checks availability and adds product to the cart
def add_to_cart(cart, product_id, qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = int(cursor.fetchone()[0])
    if qty > product_qty:
        return -1
    else:
        cursor.execute("SELECT * FROM PRODUCT WHERE ID= '%s'" % product_id)
        product_details = cursor.fetchone()
        #cart.append(product_details)
        cart.append([product_details[0], product_details[1], qty, qty * product_details[2]])
        adminOperations.update_product_qty(product_id, qty)
        return cart

def show_product():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PRODUCT")
    available_product = cursor.fetchall()
    if available_product is None:
        return -1
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

def show_location():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM LOCATION")
    available_country = cursor.fetchall()
    if available_country is None:
        return -1
    else:
        return available_country

def end_user(confirm):
    cursor = connection.cursor()
    if (confirm == 'y' or confirm == 'Y' or confirm == 'YES' or confirm == 'Yes'):
        cursor.execute("COMMIT;")
    if (confirm == 'n' or confirm == 'N' or confirm == 'NO' or confirm == 'no'):
        cursor.execute("ROLLBACK;")

# -------------------------------------------------------------------------------
# connection.close()

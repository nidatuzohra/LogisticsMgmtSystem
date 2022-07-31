import sqlite3
import adminOperations

connection = sqlite3.connect("logisticsdb.db")

# Function to update the quantity of a product based on product id
def update_product_qty(product_id,qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = cursor.fetchone()
    new_qty = product_qty[0] - qty   # it will update due to customer new quanity
    cursor.execute("UPDATE PRODUCT SET QUANTITY = ? WHERE ID = ?", [new_qty, product_id])
    cursor.execute("COMMIT;")

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
        total = float(qty * product_details[2])
        cart.append([product_details[0], product_details[1], qty, total])
        update_product_qty(product_id, qty)
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
    while True:
        try:
            # selected_no = int(input("Select your delivery mode: "))
            selected_no = int(input(statment))
            if selected_no in total_value:
                return selected_no
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

def get_user_id(email_id):
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM USER WHERE EMAIL = '%s'" % (email_id))
    user_id = int(cursor.fetchone()[0])
    return user_id

def store_order_details(user_id,vehicleid,origin,destination,price):
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM CUSTOMER WHERE USERID = '%d'" %(user_id))
    customer_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO ORDERS ('CUSTOMERID', 'VEHICLEID','ORIGIN','DESTINATION','PRICE') VALUES ('%d','%d','%d', '%d', '%d')" %(customer_id, vehicleid, origin,destination,price))
    cursor.execute("COMMIT;")

def store_oreder_items(user_id,cart):
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM CUSTOMER WHERE USERID = '%d'" %(user_id))
    customer_id = cursor.fetchone()[0]
    cursor.execute("SELECT ID FROM ORDERS WHERE CUSTOMERID = '%d'" %(customer_id))
    order_id = cursor.fetchone()[0]
    for item in cart:
        qty = item[2]
        product_id = item[0]
        cursor.execute("INSERT INTO ORDERITEM ('ORDERID', 'PRODUCTID','QUANTITY') VALUES ('%d','%d','%d')" %(order_id,product_id,qty))
        cursor.execute("COMMIT;")


def rollback_qty(cart):
    cursor = connection.cursor()
    for item in cart:
        qty = item[2]
        cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % item[0])
        product_qty = cursor.fetchone()
        new_qty = product_qty[0] + qty  # it will update due to customer new quanity
        cursor.execute("UPDATE PRODUCT SET QUANTITY = ? WHERE ID = ?", [new_qty, item[0]])
    cursor.execute("COMMIT;")
# # -------------------------------------------------------------------------------
# connection.close()

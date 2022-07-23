import sqlite3
import adminOperations

connection = sqlite3.connect("User.db")


# Function that checks availability and adds product to the cart
def add_to_cart(cart, product_id, qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = cursor.fetchone()
    if qty > product_qty:
        return -1
    else:
        cursor.execute("SELECT * FROM PRODUCT WHERE ID= '%s'" % product_id)
        product_details = cursor.fetchone()
        cart.append[product_details]
        adminOperations.update_product_qty(product_id,qty)
        return cart

    
# --------------------------------------------------------------------------------
# connection.close()

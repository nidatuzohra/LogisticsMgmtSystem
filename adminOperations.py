import sqlite3

connection = sqlite3.connect("logisticsdb.db")


# Function to check user login information - different py file?
def check_login_id(loginid):
    cursor = connection.cursor()
    cursor.execute("SELECT EMAIL FROM USER Where EMAIL= '%s'" % loginid)
    loginName = cursor.fetchone()
    if loginName == None:
        return False
    else:
        return True


# Function to add a product in the database
def save_product(name, price, quantity):
    cursor = connection.cursor()
    data = [(name, price, quantity)]
    cursor.execute("INSERT INTO PRODUCT(PRODUCTSNAME, PRICE, QUANTITY) VALUES (?, ?, ?)", data)
    cursor.execute("COMMIT;")


# Function to update the quantity of a product based on product id
def update_product_qty(product_id):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = cursor.fetchone()
    new_qty = product_qty[0] + 1
    cursor.execute("UPDATE PRODUCT SET QUANTITY = ? WHERE ID = ?", [new_qty, product_id])
    cursor.execute("COMMIT;")
    print("Product quantity updated successfully")


# Function to add a vehicle in the database
def save_vehicle(vehicle_type):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO VEHICLE(TYPE) VALUES (?)", vehicle_type)
    cursor.execute("COMMIT;")


# Function to add a location in the database
def save_location(name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO LOCATION(COUNTRY) VALUES (?)", name)
    cursor.execute("COMMIT;")


# Function to generate (a specific kind of?) reports
def generate_report():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM LOCATION")
    # generate a table of all locations


# --------------------------------------------------------------------------------
# connection.close()
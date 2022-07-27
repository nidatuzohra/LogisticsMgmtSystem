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

# function to check the password
def checkPswd(loginid, pswd):
    cursor = connection.cursor()
    cursor.execute("SELECT PASSWORD FROM USER Where EMAIL= '%s'" % loginid)
    password = cursor.fetchone()[0]
    if password == pswd:
        return True
    else:
        return False


# Function to save customer details in the database
def save_customer(email, pwd, first_name, last_name):
    cursor = connection.cursor()
    user_info = [email, pwd, 'C']
    cursor.execute("INSERT INTO USER(EMAIL, PASSWORD, ROLE) VALUES(?, ?, ?)", user_info)
    user_id = cursor.execute("SELECT ID FROM USER WHERE EMAIL = '%s'" % email).fetchone()[0]
    customer_info = [first_name, last_name, user_id]
    cursor.execute("INSERT INTO CUSTOMER(FIRSTNAME, LASTNAME, USERID) VALUES(?, ?, ?)", customer_info)
    cursor.execute("COMMIT;")
    cursor.close()


# Function to add a product in the database
def save_product(name, price, quantity):
    cursor = connection.cursor()
    data = [name, price, quantity]
    cursor.execute("INSERT INTO PRODUCT(PRODUCTSNAME, PRICE, QUANTITY) VALUES (?, ?, ?)", data)
    cursor.execute("COMMIT;")
    cursor.close()


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
    cursor.execute("INSERT INTO VEHICLE(TYPE) VALUES (?)", (vehicle_type,))
    cursor.execute("COMMIT;")


# Function to add a location in the database
def save_location(name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO LOCATION(COUNTRY) VALUES (?)", (name,))
    cursor.execute("COMMIT;")


# Function to generate (a specific kind of?) reports
def generate_report():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM LOCATION")
    # generate a table of all locations

# --------------------------------------------------------------------------------
# connection.close()

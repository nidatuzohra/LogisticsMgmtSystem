import sqlite3

connection = sqlite3.connect("logisticsdb.db")
user_email = ""

# Function to check user login information - different py file?
def check_login_id(loginid):
    global user_email
    cursor = connection.cursor()
    cursor.execute("SELECT EMAIL FROM USER Where EMAIL= '%s'" % loginid)
    loginName = cursor.fetchone()
    if loginName == None:
        return False
    else:
        user_email = loginName
        return True

# function to check the password
def checkPswd(loginid, pswd, selectedRole):
    cursor = connection.cursor()
    cursor.execute("SELECT PASSWORD, ROLE FROM USER Where EMAIL= '%s'" % loginid)
    details = cursor.fetchall()
    password = details[0][0]
    role = details[0][1]
    if password == pswd:
        if selectedRole == 1 and role == 'A' or selectedRole == 2 and role == 'C':
            return True
        else:
            return False
    else:
        return False

# Function to add a product in the database
def save_product(name, price, quantity):
    cursor = connection.cursor()
    data = [name, price, quantity]
    cursor.execute("INSERT INTO PRODUCT(PRODUCTSNAME, PRICE, QUANTITY) VALUES (?, ?, ?)", data)
    cursor.execute("COMMIT;")
    cursor.close()


# Function to update the quantity of a product based on product id
def update_product_qty(product_id,qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = cursor.fetchone()
    new_qty = product_qty[0] - qty   # it will update due to customer new quanity
    cursor.execute("UPDATE PRODUCT SET QUANTITY = ? WHERE ID = ?", [new_qty, product_id])
    cursor.execute("COMMIT;")
    print("Product quantity updated successfully")


#--------- customer details add by customer  -----------
def create_customer_details(first_name,last_name):
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM USER WHERE EMAIL = '%s'" %(user_email))
    user_id = cursor.fetchone()[0]
    cursor.execute("BEGIN TRANSACTION;")
    cursor.execute("INSERT INTO CUSTOMER ('FIRSTNAME','LASTNAME','USERID') VALUES ('%s','%s','%d')" %(first_name,last_name,user_id) )
    cursor.fetchone()
    #cursor.execute("COMMIT;")
    return user_id

def store_order_details(user_id,vehicleid,origin,destination,price):
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM CUSTOMER WHERE ID = '%d'" %(user_id))
    customer_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO ORDERS('CUSTOMERID', 'VEHICLEID','ORIGIN','DESTINATION','PRICE') VALUES ('%d','%d','%d', '%d', '%d')" %(customer_id, vehicleid, origin,destination,price))
    cursor.execute("COMMIT;")

# Function to add a vehicle in the database
def save_vehicle(vehicle_type):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO VEHICLE(TYPE) VALUES (?)", (vehicle_type))
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
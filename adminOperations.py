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


# Function to check product id
def check_product_id(product_id):
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM PRODUCT Where ID= '%s'" % product_id)
    prod_id = cursor.fetchone()
    if prod_id == None:
        return False
    else:
        return True


# Function to list all product
def show_all_product():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PRODUCT")
    prod = cursor.fetchall()
    return prod
    cursor.close()


# Function to update the quantity of a product based on product id
def admin_update_product_qty(product_id, new_qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qnty = cursor.fetchone()
    new_qty = product_qnty[0] + new_qty
    cursor.execute("UPDATE PRODUCT SET QUANTITY = ? WHERE ID = ?", [new_qty, product_id])
    cursor.execute("COMMIT;")
    print("Product quantity updated successfully")


def update_product_qty(product_id, qty):
    cursor = connection.cursor()
    cursor.execute("SELECT QUANTITY FROM PRODUCT Where ID= '%s'" % product_id)
    product_qty = cursor.fetchone()
    new_qty = product_qty[0] - qty  # it will update due to customer new quantity
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

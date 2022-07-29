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
import sqlite3
import csv

connection = sqlite3.connect("User.db")

def checkLoginId(loginid):
    cursor = connection.cursor()
    cursor.execute("SELECT Login FROM TB_USER Where Login= '%s'" % loginid)
    loginName = cursor.fetchone()
    if loginName == None:
        return False
    else:
        return True


def saveInDB(loginid, pswd):
    cursor = connection.cursor()
    data = [(loginid, pswd, 0)]
    cursor.executemany("INSERT INTO TB_USER(Login, CRYP_PASSWORD, ACCESS_COUNT) VALUES (?, ?, ?)", data)
    cursor.execute("COMMIT;")
    updateCSV()


def updateInDB(loginid, pswd):
    print("Updated Details", loginid, pswd)
    cursor = connection.cursor()
    cursor.execute("SELECT ACCESS_COUNT FROM TB_USER Where Login= '%s'" % loginid)
    access_count = cursor.fetchone()
    count_inc = access_count[0] + 1
    values = (loginid, pswd, count_inc, loginid)
    cursor.execute(''' Update TB_USER SET Login = ?, CRYP_PASSWORD = ?, ACCESS_COUNT = ? WHERE Login = ? ''', values)
    cursor.execute("COMMIT;")
    print("Hello", loginid, "Welcome. access=", count_inc)
    updateCSV()

def checkPswd(loginid, pswd):
    cursor = connection.cursor()
    cursor.execute("SELECT CRYP_PASSWORD FROM TB_USER Where Login= '%s'" % loginid)
    password = cursor.fetchone()[0]
    if password == pswd:
        return True
    else:
        return False

def updateCSV():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TB_USER")
    results = cursor.fetchall()
    with open('userdb-backup.csv', 'w') as out:
        csv_out = csv.writer(out)
        for row in results:
            csv_out.writerow(row)



# --------------------------------------------------------------------------------
# connection.close()

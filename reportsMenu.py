import sqlite3
# import pandas as pd


def showReportsOptions():
    connection = sqlite3.connect("logisticsdb.db")
    cursor = connection.cursor()
    noReportExit = True

    while noReportExit:
        print("\nChoose an option to generate report."
              "\n 1-All destinations sorted by frequencies."
              "\n 2-Customers placed most orders."
              "\n 3-Top 5 & Least 5 products ordered."
              "\n 4-Back")
        try:
            reportChoice = int(input("Select an option: "))
        except ValueError:
            print('\nWrong selection!! Try again.', ValueError)
            continue

        if reportChoice == 4:
            print("Exit to main admin menu")
            noReportExit = False
        else:
            if reportChoice == 1:
                print("All destinations sorted by frequencies.")
                cursor.execute("SELECT COUNTRY FROM LOCATION JOIN ORDERS ON ORDERS.DESTINATION = LOCATION.ID")
                data_list = cursor.fetchall()
                destination_list = []
                for x in range(len(data_list)):
                    destination_list.append(data_list[x][0])
                # destination_df = pd.DataFrame(destination_list, columns='Destination')
                # destination_freq = destination_df['Destination'].value_counts()
                # print(destination_freq)
                # print(type(destination_freq))
            elif reportChoice == 2:
                print("Customers placed most orders.")
                print("Add generating report fn here")
            elif reportChoice == 3:
                print("Top 5 & Least 5 products ordered.")
                print("Add generating report fn here")
            else:
                print("Wrong selection. Try again with different option.")
                continue
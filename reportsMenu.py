# import pandas as pd
import adminOperations

def showReportsOptions():
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
            print("Exit to admin menu")
            noReportExit = False
        else:
            if reportChoice == 1:
                print("All destinations sorted by frequencies.")
                print("Add generating report fn here")
            elif reportChoice == 2:
                print("Customers placed most orders.")
                adminOperations.get_AllCustomers()
            elif reportChoice == 3:
                print("Top 5 & Least 5 products ordered.")
                print("Add generating report fn here")
            else:
                print("Wrong selection. Try again with different option.")
                continue
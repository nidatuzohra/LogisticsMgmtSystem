import pandas as pd
import matplotlib.pyplot as plt
import adminOperations


def showReportsOptions():
    noReportExit = True

    while noReportExit:
        print("\nChoose an option to generate report."
              "\n 1-All destinations sorted by frequencies."
              "\n 2-Customers placed most orders."
              "\n 3-Top 5 products ordered."
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
                print("All destinations sorted by order frequency")
                destination_list = adminOperations.get_all_destinations()
                destination_freq = {x: destination_list.count(x) for x in destination_list}
                destination_df = pd.DataFrame(destination_freq.items(), columns=['Destination', 'Count']).sort_values('Count', ascending=False)
                plt.bar(destination_df['Destination'], destination_df['Count'], color='#855a9e')
                plt.title("Order destinations in most ordered from to least")
                plt.xlabel("Countries")
                plt.ylabel("Order Frequency")
                plt.show()
            elif reportChoice == 2:
                print("Customers placed most orders.")
                allCustomers = adminOperations.get_AllCustomers()
                df = pd.DataFrame(allCustomers, columns=['CustomerId', 'FirstName', 'LastName', 'Total orders'])
                print(df)
                plt.bar(df['FirstName'], df['Total orders'])
                plt.show()
            elif reportChoice == 3:
                print("Top 5 products ordered.")
                print("All Products in Descending Order.")
                order_list = adminOperations.get_descendingorder()
                df = pd.DataFrame(order_list, columns=['Id', 'FirstName', 'ProductName', 'ProductID', 'Quantity'])
                plt.bar(df['ProductName'], df['Quantity'])
                plt.show()
            else:
                print("Wrong selection. Try again with different option.")
                continue

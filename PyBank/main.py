#Create the modules needed for this assignment

import os
import csv

#Set the path for the file
csvpath = os.path.join('Resources/budget_data.csv')

#Open the budget data csv file
with open(csvpath, newline = "") as csvfile:

    #set csv reader and variable that will hold the data
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read header row first
    csv_header = next(csvreader)
    
    #Create an new list to add the csv values
    total_months = []
    net_total_amount = []
    net_change = []

    #Iterate through all the values and add to empty list
    for row in csvreader:
        total_months.append(row[0])
        net_total_amount.append(int(row[1]))

    for i in range(len(net_total_amount)-1):  
        net_change.append(net_total_amount[i + 1] - net_total_amount [i]) 

    #Evaluate the greatest and lowest profit
    greatest_increase = max(net_change)
    greatest_decrease = min(net_change)

    #Evaluate the greatest and lowest month using index
    month_increase = net_change.index(max(net_change)) + 1
    month_decrease = net_change.index(min(net_change)) + 1

# print the results to the screen
    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months:{len(total_months)}")
    print(f"Total: ${sum(net_total_amount)}")
    print(f"Average Change: {round(sum(net_change)/len(net_change),2)}")
    print(f"Greatest Increase in Profit: {total_months[month_increase]} (${(str(greatest_increase))})")
    print(f"Greatest Decrease in Profit: {total_months[month_decrease]} (${(str(greatest_decrease))})")


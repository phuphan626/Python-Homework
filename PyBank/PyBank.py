#Import os and csv into Python
import os
import csv
#Set path to file as variable
inputpath=os.path.join("Resources", "budget_data.csv")
outputpath=os.path.join("analysis","analysis.txt")
#Set profit,loses,month and date in variable
initial_profit=0
final_profit=0
total_profit=0
total_changes=0
count=0
profit=[]
date=[]
monthly_change=[]
greatest_increase=[]
greatest_decrease=[]

#Using CSV module to read through the file,and store it to csvfile variable
with open(inputpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip the header,so the row[] will take the initial value in the second column
    csvheader=next(csvreader)
    for row in csvreader:
        count=count+1

        date.append(row[0])

        profit.append(row[1])

        total_profit=total_profit+int(row[1])

        final_profit=int(row[1])

        profit_change=final_profit-initial_profit

        monthly_change.append(profit_change)

        total_changes=total_changes+profit_change

        initial_profit=final_profit

        average=round(sum(monthly_change)/len(monthly_change))
    #Using min and max to find greatest increase and decrease
        greatest_decrease=min(monthly_change)
        greatest_increase=max(monthly_change)
        decrease_date=date[monthly_change.index(greatest_decrease)]
        increase_date=date[monthly_change.index(greatest_increase)]
    analysis={
        "Total Months:":count,
        "Total Profits:":str(total_profit)+"$",
        "Average Change:":str(average)+"$",
        "Greatest Increase in Profits:":(str(greatest_increase)+"$",increase_date),
        "Greatest Decrease in Profits:":(str(greatest_decrease)+"$",decrease_date)}
print(analysis)
# print("-----------------")
# print("Financial Analysis")
# print("-----------------")
# print("Total Months:")
# print("Total Profits:")
# print("Average Change:")
# print("Greatest Increase in Profit:")
# print("Greatest Decrease in Profit:")
with open(outputpath,'w') as text:
    text.write("----------------------------\n")
    text.write("Financial Analysis"+"\n")
    text.write("----------------------------\n")
    text.write("Total Months:"+" "+str(count)+" "+"months"+"\n")
    text.write("Total Profits:"+" "+"$"+str(total_profit)+"\n")
    text.write("Average Change:"+" "+"$"+str(average)+"\n")
    text.write("Greatest Increase in Profits:"+" "+str(increase_date)+" " +"("+"$"+str(greatest_increase)+")"+"\n")
    text.write("Greatest Decrease in Profits:"+" "+str(decrease_date)+" " +"("+"$"+str(greatest_decrease)+")"+"\n")
    text.write("----------------------------\n")



        


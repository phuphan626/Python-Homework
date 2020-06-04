#Import os and csv into Python
import os
import csv
#Set path to file as variable
inputpath=os.path.join('..','Resources','budget_data.csv')
outputpath=os.path.join('..','analysis','analysis.csv')
#Set profit,loses,month and date in variable
total_month=0
total_profit=0
greatest_increase=["",0]
reatest_decrease=["",999999999999999999999]
#Assign value for the profit and losses as the integer
profit=int(row["Profit/Losses"])
#Assign an array for the date
date_change=[]
#Using CSV module to read through the file,and store it to csvfile variable
with open(inputpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter='')
    for row in csvreader:
        total_month=total_month+1
        total_profit=total_profit+profit
        if 
        


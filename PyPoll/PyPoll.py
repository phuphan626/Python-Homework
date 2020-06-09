#Source https://github.com/shrawantee/Python-PyBank-and-PyPoll

import os
import csv
inputpath=os.path.join("Resources","election_data.csv")
outputpath=os.path.join("analysis","analysis.txt")

count=0
country=[]
candidate=[]
unique_candidate=[]
vote_count=[]
vote_percent=[]

with open(inputpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    for row in csvreader:
        count=count+1
        candidate.append(row[2])
        country.append(row[1])
    for x in set(candidate):
        unique_candidate.append(x)
        y=candidate.count(x)
        vote_count.append(y)
        z=round(((y/count)*100),4)
        vote_percent.append(z)
    winning=max(vote_count)
    winner=unique_candidate[vote_count.index(winning)]
print("-----------")
print("Election Result")
print("Total Vote:" + str(count))
print("-----------")
for i in range(len(unique_candidate)):
        print(unique_candidate[i] + ":" + str(vote_percent[i]) + "%" + "(" + str(vote_count[i]) + ")")
print("----------")
print("The Winner is:" + winner)


with open(outputpath,'w')as text:
    text.write("Election Result\n")
    text.write("----------------\n")
    text.write("Total Vote:" + str(count) + "\n")
    for i in range(len(unique_candidate)):
        text.write(unique_candidate[i] + ":" + str(vote_percent[i]) + "%" + "(" + str(vote_count[i]) + ")" +"\n")
        
    text.write("-----------------\n")
    text.write("The winner is:" + winner + "\n")
    
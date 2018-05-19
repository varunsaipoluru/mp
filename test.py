import pygeoip
import csv
import requests
from collections import Counter
import sys
# import matplotlib.pyplot as plt


new_arr = []
hack_team = []
year_count = []
hack_dict = {}

with open('cases.csv', encoding="ISO-8859-1") as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    for row in readCSV:
     	new_arr.append(dict(row))

#****************************************Module 1
#Top 10 most hacks
for i in range(len(new_arr)):
	hack_team.append(new_arr[i].get("Notify"))

hack_dict = Counter(hack_team)

with open('organizations.txt','w') as file:
    for l in range(len(hack_dict)):
        file.write(str(list(hack_dict.items())[l]) + '\n')


limit = 3
print("Top "+str(limit)+" most hacks by organizations")
print("*"*34)
# print(Counter(hack_team).most_common(10))
for j in range(len(Counter(hack_team).most_common(limit))):
	# print(Counter(hack_team).most_common(10)[j])
	print("'"+str(Counter(hack_team).most_common(limit)[j][0])+"' hacked "+ str(Counter(hack_team).most_common(limit)[j][1])+" websites")
# print(hack_team.count("BD GREY HAT HACKERS"))
# print(hack_team)
#Top 10 most hacks
#****************************************Module 1

print("\n")

print("Check all the hacking organization names generated in the file organizations.txt")
print("\n")
#****************************************Module 2
# Team CodeZero
print("Websites hacked by an organization")
print("*"*35)
team = input("Enter the name of hacking organization: ")

for k in range(len(new_arr)):

	if(new_arr[k].get("Notify") == str(team)):
		print(str(team)+" organization hacked "+str(new_arr[k].get("URL"))+
			" website in "+str(new_arr[k].get("Country"))+" on "+str(new_arr[k].get("Date")))

#****************************************Module 2


print("\n")
print("Check the total number of hacking incidents occured in a particular year")
print("\n")

#****************************************Module 3

#Number of incidents in an year_
for i in range(len(new_arr)):
	year_count.append(new_arr[i].get("Date")[:4])
# print(Counter(year_count))
# print(year_count.count("2015"))


print("List of years: "+str(Counter(year_count).keys())[10:])

year = input("Enter an year from the above list: ")

if(year in str(Counter(year_count).keys())[10:]):
	year_val = year_count.count(year)
	print("Total incidents reported in the year "+year+" were: "+str(year_val))
else:
	print("Please try again !!!")
	sys.exit()

# name = input("Whats your name ? - ")
# print("Hii "+str(name))


#****************************************Module 3



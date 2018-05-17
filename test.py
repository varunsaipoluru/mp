import pygeoip
import csv
import requests
from collections import Counter
import sys
# import matplotlib.pyplot as plt


new_arr = []
year_count = []

with open('cases.csv', encoding="ISO-8859-1") as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    for row in readCSV:
     	new_arr.append(dict(row))


# print(len(new_arr))
# print(new_arr[1])
# print(new_arr[1].get("Date")[:4])

#Number of incidents in an year_
for i in range(len(new_arr)):
	year_count.append(new_arr[i].get("Date")[:4])
# print(Counter(year_count))
# print(year_count.count("2015"))

print(new_arr[87762])	

#############################################################################

# print("List of years: "+str(Counter(year_count).keys())[10:])

# year = input("Enter an year from the above list: ")

# if(year in str(Counter(year_count).keys())[10:]):
# 	year_val = year_count.count(year)
# 	print("Total incidents reported in the year "+year+" were: "+str(year_val))
# else:
# 	print("Please try again !!!")
# 	sys.exit()

# name = input("Whats your name ? - ")
# print("Hii "+str(name))


##############################################################################



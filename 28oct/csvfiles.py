import csv

# excel filer are in two format one csv and another one is xlsx and for this we have to use different library

with open("data_csv.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for value in row:
            print(value, end=", ")
        print()

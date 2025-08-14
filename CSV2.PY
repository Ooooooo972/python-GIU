import csv

with open('variable/CSV/university_records.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    print(headers)
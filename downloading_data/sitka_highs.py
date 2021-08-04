import csv

file_name = "data/sitka_weather_07-2018_simple.csv"

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)


    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)


print(highs)

for index, column_header in enumerate(header_row):
    print(index, column_header)
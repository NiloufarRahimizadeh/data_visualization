import csv

file_name = "data/sitka_weather_07-2018_simple.csv"

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
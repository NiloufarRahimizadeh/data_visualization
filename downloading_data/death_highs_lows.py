import csv
from datetime import date, datetime
import matplotlib.pyplot as plt


file_name = 'data/death_valley_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get date, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# The alpha argument controls a color’s transparency.
ax.plot(dates, highs, c='red', alpha=1)
ax.plot(dates, lows, c='blue', alpha=1)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.2)

# Format plot
plt.title("Daily high and low temperatures - 2018\n Death Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
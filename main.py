# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107011133.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# create a new list to store output data
new_data = []
# Retrive all data points which HUMD is not '-99.000' or '-999.000' as a list.
filter_data = list(filter(lambda item: item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))
for i in ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']:
    # Retrive all data points which station_id equals to i which i is 'C0A880' in first loop and 'C0F9A0' in second loop and so on
    target_data = list(filter(lambda item: item['station_id'] == i, filter_data))
    sum = 0
    for j in target_data:
        sum += float(j['HUMD']) # sum up all the desired HUMD
    # set up output data
    if sum == 0:
        new_data.append([i,'None'])
    else:
        new_data.append([i,sum])
# Retrive ten data points from the beginning.
#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(new_data)
#========================================
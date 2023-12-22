# Python program to convert
# JSON file to CSV


import json
import csv

# Opening JSON file and loading the data
# into the variable data

json_file = open('C:/Users/Microsoft/Desktop/example_2.json')
data = json.load(json_file)

json_file.close();

employee_data = data['emp_details']

# now we will open a file for writing
csv_file = open('C:/Users/Microsoft/Desktop/output.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(csv_file)

# Counter variable used for writing 
# headers to the CSV file
count = 0

for emp in employee_data:
	if count == 0:

		# Writing headers of CSV file
		header = emp.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(emp.values())

csv_file.close()
print("done")


import csv
import json
file1 = "math"
csvfile = open(file1 + '.csv', 'r')
jsonfile = open(file1 + '.json', 'w')

fieldnames = ("timestamp","name","image","convenor","fb","events","projects","description")

heading = True

reader = csv.DictReader( csvfile, fieldnames)
mainheadingIndex = 0
jsonfile.write('var ' + file1 + ' = [\n')

for row in reader:
	# to skip the first entry which makes up the headings
	if heading == True:
			heading = False
			continue

	# To make formatting right
	# the first main heading doesn't need a ',' in the beginning
	if mainheadingIndex != 0:
		jsonfile.write(",\n")
	else:
		mainheadingIndex+=1
	subHeadingIndex = 0
	jsonfile.write('{\n')
	
	for i, j in row.items():
		# To make formatting right
		# the first subheading in each main doesn't need a ',' in the beginning
		if subHeadingIndex == 0:
			jsonfile.write('\t\"' + str(i) + "\": ")
			# To check if value in None in csv.
			# If None, give json an empty string
			if j == None:
				jsonfile.write("\"\"")
			else:
				jsonfile.write("\"" + str(j) + "\"")
			subHeadingIndex+=1
		else:
			jsonfile.write(',\n\t\"' + str(i) + "\": ")
			if j == None:
				jsonfile.write("\"\"")
			else:
				jsonfile.write("\"" + str(j) + "\"")
	jsonfile.write('\n}')
jsonfile.write('\n]\n')
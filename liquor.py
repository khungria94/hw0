import csv

def main():
	found = 0
	check = 'single malt scotch'
	with open('iowa-liquor-sample.csv', 'rb') as f:
		reader = csv.reader(f, delimiter='\n')
		for row in reader:
			testlist = row[0].split(',')
			for n in testlist:
				if n.lower() == check:
					found +=1
					 
	print 'There are '+str(found)+' records that contain the word '+check+'.'

main()

#! python3
###Script to get starttime and endtime difference.
##Still quite messy & not portable as yet
###To do:
# 1. Read contents of file skipping first row
# 2. Convert into a list: Each row 
# 3. Parse the timestamps and get the differenc for each row http://stackoverflow.com/questions/21533200/finding-the-difference-between-times-in-different-columns-through-a-csv-file
# 4. Get resuls and append to file as column
# 5. Sort result file by IP, write output to sorted csv file with headers http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/
# http://stackoverflow.com/questions/28162358/append-a-header-for-csv-file-in-python


import csv, datetime, ipaddress 

#define function that returns 9th value - the int value of ip address (list of lists
def sort_foo(x):
	return x[8]

#Read from file

fileRows = []
sessionFile = open('/yourpath/file.csv')
sessionReader = csv.reader(sessionFile)
for row in sessionReader:
	
	if sessionReader.line_num == 1:
		header = list(row) 
		header.append('duration') #add header for new duration column
		#header.append('ipInt')
		
		continue #ignore and skip first row (headers)

	#fileRows.append(row)
	eachLine = list(row)
	#ip = int(ipaddress.ip_address(eachLine[4])) #convert IP address to int
	#eachLine.append(int(ipaddress.ip_address(eachLine[4])))
	#print(ip)
	stime = str(eachLine[1])
	etime = str(eachLine[2])
	#print(eachLine)
	if (stime == 'NULL') or (etime == 'NULL'):
		eachLine.append("NULL")
		eachLine.append(int(ipaddress.ip_address(eachLine[4]))) #convert ip address to int and add as last item
		fileRows.append(eachLine)
		
		#add NULL to list
	
	else: 
		#Time stamps: get difference for each row
		time1 = datetime.datetime.strptime(stime, '%Y-%m-%d %H:%M:%S')
		time2 = datetime.datetime.strptime(etime, '%Y-%m-%d %H:%M:%S')
		duration = time2 - time1 
		
		eachLine.append(str(duration))
		eachLine.append(int(ipaddress.ip_address(eachLine[4])))
		fileRows.append(eachLine)

#print(fileRows)	
resultRows = sorted(fileRows, key=sort_foo)
#print(resultRows)

#Write out new file
outputFile = open('/yourpath/output.csv', 'w')
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(header) #write the header
for line in resultRows:
	line = list(line)
	del line[-1]
	print(line)

	outputWriter.writerow(line)

sessionFile.close()
outputFile.close()
	
	



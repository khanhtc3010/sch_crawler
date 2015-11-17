

def string2IntList(stringList):
	resultList = []
	for i in xrange(len(stringList)):
		resultList.append(int(stringList[i]))
	return resultList

if __name__ == '__main__':
	# myString = "   1  ,   9"
	# print string2IntList(myString.split(','))

	if "埼玉県".decode("urf-8") in 
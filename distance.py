
# calculate Levenshtein distance between two strings str1 and str2
def levDistance(str1, str2):
	# get mappings
	mappings = getListOfIndexMappings(str1, str2, 0, 0)

	# get optimal set of mappings of shared chars
	optimal = {}
	for d in mappings:
		if len(d) > len(optimal):
			optimal = d

	# get format of buffer for strings based on mappings
	buf = getBufferedArrayFormats(str1, str2, optimal)

	differences = 0
	for i in range(0, len(buf[0])):
		if buf[0][i] != buf[1][i]:
			differences += 1

	return differences

# return dictionary associating indices of chars in str1 with their corresponding chars in str2
def getListOfIndexMappings(str1, str2, start1, start2):

	setOfDicts = []

	for ind1 in range(start1, len(str1)):
		for ind2 in range(start2, len(str2)):

			if str1[ind1] == str2[ind2]:

				if ind1 != len(str1) - 1 and ind2 != len(str2) - 1:

					print "Entering subproblem with start1 on ", str1, " = ", ind1 + 1, " and start2 on ", str2, " = ", ind2 + 1
					subProblemSet = getListOfIndexMappings(str1, str2, ind1 + 1, ind2 + 1)

					if len(subProblemSet) != 0:
						for dict_ in subProblemSet:

							dict_[ind1] = ind2
							setOfDicts.append(dict_)	# add to set
					else:
						d = {}
						d[ind1] = ind2
						setOfDicts.append(d)
				else:
					d = {}
					d[ind1] = ind2
					setOfDicts.append(d)

	
	print "exiting subproblem"
	return setOfDicts

# return buffered array which works for both str1 and str2
def getBufferedArrayFormats(str1, str2, indexMapping):

	sharedIndices = sorted([ (key, indexMapping[key]) for key in indexMapping ])

	bufferedTemplate = []
	for i in sharedIndices:
		bufferedTemplate.append(str1[i[0]])

	# DEBUG
	print bufferedTemplate
	print sharedIndices

	template1 = bufferedTemplate[:]
	template2 = bufferedTemplate[:]

	firstIter = True

	indexInTemplate = 0
	print "shared incides: ", sharedIndices
	for i in range(0, len(sharedIndices)):


		curShared = sharedIndices[i]
		prevShared = sharedIndices[i - 1] if i > 0 else (0, 0)#  if curShared != (0, 0) else (-1, -1)


		if curShared[0] - prevShared[0] > curShared[1] - prevShared[1]:
			bufferspace = curShared[0] - prevShared[0]
		else:
			bufferspace = curShared[1] - prevShared[1]

		if i != 0:
			bufferspace -= 1

		print "\n\nlooking at shared char '", str1[curShared[0]], "'"

		print "prevshared: ", prevShared
		print "curShared: ", curShared

		charsInBetween1 = str1[prevShared[0] + 1 if not firstIter else 0 : curShared[0]]
		charsInBetween2 = str2[prevShared[1] + 1 if not firstIter else 0 : curShared[1]]

		#DEBUG
		print "In between:"
		print "1: ", charsInBetween1
		print "2: ", charsInBetween2

		print "bufferspace: ", bufferspace


		for j in range(0, bufferspace):

			if j < len(charsInBetween1):
				template1.insert(indexInTemplate, charsInBetween1[len(charsInBetween1)- 1 - j])
			else:
				template1.insert(indexInTemplate, None)

			if j < len(charsInBetween2):
				template2.insert(indexInTemplate, charsInBetween2[len(charsInBetween2) - 1 - j])
			else:

				template2.insert(indexInTemplate, None)

			bufferedTemplate.insert(indexInTemplate, None)
			print "Inserting none at ", indexInTemplate

		print bufferedTemplate


		indexInTemplate += bufferspace + 1
		print "index updating to ", indexInTemplate
		firstIter = False

	# now add end buffer if needed
	end = (len(str1), len(str2))
	secondToEnd = sharedIndices[len(sharedIndices) - 1]

	if end[0] - secondToEnd[0] > end[1] - secondToEnd[1]:
		bufferspace = end[0] - secondToEnd[0] - 1
	else:
		bufferspace = end[1] - secondToEnd[1] - 1


	print "end: ", end
	print "second to end ", secondToEnd

	charsBeforeEnd1 = str1[secondToEnd[0] + 1:end[0]]
	charsBeforeEnd2 = str2[secondToEnd[1] + 1:end[1]]	

	# DEBUG
	print "before end1: ", charsBeforeEnd1
	print "before end2: ", charsBeforeEnd2

	for j in range(0, bufferspace):
			bufferedTemplate.append(None)

			if j < len(charsBeforeEnd1):
				template1.append(charsBeforeEnd1[j])
			else:
				template1.append(None)

			if j < len(charsBeforeEnd2):
				template2.append(charsBeforeEnd2[j])
			else:
				template2.append(None)

	print "Buffered Template: "
	print bufferedTemplate

	print "temp1: ", template1
	print "temp2: ", template2

	return ( template1, template2 )

def main():
	w1 = "cat"
	w2 = "catch"

	lev = levDistance(w1, w2)
	print lev




if __name__ == "__main__":
	main()
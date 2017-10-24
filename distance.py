
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
	buf = getBufferedArrayFormat(str1, str2, optimal)

	# get actual formatted arrays for each string
	format1 = getFormattedFromBuffer(str1, buf)
	format2 = getFormattedFromBuffer(str2, buf)

	differences = 0
	for i in range(0, len(format1)):
		if format1[i] != format2[i]:
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
def getBufferedArrayFormat(str1, str2, indexMapping):

	sharedIndices = sorted([ (key, indexMapping[key]) for key in indexMapping ])

	bufferedTemplate = []
	for i in sharedIndices:
		bufferedTemplate.append(str1[i[0]])

	# DEBUG
	print bufferedTemplate
	print sharedIndices

	for i in range(0, len(sharedIndices)):

		curShared = sharedIndices[i]
		prevShared = sharedIndices[i - 1] if i > 0 else (0, 0) if curShared != (0, 0) else (-1, -1)

		if curShared[0] - prevShared[0] > curShared[1] - prevShared[1]:
			bufferspace = curShared[0] - prevShared[0] - 1
		else:
			bufferspace = curShared[1] - prevShared[1] - 1

		print "bufferspace: ", bufferspace

		for j in range(0, bufferspace):
			bufferedTemplate.insert(i, None)

		i = i + bufferspace

	# now add front buffer if needed
	if sharedIndices[0][0] > sharedIndices[0][1]:
		bufferspace = sharedIndices[0][0]
	else:
		bufferspace = sharedIndices[0][1]

	for j in range(0, bufferspace):
			bufferedTemplate.insert(0, None)

	# now add end buffer if needed
	end = (len(str1), len(str2))
	secondToEnd = sharedIndices[len(sharedIndices) - 1]

	if end[0] - secondToEnd[0] > end[1] - secondToEnd[1]:
		bufferspace = end[0] - secondToEnd[0] - 1
	else:
		bufferspace = end[1] - secondToEnd[1] - 1

	for j in range(0, bufferspace):
			bufferedTemplate.append(None)

	print "Buffered Template: "
	print bufferedTemplate

	return bufferedTemplate

# return the filled out buffer for a given string
def getFormattedFromBuffer(str, buffer):
	pass

def main():
	w1 = "cranberry"
	w2 = "randomly"

	lev = levDistance(w1, w2)
	print lev


if __name__ == "__main__":
	main()
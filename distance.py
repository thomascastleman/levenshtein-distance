
# calculate Levenshtein distance between two strings str1 and str2
def levDistance(str1, str2):
	pass


# # find optimal position (int) of a char[] str1Common relative to char[] str2Common
# # so that the most shared chars are aligned
# def getOptimalZeroPosition(str1Common, str2Common):

# 	maxInCommon = 0
# 	optZeroIndex = 1 - len(str1Common)
	
# 	for zeroIndex in range(1 - len(str1Common), len(str2Common)):

# 		startIndex = 0 if zeroIndex <= 0 else zeroIndex
# 		endIndex = zeroIndex + len(str1Common) if zeroIndex + len(str1Common) <= len(str2Common) else len(str2Common)

# 		common = 0
# 		for i in range(startIndex, endIndex):

# 			str1Index = i - zeroIndex;
# 			if (str2Common[i] == str1Common[str1Index]):
# 				common += 1

# 		if common > maxInCommon:
# 			maxInCommon = common
# 			optZeroIndex = zeroIndex


# 		print ""
# 		print "z == ", zeroIndex, ", score == ", common
# 		print "str2:"
# 		print str2Common[startIndex:endIndex]

# 		print "str1:"
# 		print str1Common[startIndex - zeroIndex: endIndex - zeroIndex]



# 	return optZeroIndex

# return dictionary associating indices of chars in str1 with their corresponding chars in str2
def getListOfIndexMappings(str1, str2, start1, start2):

	setOfDicts = []

	for ind1 in range(start1, len(str1)):
		for ind2 in range(start2, len(str2)):

			if str1[ind1] == str2[ind2]:

				char = str1[ind1]
				print char, " == ", char, " at position ", ind1, " to ", ind2

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

# return the char[] form of str1 and str2 which have been buffered as necessary with null positions to allow direct comparison
def getBufferedArrayFormats(str1, str2, indexMapping):

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



	return None

def main():
	w1 = "cranberry"
	w2 = "randomly"

	s = getListOfIndexMappings(w1, w2, 0, 0)
	print "set: ", s

	opt = {}
	for d in s:
		if len(d) > len(opt):
			opt = d

	print "\n\n"

	both = getBufferedArrayFormats(w1, w2, opt)


	# z = getOptimalZeroPosition(w2Com, w1Com)
	# print "Optimal zero index of ", w1Com, " on ", w2Com, " --> ", z

if __name__ == "__main__":
	main()
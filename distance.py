
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


def main():
	w1 = "paine"
	w2 = "cane"

	s = getListOfIndexMappings(w1, w2, 0, 0)
	print "set: ", s

	# z = getOptimalZeroPosition(w2Com, w1Com)
	# print "Optimal zero index of ", w1Com, " on ", w2Com, " --> ", z

if __name__ == "__main__":
	main()
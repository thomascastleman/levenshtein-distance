
# calculate Levenshtein distance between two strings str1 and str2
def levDistance(str1, str2):
	pass


# find optimal position (int) of a char[] str1Common relative to char[] str2Common
# so that the most shared chars are aligned
def getOptimalZeroPosition(str1Common, str2Common):

	maxInCommon = 0
	optZeroIndex = 1 - len(str1Common)
	
	for zeroIndex in range(1 - len(str1Common), len(str2Common)):

		startIndex = 0 if zeroIndex <= 0 else zeroIndex
		endIndex = zeroIndex + len(str1Common) if zeroIndex + len(str1Common) <= len(str2Common) else len(str2Common)

		common = 0
		for i in range(startIndex, endIndex):

			str1Index = i - zeroIndex;
			if (str2Common[i] == str1Common[str1Index]):
				common += 1

		if common > maxInCommon:
			maxInCommon = common
			optZeroIndex = zeroIndex


		print ""
		print "z == ", zeroIndex, ", score == ", common
		print "str2:"
		print str2Common[startIndex:endIndex]

		print "str1:"
		print str1Common[startIndex - zeroIndex: endIndex - zeroIndex]



	return optZeroIndex

def getSetOfAllListsOfNonConflictingSharedCharacters(str1, str2, start1, start2):

	setOfLists = []

	for ind1 in range(start1, len(str1)):
		for ind2 in range(start2, len(str2)):

			if str1[ind1] == str2[ind2]:

				char = str1[ind1]

				print char, " == ", char

				if ind1 != len(str1) - 1 and ind2 != len(str2) - 1:


					print "Entering subproblem with start1 on ", str1, " = ", ind1 + 1, " and start2 on ", str2, " = ", ind2 + 1
					subProblemSet = getSetOfAllListsOfNonConflictingSharedCharacters(str1, str2, ind1 + 1, ind2 + 1)

					if len(subProblemSet) != 0:
						for list_ in subProblemSet:

							l = [char] + list_		# add char

							print "adding list ", l, " to result"

							setOfLists.append(l[:])	# add to set
					else:
						setOfLists.append([char])
				else:
					setOfLists.append([char])

	print "exiting subproblem"
	return setOfLists








def main():
	w1 = "chant"
	w2 = "catch"

	s = getSetOfAllListsOfNonConflictingSharedCharacters(w1, w2, 0, 0)
	print "set: "
	for item in s:
		print item

	# z = getOptimalZeroPosition(w2Com, w1Com)
	# print "Optimal zero index of ", w1Com, " on ", w2Com, " --> ", z

if __name__ == "__main__":
	main()
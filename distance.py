
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


		print "\n"
		print "z == ", zeroIndex
		print "str2:"
		print str2Common[startIndex:endIndex]

		print "str1:"
		print str1Common[startIndex - zeroIndex: endIndex - zeroIndex]

		common = 0
		for i in range(startIndex, endIndex):

			str1Index = i - zeroIndex;
			if (str2Common[i] == str1Common[str1Index]):
				common += 1

		if common > maxInCommon:
			maxInCommon = common
			optZeroIndex = zeroIndex

	return optZeroIndex




def main():
	w1 = "cat"
	w2 = "chant"

	w1Com = ['l', 'a', 'e']
	w2Com = ['a', 'l', 'e']

	z = getOptimalZeroPosition(w2Com, w1Com)
	print "Optimal zero index of ", w1Com, " on ", w2Com, " --> ", z

if __name__ == "__main__":
	main()
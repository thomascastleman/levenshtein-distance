
# calculate Levenshtein distance between two strings str1 and str2
def levDistance(str1, str2):
	print "Getting optimal mapping of indices between '" + str1 + "' and '" + str2 + "' ...\n"
	# get mappings
	mappings = getListOfIndexMappings(str1, str2, 0, 0)

	# get optimal set of mappings of shared chars
	optimal = {}
	for d in mappings:
		if len(d) > len(optimal):
			optimal = d

	print "\nMapping found: ", optimal


	if len(optimal) > 0:

		# get format of buffer for strings based on mappings
		buf = getBufferedArrayFormats(str1, str2, optimal)


		print "\nBUFFERS:"
		for c in buf[0]:
			print c if c != None else "*",
		print ""
		for c in buf[1]:
			print c if c != None else "*",

		print ""
		disagree = 0
		for i in range(0, len(buf[0])):
			if buf[0][i] != buf[1][i]:
				disagree += 1
				print "-",
			else:
				print "+",

		print "\n\nFinished with ", disagree, " disagreements"

		return disagree

	else:

		return len(str1) if len(str1) > len(str2) else len(str2)

# return dictionary associating indices of chars in str1 with their corresponding chars in str2
def getListOfIndexMappings(str1, str2, start1, start2):

	setOfDicts = []

	for ind1 in range(start1, len(str1)):
		for ind2 in range(start2, len(str2)):

			if str1[ind1] == str2[ind2]:

				print "Char match found: '" + str1[ind1] + "' at ", ind1, " and ", ind2

				if ind1 != len(str1) - 1 and ind2 != len(str2) - 1:

					print "Entering subproblem on '" + str1[ind1 + 1:] + "' and '" + str2[ind2 + 1:] + "'"

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

	
	print "Exiting subproblem"
	return setOfDicts

# return buffered array which works for both str1 and str2
def getBufferedArrayFormats(str1, str2, indexMapping):
	# get list of tuples: indices of shared chars between strings
	sharedIndices = sorted([ (key, indexMapping[key]) for key in indexMapping ])

	# init buffer as array of shared chars
	bufferedTemplate = []
	for i in sharedIndices:
		bufferedTemplate.append(str1[i[0]])

	print "Shared characters: ", bufferedTemplate

	# copy that array into separate templates for each string
	template1 = bufferedTemplate[:]
	template2 = bufferedTemplate[:]

	indexInTemplate = 0		# index used to acces chars in each template

	print "Building buffered string templates..."
	# for each shared character
	for i in range(0, len(sharedIndices)):

		curShared = sharedIndices[i]								# current shared character
		prevShared = sharedIndices[i - 1] if i > 0 else (0, 0)		# previous shared character

		# set bufferspace to the greater of the two spaces (from the two strings) between current shared char and previous
		if curShared[0] - prevShared[0] > curShared[1] - prevShared[1]:
			bufferspace = curShared[0] - prevShared[0]
		else:
			bufferspace = curShared[1] - prevShared[1]

		# exception handling for first shared char
		if i != 0:
			bufferspace -= 1

		# get all characters betwen current and previous for both strings
		charsInBetween1 = str1[prevShared[0] + 1 if i != 0 else 0 : curShared[0]]
		charsInBetween2 = str2[prevShared[1] + 1 if i != 0 else 0 : curShared[1]]

		for j in range(0, bufferspace):

			# insert intermediate chars if they exist or buffer space
			# for string 1
			if j < len(charsInBetween1):
				template1.insert(indexInTemplate, charsInBetween1[len(charsInBetween1)- 1 - j])
			else:
				template1.insert(indexInTemplate, None)

			# for string 2
			if j < len(charsInBetween2):
				template2.insert(indexInTemplate, charsInBetween2[len(charsInBetween2) - 1 - j])
			else:
				template2.insert(indexInTemplate, None)

			# for generic buffer template
			bufferedTemplate.insert(indexInTemplate, None)

			print "\nstr1 template ", template1
			print "str2 template ", template2

		indexInTemplate += bufferspace + 1	# update index back up to the next shared char now that buffer space has been added

	# now add buffer space / chars to end if needed
	end = (len(str1), len(str2))
	secondToEnd = sharedIndices[len(sharedIndices) - 1]

	# calc bufferspace as greater of the needed space from both strings
	if end[0] - secondToEnd[0] > end[1] - secondToEnd[1]:
		bufferspace = end[0] - secondToEnd[0] - 1
	else:
		bufferspace = end[1] - secondToEnd[1] - 1

	# get all chars from (last shared) to (end of string)
	charsBeforeEnd1 = str1[secondToEnd[0] + 1:end[0]]
	charsBeforeEnd2 = str2[secondToEnd[1] + 1:end[1]]	

	# add buffer space
	for j in range(0, bufferspace):

			# for string 1
			if j < len(charsBeforeEnd1):
				template1.append(charsBeforeEnd1[j])
			else:
				template1.append(None)

			# for string 2
			if j < len(charsBeforeEnd2):
				template2.append(charsBeforeEnd2[j])
			else:
				template2.append(None)

			bufferedTemplate.append(None) # for generic buffer template

			print "\nstr1 template ", template1
			print "str2 template ", template2

	print "\n\nGENERIC BUFFER: "

	for i in bufferedTemplate:
		print i if i != None else "*",

	return ( template1, template2 )

def main():
	w1 = "dab"
	w2 = "onem"

	lev = levDistance(w1, w2)
	print "\nDistance: ", lev


if __name__ == "__main__":
	main()
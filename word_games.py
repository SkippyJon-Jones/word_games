# def point_function(word):
# 	dictpoints = {"a" : 1, "b" : 3, "c": 3, "d" : 2,
# 					"e" : 1, "f" : 4, "g" : 2, "h" : 4, "i" : 1,
# 					"j" : 8, "k" : 5, "l" : 1, "m" : 3, "n" : 1,
# 					"o" : 1, "p" : 3, "q" : 10, "r" : 1, "s" : 1,
# 					"t" : 1, "u" : 1, "v" : 4, "w" : 4, "x" : 8,
# 					"y" : 4, "z" : 10}
# 	sum = 0
# 	for x in word:
# 		sum = sum + dictpoints[x]

# 	return sum

# print (point_function("bad"))

def valid_words(word):

	list = []
	list1 = []
	with open("Collins Scrabble Words (2019).txt", "r") as f:
		for line in f:
			line = line.strip()
			if len(word) ==  len(line):
				list.append(line)

	for x in list:
		if x == word:
			list1.append(x)
	return list

print (valid_words("but"))
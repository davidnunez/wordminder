def wordcount(filename):
	textfile = open(filename, 'r')
	print("The number of words are: " + len(textfile.split(" ")))
	len(textfile.split(" "))
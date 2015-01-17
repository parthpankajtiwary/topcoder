t = input()
words = []
for x in range(t):
	words.append(raw_input())

for word in words:
	if len(word) <= 10:
		print word
	else:
		abbr = ""
		print word[0] + str(len(word[1:len(word) - 1])) + word[-1]		
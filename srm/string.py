


string = raw_input()

lowerStr = string.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
newStrOne = [x for x in lowerStr if x not in vowels]
finalStr = ["."+str(x) for x in newStrOne]
print "".join(finalStr)

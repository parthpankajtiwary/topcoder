
n, m = map(int, raw_input().split())
wordDictionary = {}
for x in xrange(m):
        ai, bi = map(str, raw_input().split())
        if len(ai) <= len(bi):
            wordDictionary[ai] = ai
        else:
            wordDictionary[ai] = bi
text = [x for x in raw_input().split()]
String = []
for x in text:
    String.append(wordDictionary[x])
print " ".join(String)

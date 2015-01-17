

t = input()
counter = 0

for x in xrange(t):
    currentArray = map(int, raw_input().split())
    if currentArray.count(1) >= 2:
        counter += 2
print counter        

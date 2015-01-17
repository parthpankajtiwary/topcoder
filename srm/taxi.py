'''
Choose the 3 and 1 as much as possible. And let 2 combine with themselves. 
If there are more 1s and 2s, let two 1s combine with 2, and every four 1s take same taxi.
'''
import math

t = input()
groups = [int(x) for x in raw_input().split()]

oneCount = groups.count(1)
twoCount = groups.count(2)
threeCount = groups.count(3)
fourCount = groups.count(4)

count = 0
count += fourCount
count += min(oneCount, threeCount)
#have not considered the left out cases of 3 and 1
count += twoCount/2
#have not considered the left out case of 2

leftTwo = twoCount%2
leftOne = 0
if oneCount > threeCount:
	leftOne = oneCount - threeCount
else:
	leftThree = threeCount - oneCount
	threeCount = threeCount - oneCount

if leftTwo < leftOne:
	count += leftTwo
	leftOne -= leftTwo
if leftTwo > leftOne:
	count += leftTwo	
if leftOne > 0 and leftOne < 4:
	count += 1
else:
	count += math.ceil(leftOne/4)
print int(count)					
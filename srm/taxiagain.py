

n = input()

array = map(int, raw_input().split())
countFour = array.count(4)

for x in xrange(countFour):
    array.pop(array.index(4))


fours_3_1 = min(array.count(3), array.count(1))
for x in xrange(fours_3_1):
    array.pop(array.index(3))
    array.pop(array.index(1))


fours_2_2 = array.count(2)
if fours_2_2 % 2 == 0:
    for x in xrange(fours_2_2):
        array.pop(array.index(2))
else:
    for x in xrange(fours_2_2 - 1):
        array.pop(array.index(2))


fours_1_1 = array.count(1)
if fours_1_1 % 4 == 0:
    for x in xrange(fours_1_1):
        array.pop(array.index(1))
else:
    for x in xrange(fours_1_1 - (fours_1_1%4)):
        array.pop(array.index(1))

if sum(array) <= 4 and len(array) != 0:
    print countFour + fours_3_1 + fours_2_2/2 + fours_1_1/4 + 1
else:
    print countFour + fours_3_1 + fours_2_2/2 + fours_1_1/4 + len(array)

from math import sqrt

t = input()
numbers = []
for x in xrange(t):
    numbers.append(input())
count = 0
for x in numbers:
    for y in xrange(int(sqrt(x))):
        for z in xrange((int(sqrt(x)))):
            if x**2 == (y**2 + z**2):
                count += 1
    print count

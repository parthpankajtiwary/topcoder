from math import sqrt
 
def findPrimes(limit):
    isPrime = {}
 
    isPrime[1] = False
    for i in range(2, limit + 1):
        isPrime[i] = True
 
    checkLimit = int(sqrt(limit)) + 1
    for i in range(2, checkLimit):
        if isPrime[i]:
            for factor in range(2, limit + 1):
                j = i * factor
                if (j > limit): break
                isPrime[j] = False
 
    primes = []
    for i in range(1, limit + 1):
        if isPrime[i]:
            primes.append(i)
    return primes

t = input()
answers = []

for x in xrange(t):
    number = 0
    a, b, k = map(int, raw_input().split())
    for x in xrange(a, b+1):
        count = 0
        primes = findPrimes(x)
        for y in primes:
            if x%y == 0:
                count += 1
        if count == k:
            number += 1
    answers.append(number)
i = 1
for x in answers:
    print ("Case #%s: " + str(x))%i
    i += 1                       
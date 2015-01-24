def makeLine(x):
    print x
    arrayOne = [int(y) for y in x]
    array = [arrayOne.count(y) for y in arrayOne]
    print array
    countArray = list(set(array))
    maxElement = max(countArray)
    print countArray
    countArray.remove(maxElement)
    summation = sum(countArray)

    print summation
    if maxElement >= summation+2:
        return "impossible"
    else:
        return "possible"

#print makeLine({1,1,2,2,3,3,4,4})
#print makeLine({3,3,3,3,13,13,13,13})
input = [3,7,7,7,3,7,7,7,3]
print makeLine(tuple(input))


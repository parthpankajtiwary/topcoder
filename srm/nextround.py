
n, k = map(int, raw_input().split())
inputs = [int(x) for x in raw_input().split()]

factor = inputs[k-1]
count = 0
for x in inputs:
	if x >= factor and x > 0:
		count += 1
print count		

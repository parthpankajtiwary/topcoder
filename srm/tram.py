

n = input()
upperLimit = 0
inside = 0
for x in xrange(n):
    exit, enter = map(int, raw_input().split())
    inside -= exit
    inside += enter
    if inside > upperLimit:
        upperLimit = inside
print upperLimit

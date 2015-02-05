t = input()

def check(aimP, aimC, aimF, p, c, f):
    p.sort()
    c.sort()
    f.sort()
    print p, c, f
    pFlag, cFlag, fFlag = False, False, False
    for x in xrange(len(p)):
        if p[-1] - p[x] == aimP:
            pFlag = True

    for x in xrange(len(c)):
        if c[-1] - c[x] == aimC:
            cFlag = True

    for x in xrange(len(f)):
        if f[-1] - f[x] == aimF:
            fFlag = True

    return pFlag and cFlag and fFlag

answers = []
for x in xrange(t):
    aimP, aimC, aimF = map(int, raw_input().split())
    n = input()
    pContents = [0]
    cContents = [0]
    fContents = [0]
    for x in xrange(n):
        contents = [int(x) for x in raw_input().split()]
        pContents.append(contents[0]+ pContents[-1])
        cContents.append(contents[1]+ cContents[-1])
        fContents.append(contents[2]+ fContents[-1])
    answers.append(check(aimP, aimC, aimF, pContents, cContents, fContents))

for x in answers:
    if x:
        print "yes"
    else:
        print "no"

def oddTuples(aTup):
    x = ()
    y = len(aTup)
    z = 0
    for a in aTup:
        if z < y:
            x += (aTup[z],)
            z+=2
    return x
#another solution
def oddTuples2(aTup):
    return aTup[::2]

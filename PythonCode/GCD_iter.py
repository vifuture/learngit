def gcdIter(a,b):
    max1 = max(a,b)
    min1 = min(a,b)
    while(min1>0):
        if(max1%min1 == 0 and min(a,b)%min1 == 0):
            return min1
        else:
            min1-=1

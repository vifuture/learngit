def gcdRecur(a,b):
    if(a==0 or b==0):
        return max(a,b)
    else:
        return gcdRecur(b,a%b)

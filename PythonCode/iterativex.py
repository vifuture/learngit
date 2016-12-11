def iterPower(base,exp):
    s=1
    if(exp <= 0):
        return 1
    elif(exp%2 == 0 and exp >0):
        print(exp)
        return base**2*iterPower(base,exp/2)
    else:
        return base*iterPower(base,exp-1)

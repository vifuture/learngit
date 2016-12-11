def isIn(char,aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char
    middle = len(aStr)/2
    if(char == aStr[middle]):
        return True
    elif(char > aStr[middle]):
        return isIn(char,aStr[middle:])
    else:
        return isIn(char,aStr[:middle])

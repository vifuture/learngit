def isIn(char,aStr):
    def lenRecur(aStr):
        if aStr == '':
            return 0
        else:
            return 1+lenRecur(aStr[1:])
    x = lenRecur(aStr)
    if(char == aStr[x/2]):
        return True
    elif char > aStr[x/2]:
        for b in aStr[x/2:]:
            if( char == aStr[b]):
                return True
            else:
                return False

    else:
        for b in aStr[:x/2]:
            if( char == aStr[b]):
                return True
            else:
                return False

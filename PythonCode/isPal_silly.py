def isPal(x):
    assert type(x)== list
    temp = x[:]
    temp.reverse()
    if temp == x:
        return True
    else:
        return False
def silly(n):
    results = []
    for i in range(n):
        elem = raw_input("Enter element:")
        results.append(elem)
    if isPal(results):
        print('Yes')
    else:
        print('No')

def fibMetered(x):
    global numCalls
    numCalls += 1
    if x ==0 or x ==1:
        return 1
    else:
        return fibMetered(x-1)+fibMetered(x-2)
def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('Fib of '+str(i) + ' = '+str(fibMetered(i)))
        print('Fib called '+str(numCalls)+' times')
        

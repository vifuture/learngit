x=int(raw_input("Enter a number"))
for ans in range(0,abs(x)+1):
    if ans**3 == abs(x):
        break
if ans**3!=abs(x):
    print(str(x)+' is not a perfect cube!')
else:
    if x < 0:
        ans = -ans;
    print('Cube root of '+str(x)+' is '+str(ans))

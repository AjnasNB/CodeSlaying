n=int(input())
sum=0
test=n
power=len(str(n))
while(n>0):
    sum+=int((n%10)**power)
    n//=10
if( sum==test):
    print("true")
else:
    print("false")
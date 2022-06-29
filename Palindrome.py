n=int(input())
temp=n
s=0
while n>0:
    s=s*10+n%10
    n=n//10
if temp==s:
    print('True')
else:
    print('False')
n=int(input())
r=0
t=0
s=n*n
while(n>0):
    r=r*10+(n%10)
    n=n//10
k=r*r
while(k>0):
    t=t*10+(k%10)
    k=k//10
if(t==s):
    print('True')
else:
    print('False')


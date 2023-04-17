n=1
m=1
N=int(input())
d=2
while(d<N):
    M=n+m
    n=m
    m=M
    d=d+1
if N>=3:
    print(M)   
else:
    print(1)

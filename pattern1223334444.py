#pattern1,22,333
n=int(input("enter :"))
for i in range(n):
    for j in range(n):
        if j<=n-i-2:
            print(" ",end="")
        elif j<n:
            print(i+1, end ="")
    for j in range(n-1):
        if j<=i-1:
            print(i+1,end="")
        else:
            print(' ', end ="")        
        
    print() 


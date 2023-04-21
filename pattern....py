#pattern*,***,****
n=int(input("enter the number:" ))
for i in range(n):
    for j in range(n):
        if j<=n-i-2:
            print(" ",end="")
        elif j<n:
            print('*', end ="")
    for j in range(n-1):
        if j<=i-1:
            print("*",end="")
        else:
            print(' ', end ="")        
        
    print()

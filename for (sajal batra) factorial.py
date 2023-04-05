#find factorial of any number
num=int(input("enter the number:"))
s=1

for z in range(num,0,-1):
    s*=z
print("the factorial of ",num,"is",s)

#Palindrome number

n=int(input("Enter the number:"))
m=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if m==r:    
    print("true")
else:
    print("false")


#Palindrome number
n=int(input("Enter the number:"))
temp=n
r=0
while(temp>0):
    r=r*10+temp%10
    temp=temp//10
if n==r:    
    print("true")
else:
    print("false")

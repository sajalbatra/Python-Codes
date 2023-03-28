#area of triangle
a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
s=a+b+c
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)

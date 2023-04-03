# find the armstrong numbers.
n=int(input("Enter the no,:"))
i=n
z=0
while i>0:
    d=i%10
    z+=d**3
    i=i//10
if z==n:
    print("it is an armstromg number")
else:
    print("it is not a armstrong no.")

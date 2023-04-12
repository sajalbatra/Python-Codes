#input two limits and generate all the prime numbers between them.
n1=int(input("Enter the number 1:"))
n2=int(input("Enter the number 2:"))
print("Prime numbers between", n1, "and", n2, "are:")
for i in range(n1,n2 + 1):
   if i > 1:
       for y in range(2,i):
           if (i % y) == 0:
               break
       else:
           print(i)
    
    

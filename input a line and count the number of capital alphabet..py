# Write a program in python to input a line and count the number of capital alphabet.
line=input("enter the line:")
p=0
for k in line:
    if k.isupper():
        p+=1
print(p)        

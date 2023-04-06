s=input("enter the string")
a=' '
for i in s:
    if i not in a:
        a+=1
d={}
for i in a:
    d[i]=s.count(i)
print(d)

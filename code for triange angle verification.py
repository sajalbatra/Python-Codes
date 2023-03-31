a=int(input('enter the angle 1: '))
b=int(input('enter the angle 2: '))
c=int(input('enter the angle 3: '))
d=int(input('enter the angle 4: '))
if a+b+c+d==360:
    print('quadilateral')
if a==90 and b==90 and c==90 and d==90:
    print('rectangle')
if a+b==180 or c+d==180:
    print('trapezium')
if a==c and b==d:
    print('parallelogram')
else:
    print('no quadilateral')




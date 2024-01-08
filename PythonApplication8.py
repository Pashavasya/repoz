print('Enter "A":')
a = int(input()) # Mike's money
print('Enter "B":')
b = int(input()) # Ivan's money
print('Enter "X":')
x = int(input()) # 

if a >= x and b >= x:
    print('2')
elif a >= x and (b - (b * a)) < 0:
    print('Mike')
elif b >= x and (a - (b * a)) < 0:
    print('Ivan')
elif (a + b) < x:
    print('0')
else:
    print('1')



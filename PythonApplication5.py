a = int(input())

if (a == 0):
    print('Zero number')
elif (a > 0) and (a % 2 == 0):
    print('Positive even number')
elif (a < 0) and (a % 2 == 0):
    print('Negative even number')
elif (a > 0) and (a % 2 != 0):
    print('Positive odd number')
else:
    print('Negative odd number')

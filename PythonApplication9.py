cnt = 0
x = int(input())
if x <= 2000000000:
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    print(cnt)
else:
    print("False")

    

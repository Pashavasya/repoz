a = "0"
b = 0
c = 0
n = int(input())
if n > 0:
    for i in range(1, n + 1):
        if i <= n:
            b += 1
            x = input() * b
        if a in x:
            c += 1
    print("Quantity of zero:", c)
else:
    print("False")
    



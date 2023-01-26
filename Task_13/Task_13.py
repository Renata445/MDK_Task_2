n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
if n > m:
    n, m = m, n
if x >= n/2:
    x = n - x
if y >= m/2:
    y = m - y
if x < y:
    print(x)
else:
    print(y)
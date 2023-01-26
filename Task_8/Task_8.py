x1 = int(input("Введите координату x: "))
y1 = int(input("Введите координату y: "))
x2 = int(input("Введите координату x: "))
y2 = int(input("Введите координату y: "))
if -1 <= (x1 - x2) <= 1 and -1 <= (y1 - y2) <= 1:
    print("YES")
else:
    print("NO")
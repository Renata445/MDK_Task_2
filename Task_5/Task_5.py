a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a < b and a < c:
    print("Наименьшее число: " + str(a))
elif b < a and b < c:
    print("Наименьшее число: " + str(b))
else:
    print("Наименьшее число: " + str(c))
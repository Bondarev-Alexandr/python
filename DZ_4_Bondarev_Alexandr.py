# Перемножить все нечётные значения в диапазоне от 1 до 100
a = 1
for i in range(1, 101):
    if i % 2 !=0:
        a *= i
print(a)

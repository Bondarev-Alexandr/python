a = int(input("Длина стороны a = "))
b = int(input("Длина стороны b = "))
c = int(input("Длина стороны с = "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")
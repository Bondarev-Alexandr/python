import random
A = set([random.randint(0, 5) for i in range(5)])
print("множество A", A)
B = set([random.randint(0, 5) for j in range(5)])
print("множество B", B)
print("множества равны" if A == B else "множества не равны")
if len(A - B) == 0:
    print('множество А состоит из множества В')
if len(B - A) == 0:
    print('множество В состоит из множества А')
X = A & B
print(f"множества пересекаются в {X}" if X else "множества не пересекаются")

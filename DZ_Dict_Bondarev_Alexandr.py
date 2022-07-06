sport_tov = {"Мяч": [35, 20],
             "Шайба": [24, 56],
             "Клюшка": [37, 19],
             "Рокетка": [12, 41],
             "Коньки": [65, 15],
             "Лыжи": [71, 9]}
print("Наш ассортимент:")
for key, value in sport_tov.items():
    print(key, '-', value[0], '-', value[1])
a = 0
while True:
    tov = input('Выбирите товар (для выхода из магазина введите n)')
    if tov == 'n' or tov not in sport_tov.keys():
        break
    kol = int(input('Введите необходимое количество:'))
    if kol > sport_tov[tov][1]:
        print("Извините, столько нет")
        continue
    a += sport_tov[tov][0] * kol
    sport_tov[tov][1] -=kol
print('К оплате', a)
print("Наш ассортимент:")
for key, value in sport_tov.items():
    print(key, '-', value[0], '-', value[1])
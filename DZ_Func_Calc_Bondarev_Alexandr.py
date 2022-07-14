import math
import random

def calc():
    print('Для выхода из калькулятора введите 0')
    while True:
        op = input('Введите математическую опреацию (+, -, *, /): ')
        if op == '0':
            break
        a = float(input('Введите 1-ое число: '))
        b = float(input('Введите 2-ое число: '))

        if op == '+':
            print('Результат: ', a + b)
        elif op == '-':
            print('Результат: ', a - b)
        elif op == '*':
            print('Результат: ', a * b)
        elif op == '/':
            if b != 0:
                print('Результат: ', a / b)
            else:
                print('Ошибка: ДЕЛЕНИЕ НА 0!')
calc()
# ПЕРЕИМЕНОВАТЬ: что такое "первый" и "второй"? вы не шифрограмму пишете — имена должны быть понятны
first = int(input())
second = int(input())

integer = first // second
# ПЕРЕИМЕНОВАТЬ: остаток от деления числа — remainder
ostatok = first % second

if ostatok == 0:
    print(f'{first} делится на {second} нацело\n'
          f'частное: {integer}')
else:
    print(f'{first} не делится на {second} нацело\n'
          f'неполное частное: {integer}\n'
          f'остаток: {ostatok}')


# D:\Python\Ustinov\2023.05.28>2.py
# 15
# 4
# 15 не делится на 4 нацело
# неполное частное: 3
# остаток: 3

# D:\Python\Ustinov\2023.05.28>2.py
# 8
# 2
# 8 делится на 2 нацело
# частное: 4



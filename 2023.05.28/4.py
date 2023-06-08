# ПЕРЕИМЕНОВАТЬ: клетка (игрового) поля — square, field
first = input()
second = input()

if (ord(first[0]) + int(first[1]) + ord(second[0]) + int(second[1])) % 2 == 0:
    print('да')
else:
    print('нет')


# D:\Python\Ustinov\2023.05.28>4.py
# h2
# a7
# да

# D:\Python\Ustinov\2023.05.28>4.py
# e2
# c4
# да

# D:\Python\Ustinov\2023.05.28>4.py
# b2
# f7
# нет



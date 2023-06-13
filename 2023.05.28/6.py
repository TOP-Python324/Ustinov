# ПЕРЕИМЕНОВАТЬ: кстати, почему не alpha и beta?
first = input()
second = input()

# ИСПОЛЬЗОВАТЬ: двойка здесь вызывает некоторый когнитивный диссонанс, несмотря на то, что использована правильно — но лучше всё-таки использовать другой оператор и единицу
if abs(ord(first[0]) - ord(second[0])) <= 1 and abs(int(first[1]) - int(second[1])) <= 1:
    print('да')
else:
    print('нет')


# D:\Python\Ustinov\2023.05.21>6.py
# c3
# b2
# да

# D:\Python\Ustinov\2023.05.21>6.py
# b5
# c6
# да

# D:\Python\Ustinov\2023.05.21>6.py
# f4
# g2
# нет


# ИТОГ: отлично — 4/4

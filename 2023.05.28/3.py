year = int(input())
# ИСПОЛЬЗОВАТЬ: круглые скобки не нужны, потому что приоритет оператора or и так ниже чем оператора and
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('да')
else:
    print('нет')


# D:\Python\Ustinov\2023.05.28>3.py
# 2018
# нет

# D:\Python\Ustinov\2023.05.28>3.py
# 2008
# да

# D:\Python\Ustinov\2023.05.28>3.py
# 2020
# да

# D:\Python\Ustinov\2023.05.28>3.py
# 2015
# нет



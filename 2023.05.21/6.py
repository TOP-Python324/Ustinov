first = input()
second = input()
if abs(ord(first[0])-ord(second[0])) < 2 and abs(int(first[1])-int(second[1])) < 2:
    print ('да')
else:
    print ('нет')


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
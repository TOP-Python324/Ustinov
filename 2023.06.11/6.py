number = input()
binary_set = {'0','1','b'}
if set(list(number)) <= binary_set:
    if (number.find('b') == 0 or number.find('0b') == 0):
        print ('да')
    else:
        print ('нет')
else:
    print ('нет')
    
    
    
# D:\Python\Ustinov\2023.06.11>6.py
# 0b1
# да

# D:\Python\Ustinov\2023.06.11>6.py
# 00b1
# нет

# D:\Python\Ustinov\2023.06.11>6.py
# b101
# да

# D:\Python\Ustinov\2023.06.11>6.py
# 0110
# нет
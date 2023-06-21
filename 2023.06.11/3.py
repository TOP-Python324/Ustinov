list1 = input().split()
list2 = input().split()
length_list1 = len(list1)
length_list2 = len(list2)
veracity = False
for i in range(0,length_list1-length_list2+1):
    if list1[i:i+length_list2]==list2:
        veracity = True
        break
if veracity:
    print ('да')
else:
    print('нет')


# D:\Python\Ustinov\2023.06.11>3.py
# 4 5 6 7 8
# 4 5
# да

# D:\Python\Ustinov\2023.06.11>3.py
# 4 5 6 7 8

# да

# D:\Python\Ustinov\2023.06.11>3.py


# да

# D:\Python\Ustinov\2023.06.11>3.py
# 4 5 6 7 8
# 4 6
# нет
mail = input()
if ((mail.find('@')+1 < mail.find ('.')) #символ '.' не может идти следом за '@'
    and mail.find('@')!=0  #символ '@' не может быть первым символом
    and mail.find('.')!= len(mail)-1): #символ '.' не может быть последним символом
    print ('да')
else:
    print ('нет')


# D:\Python\Ustinov\2023.06.11>1.py
# sdf@sdf.3
# да

# D:\Python\Ustinov\2023.06.11>1.py
# @sdf.sdf
# нет

# D:\Python\Ustinov\2023.06.11>1.py
# weewr@sfsdf.
# нет

# D:\Python\Ustinov\2023.06.11>1.py
# sfssasd@
# нет

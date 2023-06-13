text = input()
text = text.replace(' ','')
print (f'{(len(text)*30)//100} руб. {(len(text)*30)%100} коп.')


# D:\Python\Ustinov\2023.06.04>5.py
# текст
# 1 руб. 50 коп.

# D:\Python\Ustinov\2023.06.04>5.py
# да
# 0 руб. 60 коп.

# D:\Python\Ustinov\2023.06.04>5.py
# не очень большой текст
# 5 руб. 70 коп.
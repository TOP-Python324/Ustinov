dictionary = {}
while True:
    if couple := input().split():
        dictionary[couple[0]]= couple[1]
    elif not couple:
        break
word = input()
print (next((key for key, value in dictionary.items() if word == value), '! value error !'))


# D:\Python\Ustinov\2023.06.11>4.py
# 10 выполнение
# 20 пауза
# 30 продолжение
# 40 конец

# пауза
# 20

# D:\Python\Ustinov\2023.06.11>4.py
# 10 выполнение
# 20 пауза
# 30 продолжение
# 40 конец

# стоп
# ! value error !
number = int(input())
summa = 0
for i in range (2,number):
    if number%i == 0:
        summa = summa + i
    if number/(i+1) < 2:
        break
print (f'{summa+number+1}')




# D:\Python\Ustinov\2023.06.04>3.py
# 50
# 93

# D:\Python\Ustinov\2023.06.04>3.py
# 40
# 90
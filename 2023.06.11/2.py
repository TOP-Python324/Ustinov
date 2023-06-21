fruits = [input()]
while True:
    if (fruit := input()):
        fruits += [fruit]
    elif not fruit:
        break
fruits_str = ' и '.join(fruits)
fruits_str = fruits_str.replace (' и',',',len(fruits)-2) 
print (fruits_str)


# D:\Python\Ustinov\2023.06.11>2.py
# апельсин
# мандарин

# апельсин и мандарин

# D:\Python\Ustinov\2023.06.11>2.py
# арбуз
# банан
# кокос

# арбуз, банан и кокос

# D:\Python\Ustinov\2023.06.11>2.py
# арбуз
# банан
# абрикос
# яблоко

# арбуз, банан, абрикос и яблоко
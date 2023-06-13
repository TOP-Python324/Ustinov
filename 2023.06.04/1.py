out=[]
while True:
    inp=int(input())
    if inp%7 == 0:
        out += [inp]
    else:
        break
print (*out[::-1])


# D:\Python\Ustinov\2023.06.04>1.py
# 49
# 7
# 14
# 63
# 90
# 63 14 7 49    
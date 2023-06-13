type = int(input())
result = 0
for i in range (10**(type-1),10**type):
    integer = 0
    for j in range (2,int(i/2)):
        if i%j == 0:
            integer += 1
    if integer == 0:
        result +=1
print (result)        



# D:\Python\Ustinov\2023.06.04>4.py
# 3
# 143

# D:\Python\Ustinov\2023.06.04>4.py
# 4
# 1061


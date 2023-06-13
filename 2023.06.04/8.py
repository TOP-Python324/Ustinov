amount = int(input())
fib = [1,1]
for i in range (2, amount):
    fib += [fib[i-1]+fib[i-2]]
print (*fib[0:amount])


# D:\Python\Ustinov\2023.06.04>8.py
# 1
# 1

# D:\Python\Ustinov\2023.06.04>8.py
# 6
# 1 1 2 3 5 8

# D:\Python\Ustinov\2023.06.04>8.py
# 2
# 1 1

# D:\Python\Ustinov\2023.06.04>8.py
# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

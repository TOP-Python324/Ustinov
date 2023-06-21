scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
letters = list(input())
letters_count = {
    letter: letters.count(letter)
    for letter in set(letters)
}
result = 0
for letter, count in letters_count.items():
    for score, let in scores_letters.items():
        if letter in let.lower():
            result += count*score
print (result)
    

# D:\Python\Ustinov\2023.06.11>5.py
# хохма
# 14

# D:\Python\Ustinov\2023.06.11>5.py
# синхрофазатрон
# 29
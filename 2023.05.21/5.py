# ПЕРЕИМЕНОВАТЬ: целая часть числа — integer
integer = int(input())
# ПЕРЕИМЕНОВАТЬ: дробная часть числа — fractional
# ИСПРАВИТЬ: и стоило преобразовывать в int, если следующее ваше действие с этим объектом — обратное преобразование в str?
fractional = int(input())

# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше двух (см. пример ниже) — придумайте более универсальное решение
fractional = float (str(0)+'.'+str(fractional))
mil= integer+fractional
# КОММЕНТАРИЙ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
# ИСПРАВИТЬ: мили округлять не нужно
print (f'{mil:.2f} миль = {mil*1.61:.1f} км')


# D:\Python\Ustinov\2023.05.21>5.py
# 16
# 8
# 16.8 миль = 27.0 км

# 5
# 81
# КОММЕНТАРИЙ: а должно быть 5.81 миль
# 13.1 миль = 21.1 км


# СДЕЛАТЬ: смотрите на оформление кода, написанного преподавателем — оно практически полностью следует PEP 8


# ИТОГ: хорошо — 4/5

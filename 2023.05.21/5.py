# ПЕРЕИМЕНОВАТЬ: целая часть числа — integer
cel = int(input());
# ПЕРЕИМЕНОВАТЬ: дробная часть числа — fractional
drob = int(input());

# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше двух (см. пример ниже) — придумайте более универсальное решение
mil= cel+drob/10;
# КОММЕНТАРИЙ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
km=round(mil*1.61, 1);
print (f'{mil} миль = {km} км');


# D:\Python\Ustinov\2023.05.21>5.py
# 16
# 8
# 16.8 миль = 27.0 км

# 5
# 81
# КОММЕНТАРИЙ: а должно быть 5.81 миль
# 13.1 миль = 21.1 км


# СДЕЛАТЬ: смотрите на оформление кода, написанного преподавателем — оно практически полностью следует PEP 8


# ИТОГ: доработать — 2/5

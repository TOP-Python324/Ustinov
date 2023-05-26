number = int(input());
a = number//100;
b = (number % 100)//10;
c = number%10;
sum = a+b+c;
prois = a*b*c;
print (f'Сумма цифр = {sum}\nПроизведение цифр = {prois}')

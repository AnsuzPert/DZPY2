#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

per1 = input('ВВедите число: ')
sum=0
for i in per1:
    if (i in {'0','1','2','3','4','5','6','7','8','9'}) :
        sum = sum+int(i)
        print(i)
print ('сумма цифр в числе: ', sum)

# *4. НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#     Реализуйте алгоритм перемешивания списка.

from random import randint

N = int(input('ВВедите количество элементов списка: '))
spis = []
proiz = 1
for i in range(0,N):
    spis.append(randint(-N, N))
print (spis) 
with open('file.txt', 'r') as file:
    per = file.read().splitlines()
    for i in per:
        proiz *=spis[int(i)]
print (per)
print ('Сумма элементов на местах из файла равна: ', proiz)
"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""

n = int(input('Введите число N: '))
i = 0
j = 0
while 2 ** i <= n :
    i = i + 1
for j in range(i) :
    print(2 ** j)

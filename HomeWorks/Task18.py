# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = int(input("Введите длину массива "))

lst = [randint(1, 10) for _ in range(n)]
print(lst)

a = int(input("Какое число проверяем? "))

totalDiff = 999
res = 0

for i in set(lst):
    if i == a:
        res = i
        break
    diff = abs(i-a)
    if diff < totalDiff:
        totalDiff = diff
        res = i

print(f"Ближайшее к {a} будет число {res}")

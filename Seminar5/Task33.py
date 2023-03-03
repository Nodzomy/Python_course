# Задача №33.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

n = int(input("Введите количество оценок: "))

lst = [randint(1, 5) for _ in range(n)]
print(lst)
min_value = min(lst)
max_value = max(lst)
lst2 = [min_value if i == max_value else i for i in lst]
print(lst2)


# s=list(map(int,input().split()))[1:]
# ma=max(s)
# mi=min(s)
# n=list(map((lambda x: min_value if (x==max_value) else x),s))
# for a in n:
#     print(a,end=' ')

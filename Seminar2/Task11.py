# Задача No9. Решение в группах
# Дано натуральное число А >1. Определите, каким по счету числом Фибоначи оно является,
# то есть выведите такое число n, что ф(n)=А. Если А не является ичслом Фибоначчи, выведите число -1.



# if a == 0:
#     print(0)
# else:
#     fib_1, fib_2 = 0, 1
#     n = 1
#     while fib_2 <= a:
#         if fib_2 == a:
#             print(n)
#             break
#         fib_1, fib_2 = fib_2, fib_1 + fib_2
#         n += 1
#     else:
#         print(-1)


n = int(input())
i = 2
a = 0
b = 0
c = 1

while a < n:
    a = b + c
    b = c
    c = a
    i += 1
    if a > n:
        i = 0
if i == 0:
    print(-1)
else:
    print(i)
# Задача №35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def prostoNumber(a):
    count = 0
    for i in range(2, (a // 2) + 1):
        if (a % i == 0):
            count += 1
    if (count <= 0):
        print("Число простое")
    else:
        print("Число не является простым")


n = int(input("Введите число: "))
prostoNumber(n)
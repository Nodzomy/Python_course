# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

k = int(input("Введи первый элемент прогрессии: "))
diff = int(input("Введи разность: "))
n = int(input("Введи количество элементов: "))
a = []

for i in range(1, n+1):
    num = k+(i-1)*diff
    a.append(num)
print(a)
# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def rec(n):
    if (n <= 0):
        return
    val=input("Введите элемент: ")
    rec(n - 1) 
    print(val, end=" ")


n=(int(input("Введите число N элементов: "))) 
rec(n)



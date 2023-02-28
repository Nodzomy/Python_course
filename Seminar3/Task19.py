# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# from random import randint
# list_1 = [randint(-3, 6) for i in range(1, 10)]
# print(list_1)
# k = int(input("Введи число сдвига"))
# print(list_1[-k:len(list_1)]+list_1[:-k])

lst = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    lst.insert(0, lst.pop())
print(lst)
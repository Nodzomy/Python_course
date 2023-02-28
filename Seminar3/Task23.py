# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

lst = [0, -1, 5, 2, 3]
count = 0
for i in range(len(lst)-1):
    if lst[i+1] > lst[i]:
        count = count+1
print(count)

# list = [0, -1, 5, 2, 3, 5]
# count = 0
# elements = ''

# for i in range(len(list)-1):
# if list[i+1]>list[i]:
# count+=1
# elements=elements + ', '+ str(list[i])+ '<' + str(list[i+1])

# print(count, elements)

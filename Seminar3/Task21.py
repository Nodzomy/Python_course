# Задача №21. Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
set1=set()
for i in dictionary:
    for j in i:
        v = i[j].strip(" ")
        set1.add(v)
print(set1)


# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
# unique_values = set()

# for value in my_dict.values():

# unique_values.add(value)

# print(unique_values)
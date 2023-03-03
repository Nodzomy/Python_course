# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.
# Output: 19

# a = str(input("Введите текст: "))
# text = set(a.lower().split())

# print(len(text))

# Дан словарь my_dict и ключ my_key. Напишите код, который проверяет, 
# есть ли ключ my_key в словаре my_dict, и если да, 
# то возвращает соответствующее значение, а если нет, то возвращает значение по умолчанию None.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_key = 'b'
my_value = my_dict.get(my_key, None)
print(my_value) # 2



# Дан словарь my_dict и ключ my_key. Напишите код, который проверяет, 
# есть ли ключ my_key в словаре my_dict, 
# и если да, то возвращает соответствующее значение, а если нет, 
# то создает новый элемент в словаре с ключом my_key и значением 0, а затем возвращает 0.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_key = 'b'
my_value = my_dict.get(my_key, 0)
if my_value == 0:
    my_dict[my_key] = my_value
print(my_value)
print(my_dict)

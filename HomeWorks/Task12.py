# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введи сумму "))
p = int(input("Введи произведение "))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(x, y)


# s = int(input("Введите сумму чисел S: "))
# p = int(input("Введите произведение чисел P: "))
# d = s*s-4*(p)
# x1 = int((s+pow(d, 0.5))/2)
# x2 = int((s-pow(d, 0.5))/2)
# print(f'{s} {p} --> {x1} {x2}')
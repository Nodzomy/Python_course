# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел. 
# Input:[1,1,2,0,-1,3,4,4]
# Output: 6

list1 = [1,1,2,0,-1,3,4,4]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(len(list2))

# print(len(set(list1)))
import random

#randomly generating lists

list1 = [random.randrange(1, 30) for _ in range(0, 15)]
list2 = [random.randrange(1, 30) for _ in range(0, 15)]
list3 = []

#printing the lists

print(list1)
print(list2)

#comparing lists

for i in list1:
    if i in list2:
        if i not in list3:
            list3.append(i)

#print out the result

print(list3)

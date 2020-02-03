import random

def BubbleSort(list):
    for i in range(0, len(list) - 1):
        for j in range(0,len(list) - 1 - i):
           if list[j] > list[j+1]:
               list[j], list[j+1] = list[j+1], list[j]
    return list


list1 = [random.randrange(1, 30) for _ in range(0, 15)]
print(list1)

print(BubbleSort(list1))

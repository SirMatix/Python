import random

list1 = [random.randrange(1, 30) for _ in range(0, 15)]

list1.sort()
print(list1)

def list_sort1(list):
    list2 = []
    for i in list:
        if i not in list2:
            list2.append(i)
    list2.sort()
    print(list2)

def list_sort2(list):
    list = set(list)
    print(list)

list_sort1(list1)

list_sort2(list1)

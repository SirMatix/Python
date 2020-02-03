from random import randint

a = [randint(1,15) for x in range(25)]
b = [randint(1,15) for x in range(18)]
print('first random list')
print(a)
print('second random list')
print(b)


c = [x for x in a if x == x in b]
print('common elements in both random lists with duplicates')
print(c)

d = []

for x in c:
    if x not in d:
        d.append(x)

print('common elements in both random lists without duplicates')
print(d)

import random

x = [random.randrange(1, 30) for _ in range(0, 15)]

x.sort()
print(x)

def sort1(y):
    z = []
    for i in y:
        if i not in z:
            z.append(i)
    z.sort()
    return z

def sort2(y):
    y = set(y)
    return y

print(sort1(x))
print(sort2(x))

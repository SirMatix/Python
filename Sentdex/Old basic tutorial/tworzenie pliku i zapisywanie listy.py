import random

list1 = [random.randrange(1, 30) for _ in range(0, 15)]


f = open('nazwa.txt', 'w')

for i in list1:
    f.write(str(i) + '\n')

f.close()

f = open("nazwa.txt", "r")

print(f.read())

f.close()

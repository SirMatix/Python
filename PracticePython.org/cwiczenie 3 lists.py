a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = int(input('Chose a number:'))

c = [num for num in a if num < b]

print(c)

"""
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""


vowels = ['a','e','i','o','u']
vow_count=0

for letter in s:
    if letter == vowels[0] or letter == vowels[1] or letter == vowels[2] or letter == vowels[3] or letter == vowels[4]:
        vow_count +=1

print('Vowels: ', vow_count)
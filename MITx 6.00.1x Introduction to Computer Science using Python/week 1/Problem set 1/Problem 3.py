"""

Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

"""

# tracking variables initialization
maxLen=0
current=s[0]
longest=s[0]

# program loop
# iterating through letters of string s

for letter in range(len(s) - 1):
    #if letter ahead current letter is 'bigger' add to current sequence
    if s[letter + 1] >= s[letter]:
        current += s[letter + 1]
        # if lenght of the current sequence is longer than maxLen update it
        # and current becomes longest
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current=s[letter + 1]

# prints out the longest substring
print ('Longest substring in alphabetical order is: ' + longest)
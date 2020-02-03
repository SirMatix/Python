'''
this excercise shows useful buil-in functions
in Python 3.7
have a great time learning
'''


# absolute value 
exNum1 = -5
exNum2 = 5

print(abs(exNum1), exNum2)

if abs(exNum1) == exNum2:
    print('these are the same')
    
#help function help(module) first improt module if you wanna help on it
    
# max and min funcitons

exList = [1,2,3,4,5,6,7,8,9,0,12,12,13,14,15]
print(exList)
print('prinint out the maximum of the list')
print(max(exList))
print('printing out the minimum of the list')
print(min(exList))

# round function

x = 7.432425321452
y = 7.543532453223

print('x=',x,'y=',y,sep=' ')
print(round(x),round(y))

# math floor - rounds down, math ceil round up, need to import math


from functools import lru_cache


@lru_cache(maxsize = 1000)
def fibonacci(n):
    #Check that the input is a positive integer
    if type(n) != int:
        raise TypeError('n must be positive int')
    if n < 1:
        raise ValueError('n must be a positive int')
   
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

    
'''
#golden ratio calculation
for n in range(1,51):
    print(fibonacci(n+1) / fibonacci(n))
'''



for n in range(1,101):
    print(n, ':', fibonacci(n))


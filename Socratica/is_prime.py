import time
import math

def is_prime_v1(n):
    #Return 'True' if 'n' is a prime number. False otherwise
    if n == 1:
        return False #1 is not a prime

    for d in range(2,n):
        if n % d == 0 :
            return False
    return True


### ==== TEST FUNCTION ====
##
##for n in range(2,21):
##    print(n, is_prime_v1(n))
##
### ==== TIME FUNCTION ====
##
##t0 = time.time()
##for n in range(1, 10000):
##    is_prime_v1(n)
##t1 = time.time()
##print('time required: ', t1-t0)

def is_prime_v2(n):
    #Return 'True' if 'n' is a prime number. False otherwise
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

### ==== TEST FUNCTION ====
##
##for n in range(1,21):
##    print(n, is_prime_v2(n))
##
### ==== TIME FUNCTION ====
##
##t0 = time.time()
##for n in range(1, 100000):
##    is_prime_v2(n)
##t1 = time.time()
##print('time required: ', t1-t0)
##

def is_prime_v3(n):
    #Return 'True' if 'n' is a prime number. False otherwise
    if n == 1:
        return False # 1 is not a prime

    #if it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

### ==== TEST FUNCTION ====
##
##k = 0
##primes = []
##for n in range  (50,1000):
##    print(n, is_prime_v3(n))
##    if is_prime_v3(n) == True:
##        k += 1
##        primes.append(n)
##    else:
##        k += 0
##
##print('there is ' + str(k) + 'primes')
##print(primes)
##
### ==== TIME FUNCTION ====
##
##t0 = time.time()
##for n in range(1, 1000):
##    is_prime_v3(n)
##t1 = time.time()
##print('time required: ', t1-t0)

# === EXTRA TIME-TEST FUNCTION WITH PRIME LIST ====

t0 = time.time()
k = 0
primes = []
for n in range  (0,500000):
    if is_prime_v3(n) == True:
        k += 1
        primes.append(n)
    else:
        k += 0

print('there is ' + str(k) + 'primes')
print(primes)
t1 = time.time()
print('time required: ', t1-t0)

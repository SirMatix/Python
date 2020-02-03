def get_number(prompt):
    num = int(input(prompt))
    return num

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for x in range(2,(num-1)):
            if num % num == 0 and num % 1 == 0:
                return True
            else:
                return False

def print_prime(is_prime):
    if is_prime == True:
        print(num, 'is a prime number', sep=' ', end='\n')
    else:
        print(num, 'is not a prime number', sep=' ', end='\n')

number = get_number('please provide a number')

check = is_prime(number)

print(print_prime(check))

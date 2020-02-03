import random

'''
password generator minimum lenght is 8.
'''

def pass_gen(lenght=8):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    passlen = lenght
    psw = ''

    #generates random pass with lenght specified in passlen variable
    for i in range(passlen):
        next_index = random.randrange(len(alphabet))
        psw = psw + alphabet[next_index]

    #replace one or more of characters with a digit
    if lenght == 8:
        for i in range(random.randrange(1,3)):
            replace_index = random.randrange(len(psw)//2)
            psw = psw[0:replace_index] + str(random.randrange(10)) + psw[replace_index+1:]
    elif lenght > 8:
        for i in range(random.randrange(1,lenght//2)):
            replace_index = random.randrange(len(psw)//2)
            psw = psw[0:replace_index] + str(random.randrange(10)) + psw[replace_index+1:]

    #replace one or more of characters with a UPPERCASE letter
    if lenght == 8:
        for i in range(random.randrange(1,3)):
            replace_index = random.randrange(len(psw)//2,len(psw))
            psw = psw[0:replace_index] + psw[replace_index].upper() + psw[replace_index+1:]
    elif lenght > 8:
        for i in range(random.randrange(1,lenght//2)):
            replace_index = random.randrange(len(psw)//2,len(psw))
            psw = psw[0:replace_index] + psw[replace_index].upper() + psw[replace_index+1:]



    return(psw)


print(pass_gen(24))

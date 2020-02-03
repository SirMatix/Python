while True:
    quest = str(input('Do you wanna check divisors[Y/N]:'))
    if quest == 'Y' or quest == 'y':
        num = int(input('Choose a number: '))
        divs = []

        for i in range(1,num):
            if num % i == 0:
                divs.append(i)

        print('there is ' + str(len(divs)) + '  divisors')

        print(divs)
    elif quest == 'N' or quest == 'n':
        break;
    else:
        print('incorrect answer try again!')
              




    

            



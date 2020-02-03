from random import randint

print('This is a guessing game. You need to guess number from 1 to 9.')

rand_list = [x for x in range(1,10)]
play = 1

while play == 1:
    computer = rand_list[randint(1,10)]
    count = 0
    #game loop
    while True:
        player = int(input('guess a number from 1 to 9: '))
        if player == computer:
                 print('You guess correct! You win!')
                 count += 1
                 break;
        elif player > computer:
                 print('You guessed too high. Try again!')
                 count += 1
        elif player < computer:
                 print('You guessed too low. Try again!')
                 count += 1
    if count == 1:
        print('You finished game in:', count, 'move', sep=' ')
    elif count > 1:
        print('You finished game in:', count, 'moves', sep=' ')

    #exit/again loop
    while True:
        play = str(input('type "exit" to finish or "again" to try one more time: '))
        play = play.lower()
        if play == 'exit':
            play = 0
            break;
        elif play == 'again':
            play = 1
            break;
        else:
            print('wrong input try again!')
    
                     


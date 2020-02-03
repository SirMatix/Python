from random import randint



while True:
    start = str(input('Do you wanna play Rock, Paper, Scissors? [Y/N]'))
    if start == 'Y' or start == 'y':
        t = ["rock", "paper", "scissors"]
        computer = t[randint(0,2)]
        player = str(input('Choose Rock, Paper, Scissors: '))
        player = player.lower()
        print('You choose', player, 'computer choose', computer, sep=' ')
        if player == computer:
            print('tie!')
        elif player == 'rock':
            if computer == 'paper':
                     print(computer)
                     print('You lose', computer, 'covers', player, sep=' ')
            else:
                     print('You win', player, 'smashes', computer, sep=' ')
        elif player == 'paper':
            if computer == 'scissors':
                     print(computer)
                     print('You lose', computer, 'cuts', player, sep=' ')
            else:
                     print('You win', player, 'covers', computer, sep=' ')
        elif player == 'scissors':
            if computer == 'rock':
                     print(computer)
                     print('You lose', computer, 'smashes', player, sep=' ')
            else:
                     print('You win', player, 'covers', computer, sep=' ')
    elif start == 'N' or start == 'n':
        break;
    else:
        print('Wrong answer. Try again!')

        

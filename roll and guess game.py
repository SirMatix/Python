import random

def Throw(DiceSize):
	number = random.randint(1,DiceSize)
	return number

print('''
Welcome to dice throw and number guess simulator,
in order to play You need to pick the size of the dice,
range from which you are going to guess numbers and then just play!
''')

play = True
choice = input('would You like to play?: (y/n):')

while play:
        choice = choice.lower()
        g_count = 0
        Dice = int(input('Please chose the size of the dice:'))
        if choice == 'y':
                temp = Throw(Dice)
                guess = int(input('guess number on dice: '))
                guessing = True
                while guessing:
                        if guess == temp:
                                g_count += 1
                                print(temp,' is a good guess, you guessed in', g_count, 'tries')
                                choice = input('would You like to throw again?: (y/n):')
                                choice = choice.lower()
                                if choice == 'y':
                                        guessing = False
                                        play = True
                                elif choice == 'n':
                                        guessing = False
                                        play = False
                        elif guess != temp:
                                guess = int(input('guess again!: '))
                                g_count += 1
                                guessing = True

        elif choice == 'n':
                play = False

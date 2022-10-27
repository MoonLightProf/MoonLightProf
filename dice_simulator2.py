import random

x = 'y'

while x.lower() == 'y':
    number = random.randint(1 , 6)

    if number == 1:
        print(' ---------- ')
        print(' |         |')
        print(' |    0    |') 
        print(' |         |')
        print(' ---------- ')  
        print('1')
        print('/q')

    if number == 2:
        print(' ---------- ')
        print(' |         |')
        print(' |   0 0   |') 
        print(' |         |')
        print(' ---------- ') 
        print('2')
        print('/q')

    if number == 3:
        print(' ---------- ')
        print(' |         |')
        print(' |  0  0   |') 
        print(' |    0    |')
        print(' ---------- ') 
        print('3')
        print("/q")

    if number == 4:
        print(' ---------- ')
        print(' |         |')
        print(' |  0  0   |') 
        print(' |  0  0   |')
        print(' ---------- ') 
        print('4')
        print('/q')

    if number == 5:
        print(' ---------- ')
        print(' |  0   0   |')
        print(' |  0   0   |') 
        print(' |    0     |')
        print(' ---------- ') 
        print('5')
        print("/q")

    if number == 6:
        print(' ---------- ')
        print(' |  0   0   |')
        print(' |  0   0   |') 
        print(' |  0   0   |')
        print(' ---------- ')
        print('6')
        print("/q")

    x = input("Press 'y' to play again and /q to quit. ")

    if x.lower() == '/q':
        quit()
    else:
        print("I don't understand that, check the spelling or type /h for help.")

    if x.lower() == '/h':
        print("""
Commands:
/q - to quit
/h - help
/y - start/roll again


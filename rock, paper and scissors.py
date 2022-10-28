from random import randint   

choices = ["rock", "paper", "scissors"] #here is a list of choices
score = 0 #We have set score to 0 at the start. So while all this is true, the code #below will be executed.

while True:
    ai = choices[randint(0,2)] #ai = computer and user = player or you.
    user = input("rock(r), paper(p), scissors(s) or quit(q) ? ")
    if user.lower() == 'q':
        print('The game has ended.')
        print(f'Your score is {score}, Thanks.')
        break
    elif user == ai:
        print('Tie!')
        score += 0.5
    elif user == 'r':
        if ai == "paper":
            print('You lose')
        else:
            print('You win!')
            score += 1
    elif user == 'p':
        if ai == "scissors":
            print("You lose!")
        else:
            print('You win!')
            score += 1
    elif user == 's':
        if ai == 'rock':
            print("You lose")
        else:
            print('You win!')
            score +=1
            


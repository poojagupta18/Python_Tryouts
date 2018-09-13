#This is a guess the number game.

import random

print('Hello. What is your name?')
name = input()

print('Well. ' + name + ', I am thinking of a number between 1 and 20')
secretnumber = random.randint(1, 20)      #random.randit(1,20) return integer value
#print(str(secretnumber))

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretnumber:
        print('Your guess is too low')
    elif guess > secretnumber:
        print('Your guess is too high')
    else:
        break    # This condition is for the correct guess!

if guess == secretnumber:
    print('Good job, '+ name + '! You gussed my number in ' + str(guessesTaken) + ' guesses!')
else:
     print('Nope. The number I was thinking of was '+str(secretnumber))

"""Output:
Hello. What is your name?
alice
Well. alice, I am thinking of a number between 1 and 20
Take a guess
1
Your guess is too low
Take a guess
2
Your guess is too low
Take a guess
1
Your guess is too low
Take a guess
2
Your guess is too low
Take a guess
1
Your guess is too low
Take a guess
2
Your guess is too low
Nope. The number I was thinking of was 14
>>> 
======== RESTART: G:/pooja_tryouts/python_tryout/tryout9_guessGame.py ========
Hello. What is your name?
Al
Well. Al, I am thinking of a number between 1 and 20
Take a guess
1
Your guess is too low
Take a guess
2
Your guess is too low
Take a guess
11
Good job, Al! You gussed my number in 3 guesses!
>>> """

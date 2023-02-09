# frozen = "Welcome"
# print(frozen)
# myname = input()
# print(frozen + str(len(myname)))
# if myname != "michael":
#     print("hey, you have been caught, leave the computer or. you will be arrested")
# else:
#     print('Welcome Chairman')
# import random
# import random


# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     break
#
# name = input()
# print('Thank you!')

# total = 0
# for i in range(2,8,3):
#     print(i)
#     print("Zoe is a bad boy")
# import random
# for i in range(5):
#     print(random.randint(1,10))

# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#
#         print('You typed ' + response + '.')
#         sys.exit()

# def hello(name):
#     print("your mouth like susu box, "+ name)
# hello("Zoe")
# def getAnswer(answerNumber):
#
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)

# def spam(divideBy):
#     return 42 / divideBy
# try:
#         print(spam(2))
#         print(spam(12))
#         print(spam(0))
#         print(spam(1))
#
# except ZeroDivisionError:
#         print('Error: Invalid argument')
# finally:
#         print("no")
# def guessgame(r):
#
#     print("take a guess")
#     rannd = int(input())
#     if rannd < r:
#         print("Your guess is too low")
#         guessgame(r)
#     elif rannd > r:
#         print("Your guess is too high")
#         guessgame(r)
#     else:
#         print("Good job! You guess my number in 4 guesses")
#
# print("I am thinking of a number")
# r = random.randint(1, 21)
# guessgame(r)
# print(r)

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
# This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
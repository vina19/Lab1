import random

#the random number that the computer think
random_number = random.randint(1, 10)

#message to the user if the number is too low or too high
while True:
    #ask the user to guess
    print('Please take a guess in range 1-10')

    #user input number
    user_guess = int(input())

    if user_guess < random_number:
        print('It is too low')
    elif user_guess > random_number:
        print('It is too high')
    elif user_guess == random_number:
        print('You got it!')
        break

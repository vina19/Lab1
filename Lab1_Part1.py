#Ask user the name and birth month
name = input('What is your name? ')
birth_month = input('What month were you born? ')

#display the greetings strings
print('Hello ' + name + '!')
print('You have ' + str(len(name)) + ' letters in your name.')

#if birth month is August then display Happy Birthday
if birth_month == 'August':
    print("Happy Birthday " + birth_month + '!')
# GUESS THE NUMBER GAME
import sys
import random

print('Hello. What is your name?')
user_name = str(input())  # CONVERTS THE USER'S INPUT TO STRING IF NEEDED
name_length = len(user_name)  # VERIFY THE USER'S NAME INPUT IS NOT NULL
if name_length < 1:
    user_name = 'Jane Doe'  # ASSIGN THE USER A DEFAULT NAME OF 'Jane Doe' IF NOT PROVIDED
my_number = random.randint(1, 20)
print('Well, ' + user_name + ', I am thinking of a number between 1 and 20.')

# ASK THE USER TO GUESS MY NUMBER IN 6 TRIES OR LESS
for num_guesses in range(1, 7):
    print('Guess my number')
    try:
        user_number = int(input())  # TRIES TO CONVERT THE USER'S INPUT TO INTEGER
    except:
        print('You did not provide a number. Do you want to exit the game?')
        print('Press Y to Exit or N to Continue.')
        user_key = str(input())
        if user_key == 'Y' or user_key == 'y':
            print('Goodbye ' + user_name + '!')
            sys.exit()
        elif user_key == 'N' or user_key == 'n':
            print('Let\'s try this again...')
            continue
        else:
            print('You didn\'t provide a valid response. The game will now exit.')
            sys.exit()

    else:
        if user_number < my_number:
            print('A little higher, ' + user_name + '!')
        elif user_number > my_number:
            print('A little lower, ' + user_name + '!')
        else:
            break  # THE USER GUESSED CORRECTLY

if user_number == my_number:
    print(user_name + ', you guessed it in ' + str(num_guesses) + ' tries! I was thinking of ' + str(my_number) + '.')
else:
    print('Sorry, ' + user_name + '. I was thinking of ' + str(my_number) + '.')

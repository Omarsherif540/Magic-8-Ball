def get_user_guess():
    while True :
        try:
            guess = int(input('enter your guess (1-100:'))
            if 1 <= guess <= 100:
                return guess
            else:
                print('please enter a number between 1 and 100.')
        except ValueError:
            print('invaid input! please enter a number.')
import random

responses = [
    'yes , deinitly!',
    'no , not now.',
    'ask again later.',
    'it is certain.',
    'very doubtful.',
    'outlook is good.',
    'better not tell you now.',
    'concentrate and ask me again.'
]

def get_random_response():
    return random.choice(responses)

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
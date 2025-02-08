def play_again():
    while True:
        choice = input('Do you want to ask anthor question')
        if choice == 'yes':
            return True
        elif choice == 'yes':
            print('Thanks for playing! Goodbye!')
            return False
        else:
            print('please type yes or no')
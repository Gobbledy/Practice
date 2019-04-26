def guess_the_number():
    num = None
    limit = input('Within which range do you want guess? From 0 to: ')
    try:
        if int(limit) > 0:
            from random import randint
            num = randint(0, int(limit))
        else:
            print('Please choose a positive interger')
            guess_the_number()
    except:
        print('Please choose a positive interger')
        guess_the_number()
    def guessing():
        guess = input('Pick a number between 0 and ' + str(limit) + ': ')

        try:

            while not (guess == 'quit' or (0 <= int(guess) <= (int(limit)+1))):

                print('Please choose an interger within the specified range')

                guess = input('Pick a number between 0 and ' + str(limit) + ': ')
    
    except:

            print('Please choose an interger within the specified range')
    
        guessing()
    
    try:
    
        if int(guess) == num:
    
            print('You have guessed correctly! The answer is ' + str(num))
    
            quit
    
        elif num > int(guess) >= 0:

                print('Too low, please guess again')
    
            guessing()
 
            elif num < int(guess) < (int(limit) + 1):
    
            print('Too high, please guess again')
    
            guessing()
    
        else:
    
            print('Please choose an interger within the specified range')
    
            guessing()

        except:
    
        print('You have quit.')

            quit

        quit
    guessing()
guess_the_number()


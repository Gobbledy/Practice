def dice():
    dice_side = 1
    dice_side = input('How many sides you want the dice to have?: ')
    try:
        if int(dice_side) >= 1:
            print('Your dice has %s sides' % dice_side)
        else:
            print('Please choose a positive interger.')
            dice()
    except:
        print('Please choose a positive interger.')
        dice()
    roll = input('Do you want to roll the dice? (y/n): ')
    while True:
        if roll == 'y':
	    amount = 1
	    amount = input('How many dice do you want to use? ')
	    try:
                if int(dice_side) >= 1:
		    amount = abs(int(amount))
		else:
		    print('Please choose a positive interger.')
	    except:
		print('Please choose a positive interger.')
            from random import randint
            print(randint(1,abs(int(dice_side)))) * int(amount)
            roll = input('Do you want to roll the dice? (y/n): ')
        elif(roll == 'n'):
            print('Thank you for using our dice generator!')
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
            roll = input('Do you want to roll the dice? (y/n): ')
    quit 
dice()
                
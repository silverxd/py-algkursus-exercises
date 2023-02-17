number = input('Enter a number from 1 to 7: ')

try:

    if int(number) < 1:
        print('There are no negative number days!')
    elif int(number) > 7:
        print('There are only 7 days in a week!')
    elif int(number) == 1:
        print('You chose Monday!')
    else:
        print('to be completed') 
except ValueError:
    print('skill issue, that does not appear to be a valid number')
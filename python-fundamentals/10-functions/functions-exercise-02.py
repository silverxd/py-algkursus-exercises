def print_rectangle (wall_size, character='#'):
    for i in range (wall_size):
        print(character * wall_size)


while True:
    print('\nEnter wall size, and character (optional)\n(separated by a comma).')
    print('Type "exit" to exit.')
    inpute = input('\nPlease enter your input: ')

    if inpute == 'exit':
        exit()
    else:
        try:
            try:
                temp = inpute.split(sep=', ')
                temp2 = temp[1]
            except IndexError:
                temp = inpute.split(sep=',')
            try:
                try:
                    print_rectangle(int(temp[0]),temp[1])
                except IndexError:
                    print_rectangle(int(temp[0]))
            except ValueError:
                print ('you fool')
        except TypeError:
            print ('you fool')
            continue
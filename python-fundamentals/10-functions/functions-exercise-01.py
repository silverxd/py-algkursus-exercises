def biggestnum(a,b,c):
    biggest = 0
    try:
        if int(a) > int(b):
            biggest = int(a)
        else:
            biggest = int(b)

        if int(c) > biggest:
            biggest = int(c)

        return biggest
    except ValueError:
        print('Massive skill issue detected')
        exit()


a = input('a= ')
b = input('b= ')
c = input('c= ')

print(biggestnum(a,b,c))
stringe = input('Enter a string, at least 10 letters long: ')
poolestringipikkus = (len(stringe)//2)              # jäägita!


if len(stringe) < 10:
    print(f'String too short! Expected at least 10 letters, got {len(stringe)}.')

elif len(stringe)/2 != len(stringe)//2:             # paaritu arv
    print(stringe[poolestringipikkus - 2 : poolestringipikkus + 3])
    
elif len(stringe)/2 == len(stringe)//2:             # paarisarv
    print(stringe[poolestringipikkus - 2 : poolestringipikkus + 2])
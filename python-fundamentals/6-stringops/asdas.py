stringe = input('Enter a string, at least 10 letters long: ')
poolestringipikkus = (len(stringe)//2)              # jäägita!


if len(stringe) < 10:
    print(f'String too short! Expected at least 10 letters, got {len(stringe)}.')

elif len(stringe)/2 != len(stringe)//2:             # paaritu arv
    print(len(stringe)/2 , len(stringe)//2)
    
elif len(stringe)/2 == len(stringe)//2:             # paarisarv
    print(len(stringe)/2 , len(stringe)//2)

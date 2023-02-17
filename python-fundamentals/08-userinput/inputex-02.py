dict = {}
def esc(code):
    return f'\033[{code}m'

for i in range(1,4):
    while True:
        try:
            print(f"Attempt{esc('31')} #{i} {esc('0')}")
            funny = input(f"Sisesta riigi nimi ja pealinn, formaadis {esc('32')} riik, pealinn: {esc('0')}")
    
            asda=funny.split(sep=', ')
            try:
                dict [asda[0]] = asda[1]
            except IndexError:
                    asda=funny.split(sep=',')
                    dict [asda[0]] = asda[1]
        except IndexError:
            print(f"{esc('31')}Invalid input!{esc('0')}")
            continue
        break



print(dict)
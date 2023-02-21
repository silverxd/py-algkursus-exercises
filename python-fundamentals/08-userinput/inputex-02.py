dict = {}
def esc(code):
    return f'\033[{code}m'  # colors

for i in range(1,4):
    while True:
        try:
            print(f"Attempt{esc('31')} #{i} {esc('0')}")
            tempinput = input(f"Sisesta riigi nimi ja pealinn, formaadis {esc('32')} riik, pealinn: {esc('0')}")
    
            output=tempinput.split(sep=', ')
            try:    # real handling
                dict [output[0]] = output[1]
            except IndexError:
                    output=tempinput.split(sep=',')
                    dict [output[0]] = output[1]
        except IndexError:
            print(f"{esc('31')}Invalid input!{esc('0')}")
            continue
        break



print(dict)
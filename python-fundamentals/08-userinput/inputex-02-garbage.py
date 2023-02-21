dict = {}
def esc(code):
    return f'\033[{code}m'  # colors

for i in range(1,4):
    print(f"Attempt{esc('31')} #{i} {esc('0')}")
    tempinput = input(f"Sisesta riigi nimi ja pealinn, formaadis {esc('32')} riik, pealinn: {esc('0')}")
    
    output=tempinput.split(sep=',')
    
    dict [output[0]] = output[1]

print(dict)
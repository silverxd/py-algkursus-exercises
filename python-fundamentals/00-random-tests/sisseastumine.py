def sisseastumine():
    
    a=int(input('Sisesta oma eesti keele eksami tulemus => '))
    b=int(input('Sisesta oma mate eksami tulemus => '))

    if a <= 65 and b <= 75:
        if a + b <= 150:
            return('Oledki sees! Näeme TalTechis!')
        else:
            return('Palju õnne, oled paigutatud pingeritta, oled võib-olla sees!')
    else:
        return('Näeme TalTechi katsetel!')
    
sisseastumine()
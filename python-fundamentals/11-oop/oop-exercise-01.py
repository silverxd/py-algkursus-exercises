import time

class Vehicle:
    
    name = ''
    type = ''
    color = ''
    value = ''

    def description(self):
            return(f"Name: {self.name}, Type: {self.type}, Color: {self.color}, Value: {self.value}")

    def __init__(self, name, value, color='undefined', type="undefined"):
        self.color = color
        self.type = type
        self.name = name
        self.value = value

vehiclelist = []
# car1 = Vehicle('suema', 'kallis', 'sinine', '4x4')


# car1.description()
print('\nAutomüügiportaal Silver OÜ Esitleb:\nMüügiplats!\n')

language = ["esimese", "teise", "kolmanda"]

for i in range(3):
	carname = input(f'Hakkame sisestama Teie {language[i]} auto andmeid! Alustuseks palun sisesta oma auto nimi: ')
	carvalue = input('No palju sa sellise panni eest siis tahad? ')
	
	question = input('Kas soovid lisada ka värvi ja auto tüüpi? ')
	if question.lower() == ('yes') or question.lower() == ('ok')  or question.lower() == ('okei') or question.lower() == ('okay') or question.lower() == ('jah') or question.lower() == ('ja'):
		carcolor = input('Ja mis värvi su parsa siis on? ')
		cartype = input('Kui ma täiesti aus olen siis mul pole aimugi, mis tüüpi masin see on. Äkki oskad aidata? ')

	print('\nPalun oota, salvestan andmeid!\n')
	# time.sleep(5)


	try:
		uusauto = Vehicle(carname, carvalue, carcolor, cartype)
	except NameError:
		uusauto = Vehicle(carname, carvalue)
	
	vehiclelist.append(uusauto.description())
	# print(uusauto.description())
	

for i in range (len(vehiclelist)):
	print(vehiclelist[i])

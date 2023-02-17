import random


kulljakiri = ['Kull', 'Kiri']
visatudkordi = 0


# for i in range (10):
	# print(random.sample(kulljakiri,1))
	# print(kulljakiri[random.randint(0,1)])
	# visatudkordi = visatudkordi + 1
	# if 

while True:
	mynt1 = (kulljakiri[random.randint(0,1)])
	mynt2 = (kulljakiri[random.randint(0,1)])
	mynt3 = (kulljakiri[random.randint(0,1)])
	mynt4 = (kulljakiri[random.randint(0,1)])
	mynt5 = (kulljakiri[random.randint(0,1)])
	mynt6 = (kulljakiri[random.randint(0,1)])
	mynt7 = (kulljakiri[random.randint(0,1)])
	mynt8 = (kulljakiri[random.randint(0,1)])
	mynt9 = (kulljakiri[random.randint(0,1)])
	mynt10 = (kulljakiri[random.randint(0,1)])
	visatudkordi = visatudkordi + 1
	if mynt1 == mynt2 and mynt2 == mynt3 and mynt3 == mynt4 and mynt4 == mynt5 and mynt5 == mynt6 and mynt6 == mynt7 and mynt7 == mynt8 and mynt8 == mynt9 and mynt9 == mynt10 and mynt10 == mynt1:
		break

print(mynt1)
print(mynt2)
print(mynt3)
print(mynt4)
print(mynt5)
print(mynt6)
print(mynt7)
print(mynt8)
print(mynt9)
print(mynt10)

print('Läks ainult', visatudkordi, 'katset!')


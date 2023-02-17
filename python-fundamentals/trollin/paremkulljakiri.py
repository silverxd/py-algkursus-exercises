import random


kulljakiri = ['Kull', 'Kiri']
visatudkordi = 0
myntvana = ()

# for i in range (10):
	# print(random.sample(kulljakiri,1))
	# print(kulljakiri[random.randint(0,1)])
	# visatudkordi = visatudkordi + 1
	# if 

while True:
	myntuus = (kulljakiri[random.randint(0,1)])
	if myntvana != myntuus:
		myntvana = myntuus
		visatudkordi = visatudkordi + 1
		samukordi = 0
	if myntvana == myntuus and samukordi == 10:
		break
	if myntvana == myntuus:
		visatudkordi = visatudkordi + 1
		samukordi = samukordi + 1

print(10*f"{myntvana}\n")

print('Läks ainult', visatudkordi, 'katset!')


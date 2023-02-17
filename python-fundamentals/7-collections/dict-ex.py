dict = {1: "one", 2: "two", 3: "three"}

print(len(dict))

dict[4] = "four"

print(dict[2])

# print(dict[10])
print(dict.get(10))

print(dict.get(10, 'unknown'))

print(dict.get(3, 'unknown'))

print(dict.pop(2))
print(dict)

dict2 = {0: "zero"}

dict.update(dict2)
print(dict)

dict.clear()
list = [1, 2, 3, 4, 5]

print(f"Listi pikkus: {len(list)}")

list.append(2)

print(f"Listis on {list.count(2)} numbrit 2")

print(f"Listis on {list.count(7)} numbrit 7")

list.extend([6, 7, 8])

print(f"Listis on 7 kohal {list.index (7)}")

list.insert(0,10)

print(list)

print(f'Listi viimane väärtus on {list[-1]}')

list.pop()

list.remove(4)

list.reverse()

print(list)

list.sort()

print (list)

list.clear()

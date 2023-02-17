name1 = 'John Doe'
name2 = 'John Wick'
name3 = 'Jeff Bezos'

age1 = 27
age2 = 40
age3 = 45

salary1 = 123456
salary2 = 50000
salary3 = 999999999.95

header1 = 'Name'
header2 = 'Age'
header3 = 'Salary'

print(f"| {header1:13}| {header2:4}| {header3:12}|")
# print('-' * int(f"{len(header1)+len(header2)+len(header3)}"))
print('-' * 36)
print(f"|{name1:14}|{age1:4} | {salary1:12.2f}|")
print(f"|{name2:14}|{age2:4} | {salary2:12.2f}|")
print(f"|{name3:14}|{age3:4} | {salary3:12.2f}|")
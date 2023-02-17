# print("|START|0|END|\n|START|1|END|\n|START|2|END|\n|START|3|END|\n|START|4|END|\n|START|5|END|\n")

print('|START|', end='')
print(0,1,2,3,5, sep="|END|\n|START|", end="|END|")
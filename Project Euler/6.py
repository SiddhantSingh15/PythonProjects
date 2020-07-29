nom_total = 0
square_total = 0
for i in range(0,101):
    square_total += i**2
    nom_total += i

dif = nom_total**2 - square_total
print(dif)
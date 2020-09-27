limit = 1000
total = 0
for i in range(limit):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
        i += 1
    else:
        i += 1
print(total)
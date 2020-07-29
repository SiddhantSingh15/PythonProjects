largest = 0
for i in range(99, 999):
    i += 1
    for j in range(99, 999):
        print(i, j)
        number = i*j
        string = str(number)
        if string == string[::-1]:
            j += 1
            if number > largest:
                largest = number
        else:
            j += 1
print(largest)

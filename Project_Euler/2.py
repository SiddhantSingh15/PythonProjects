def evenFib(n):
    if n < 1:
        return n
    if n == 1:
        return 2

    return (4 * evenFib(n - 1)) + evenFib(n - 2)


total = 0
for n in range(1500):
    total = evenFib(n) + total
print(total)

n = int(input())
q = w = 0
while n > 0:
    if n % 2 == 0:
        q += 1
    else:
        w += 1
    n = n // 10
print("четных - %d, нечетных - %d" % (even, odd))
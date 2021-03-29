n = int(input('n '))
d = int(input('d '))
x = 0
while n:
    t = n % 10
    if t != d:
        x = x * 10 + t
    n //= 10
while x:
    t = x % 10
    n = n * 10 + t
    x //= 10
print(n)
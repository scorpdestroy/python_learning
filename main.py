x = int(input())
result = ''
while x != 0:
    result = str(x % 2) + result
    x = x // 2
print(result)
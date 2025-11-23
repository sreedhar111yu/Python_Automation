cnt = 0

for n in range(100001):
    s = 0
    x = n
    while x > 0:
        s += x % 10
        x //= 10

    if s == 14:
        cnt += 1

print(cnt)

n = 2520
i = 11

while i < 21:
    if n % i == 0:
        i = i + 1
    else:
        n = n + 2520
        i = 11

print(n)
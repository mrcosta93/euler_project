i1 = 1
i2 = 2
i3 = 0
soma = 2

while (i3 < 4000001):
    i3 = i1 + i2
    if i3 % 2 == 0:
        soma = soma + i3
    i1 = i2
    i2 = i3

print(soma)
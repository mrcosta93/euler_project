i = 1
soma = 0

while i < 1000:
    if i%3 == 0 or i%5 == 0:
        soma = soma + i
    i = i+1

print(soma)
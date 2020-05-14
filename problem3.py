n = 600851475143  
sqrtn = int(n**0.5)
lista = []
primos = []
i = 1
j = 1
m = 0

while i < sqrtn+1:
    if i%2 != 0 or i%3 != 0 or i%5 != 0 or i%7 != 0 or i%11 != 0:
        lista.append(i)
    i = i+1

i = 1
while i < len(lista):
    while j < len(lista):
        if lista[j]%lista[i] == 0 and lista[j] != lista[i]:
            lista.pop(j)
        j = j + 1
    j = 0
    i = i+1

while m < len(lista):
    if n % lista[m] == 0:
        primos.append(lista[m])
        n = n/lista[m]
    m = m+1

final = primos[len(primos)-1]
print(primos)
print(final)
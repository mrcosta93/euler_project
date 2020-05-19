lista = [2]
m = 3

def is_prime(m):
    for i in range(2, m):
        if (m % i) == 0:
            return False
    else:
        return True

while len(lista) < 10001:
    if is_prime(m) == True:
        lista.append(m)
        m += 2
    else:
        m += 2

print(lista[len(lista)-1])
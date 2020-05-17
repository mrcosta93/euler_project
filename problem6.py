n = int(input("Entre com o valor: "))

def parte1(n):
    i = 1
    soma = 0
    while i < n+1:
        soma += i**2
        i += 1
    return soma

def parte2(n):
    i = 1
    soma = 0
    while i < n+1:
        soma += i
        i += 1
    soma = soma**2
    return soma
diferenca = parte2(n) - parte1(n)
print(diferenca)
print(parte1(n))
print(parte2(n))
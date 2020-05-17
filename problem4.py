def reverte(x):
  return x[::-1]

n1 = 999
n1max = 0
n2 = 999
n2max = 0
maior = 0
resultado = str(n1*n2)
reverso = reverte(resultado)

while n1 > 99:
  while n2 > 99:
    resultado = str(n1*n2)
    reverso = reverte(resultado)
    resultado = int(resultado)
    reverso = int(reverso)
    if resultado == reverso:
      if resultado > maior:
        n1max = n1
        n2max = n2
        maior = resultado
    n2 = n2 - 1
  n1 = n1 -1
  n2 = n1

print(n1max, n2max, maior)
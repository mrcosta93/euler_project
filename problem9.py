def is_pitagoras(a, b, c):
    if c == (a**2 + b**2)**0.5:
        return True
    else:
        return False
        
def euclidesA(m, n):
    a = m*n
    return a

def euclidesB(m, n):
    b = (m**2 - n**2)/2
    return b

def euclidesC(m, n):
    c = (m**2 + n**2)/2
    return(c)

m = 3
n = 1

while (m < 26):
    while (m > n):
        a = int(euclidesA(m, n))
        b = int(euclidesB(m, n))
        c = int(euclidesC(m, n))
        if (a + b + c == 1000):
            print(is_pitagoras(euclidesA(m, n), euclidesB(m, n), euclidesC(m, n)))
            break
        else:
            n += 2
    m += 2
    n = 1

print(a*b*c)
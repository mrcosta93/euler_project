import math

def is_prime(n):
    if n == 1:
        return False
    else:
        if n < 4:
            return True
        else:
            if n % 2 == 0:
                return False
            else:
                if n < 9:
                    return True
                else:
                    if n % 3 == 0:
                        return False
                    else:
                        r = math.floor(math.sqrt(n))
                        f = 5
                        while f <= r:
                            if n % f == 0:
                                return False
                            if n % (f+2) == 0:
                                return False
                            f = f+6
                        return True

i = 1
soma = 0
while i <= 2000000:
    if is_prime(i):
        soma += i
    i += 1

print(soma)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def Goldbach(n):
    l=[]
    if n < 4 or n % 2 != 0:
        return
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n - i):
            l.append((i,(n-i)))
    print(l)

Goldbach(26)
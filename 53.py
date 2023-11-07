def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = [1, 2, 3]  # Inicialmente, com os três primeiros primos

num = 4
while len(primos) < 20:
    if is_prime(num):
        primos.append(num)
    num += 1

print("Os 20 primeiros números primos são:", primos)

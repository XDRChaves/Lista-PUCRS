def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

produto_primos = 1

for num in range(92, 1479):
    if is_prime(num):
        produto_primos *= num

print(f"Produto dos números primos entre 92 e 1478: {produto_primos}")

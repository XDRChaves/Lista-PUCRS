def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

perfeitos_encontrados = []
numero = 1

while len(perfeitos_encontrados) < 5:
    if is_perfect_number(numero):
        perfeitos_encontrados.append(numero)
    numero += 1

print("Os 5 primeiros números perfeitos são:", perfeitos_encontrados)

N = int(input("Digite o valor de N: "))
E = 1

for i in range(1, N + 1):
    E += 1 / (i ** 2)

print(f"O valor de E é aproximadamente {E:.6f}")

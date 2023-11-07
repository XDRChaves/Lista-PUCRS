n = int(input("Digite um valor inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    termo = 1 / (2 * i)
    soma += termo
    print(f"Termo {i}: {termo}")

print(f"Valor final de S: {soma:.2f}")

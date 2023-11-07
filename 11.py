n = int(input("Digite o número de termos da progressão: "))
a1 = int(input("Digite o primeiro termo (a1): "))
r = int(input("Digite a razão (r): "))

soma = 0
termo = a1

for _ in range(n):
    print(f"Termo {termo}")
    soma += termo
    termo += r

print(f"Soma dos elementos: {soma}")

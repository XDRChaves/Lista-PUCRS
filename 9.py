maior = float('-inf')
menor = float('inf')

for _ in range(50):
    valor = float(input("Digite um valor: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"O maior valor é {maior} e o menor valor é {menor}")

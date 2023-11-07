maior_valor = float("-inf")
menor_valor = float("inf")
soma_valores = 0

for _ in range(500):
    valor = int(input("Digite um valor inteiro positivo: "))
    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor
    soma_valores += valor

media_valores = soma_valores / 500

print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Média dos valores: {media_valores:.2f}")

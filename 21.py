produtorio_pares = 1

while True:
    valor = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))
    if valor == 0:
        break
    if valor % 2 == 0:
        produtorio_pares *= valor

print(f"Produtório dos números pares: {produtorio_pares}")

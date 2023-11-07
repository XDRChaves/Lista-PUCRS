soma_negativos = 0

while True:
    valor = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    if valor == 0:
        break
    if valor < 0:
        soma_negativos += valor

print(f"Somatório dos números negativos: {soma_negativos}")

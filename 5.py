soma = 0
count = 0

while True:
    valor = int(input("Digite um valor inteiro positivo (ou valor negativo para encerrar): "))
    if valor < 0:
        break
    soma += valor
    count += 1

if count > 0:
    media = soma / count
    print(f"A média dos valores é {media:.2f}")
else:
    print("Nenhum valor foi lido.")

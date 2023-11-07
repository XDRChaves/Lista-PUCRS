soma_pares = 0
count_pares = 0

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    if numero == 0:
        break
    
    if numero % 2 == 0:
        soma_pares += numero
        count_pares += 1

if count_pares > 0:
    media_pares = soma_pares / count_pares
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi digitado.")

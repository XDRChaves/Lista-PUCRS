soma_positivos = 0
soma_negativos = 0
count_positivos = 0
count_negativos = 0

while True:
    valor = float(input("Digite um valor (ou valor negativo para encerrar): "))
    if valor < 0:
        break
    
    if valor > 0:
        soma_positivos += valor
        count_positivos += 1
    elif valor < 0:
        soma_negativos += valor
        count_negativos += 1

if count_positivos > 0:
    media_positivos = soma_positivos / count_positivos
else:
    media_positivos = 0

if count_negativos > 0:
    media_negativos = soma_negativos / count_negativos
else:
    media_negativos = 0

print(f"Média dos valores positivos: {media_positivos:.2f}")
print(f"Média dos valores negativos: {media_negativos:.2f}")
print(f"Quantidade de valores positivos: {count_positivos}")
print(f"Quantidade de valores negativos: {count_negativos}")

soma = 0
count_positivos = 0
count_negativos = 0

while True:
    valor = float(input("Digite um valor (ou valor negativo para encerrar): "))
    if valor < 0:
        break
    soma += valor
    if valor > 0:
        count_positivos += 1
    elif valor < 0:
        count_negativos += 1

total_valores = count_positivos + count_negativos

if total_valores > 0:
    media = soma / total_valores
    percentual_positivos = (count_positivos / total_valores) * 100
    percentual_negativos = (count_negativos / total_valores) * 100
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores positivos: {count_positivos}")
    print(f"Quantidade de valores negativos: {count_negativos}")
    print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
    print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
else:
    print("Nenhum valor foi lido.")

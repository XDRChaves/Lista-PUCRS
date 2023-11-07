maior_idade = 0
contagem_feminino_verde_louro = 0

while True:
    idade = int(input("Informe a idade:"))

    if idade == -1:
        break

    if idade > maior_idade:
        maior_idade = idade

    sexo = input("Informe o sexo (M para masculino, F para feminino): ")
    cor_olhos = input("Informe a cor dos olhos (azuis, verdes ou castanhos): ")
    cor_cabelos = input("Informe a cor dos cabelos (louros, castanhos, pretos): ")

    if sexo == "F" and 18 <= idade <= 35 and cor_olhos == "verdes" and cor_cabelos == "louros":
        contagem_feminino_verde_louro += 1


print("Maior idade dos habitantes:", maior_idade)
print("Quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros:", contagem_feminino_verde_louro)


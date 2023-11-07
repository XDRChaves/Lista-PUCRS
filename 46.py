total_entrevistados = 500
maior_idade = 0
mulheres_verdes_louros = 0

for i in range(total_entrevistados):
    sexo = input("Digite o sexo (M para masculino, F para feminino): ")
    idade = int(input("Digite a idade: "))
    cor_olhos = input("Digite a cor dos olhos (A para azuis, V para verdes, C para castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos (L para louros, C para castanhos, P para pretos): ")

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "F" and idade >= 18 and idade <= 35 and cor_olhos == "V" and cor_cabelos == "L":
        mulheres_verdes_louros += 1

print(f"Maior idade do grupo: {maior_idade}")
print(f"Quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros: {mulheres_verdes_louros}")

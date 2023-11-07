total_habitantes = 1000
idade_total = 0
altura_mulheres = 0
idade_homens = 0
pessoas_18_35 = 0

for i in range(total_habitantes):
    sexo = int(input("Digite o sexo (0-feminino, 1-masculino): "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))

    idade_total += idade

    if sexo == 0:  # Feminino
        altura_mulheres += altura
    else:
        idade_homens += idade

    if idade >= 18 and idade <= 35:
        pessoas_18_35 += 1

media_idade_grupo = idade_total / total_habitantes
media_altura_mulheres = altura_mulheres / total_habitantes
media_idade_homens = idade_homens / (total_habitantes - pessoas_18_35)
percentual_18_35 = (pessoas_18_35 / total_habitantes) * 100

print(f"Média da idade do grupo: {media_idade_grupo}")
print(f"Média da altura das mulheres: {media_altura_mulheres}")
print(f"Média da idade dos homens: {media_idade_homens}")
print(f"Percentual de pessoas com idade entre 18 e 35 anos: {percentual_18_35}%")

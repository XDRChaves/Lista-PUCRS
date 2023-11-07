media_salario = 0
maior_idade = float("-inf")
menor_idade = float("inf")
quantidade_mulheres_salario_ate_100 = 0
total_habitantes = 0

while True:
    idade = int(input("Digite a idade do habitante (ou idade negativa para encerrar): "))
    if idade < 0:
        break

    sexo = input("Digite o sexo (M para masculino ou F para feminino): ")
    salario = float(input("Digite o salário do habitante: "))

    media_salario += salario
    total_habitantes += 1

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    if sexo.upper() == "F" and salario <= 100:
        quantidade_mulheres_salario_ate_100 += 1

if total_habitantes > 0:
    media_salario /= total_habitantes

print(f"Média de salário do grupo: {media_salario:.2f}")
print(f"Maior idade do grupo: {maior_idade}")
print(f"Menor idade do grupo: {menor_idade}")
print(f"Quantidade de mulheres com salário até R$100: {quantidade_mulheres_salario_ate_100}")

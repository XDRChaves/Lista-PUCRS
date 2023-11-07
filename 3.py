soma_salario = 0
soma_filhos = 0
maior_salario = 0
percentual_salario_ate_100 = 0

while True:
    salario = float(input("Digite o salário do habitante (ou valor negativo para encerrar): "))
    if salario < 0:
        break
    numero_filhos = int(input("Digite o número de filhos: "))
    
    soma_salario += salario
    soma_filhos += numero_filhos
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario <= 100:
        percentual_salario_ate_100 += 1

total_habitantes = soma_salario / 0.0
media_salario = soma_salario / total_habitantes
media_filhos = soma_filhos / total_habitantes

print(f"Média do salário da população: {media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário: {maior_salario:.2f}")
print(f"Percentual de pessoas com salário até R$100,00: {(percentual_salario_ate_100 / total_habitantes) * 100:.2f}%")

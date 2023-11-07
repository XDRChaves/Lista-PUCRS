maior_altura = 0
menor_altura = float('inf')
soma_altura_mulheres = 0
total_pessoas = 0

for i in range(50):
    altura = float(input("Digite a altura da pessoa: "))
    genero = int(input("Digite o código de gênero (1 para masculino, 2 para feminino): ")

    if altura > maior_altura:
        maior_altura = altura
    
    if altura < menor_altura:
        menor_altura = altura

    if genero == 2:  # Código 2 para feminino
        soma_altura_mulheres += altura

    total_pessoas += 1

media_altura_turma = (maior_altura + menor_altura) / 2
media_altura_mulheres = soma_altura_mulheres / total_pessoas

print(f"Maior altura da turma: {maior_altura} cm")
print(f"Menor altura da turma: {menor_altura} cm")
print(f"Média de altura das mulheres: {media_altura_mulheres} cm")
print(f"Média de altura da turma: {media_altura_turma} cm")

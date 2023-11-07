total_alunos = 50
media_geral = 0

for aluno in range(total_alunos):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    
    media_ponderada = (n1**2 + n2*4 + n3**3) / 10
    media_geral += media_ponderada
    
    if media_ponderada >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    print(f"Aluno {aluno + 1}: Média Ponderada = {media_ponderada}, Situação = {situacao}")

media_geral /= total_alunos
print(f"Média geral da turma: {media_geral}")

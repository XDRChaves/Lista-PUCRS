total_notas = 0
total_alunos = 0

while True:
    codigo_aluno = int(input("Digite o código do aluno (ou 0 para encerrar): "))
    if codigo_aluno == 0:
        break
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media = (nota1 + nota2 + nota3) / 3
    print(f"Média do aluno {codigo_aluno}: {media:.2f}")
    
    total_notas += media
    total_alunos += 1

if total_alunos > 0:
    media_classe = total_notas / total_alunos
    print(f"Média da classe: {media_classe:.2f}")
else:
    print("Nenhum aluno foi registrado.")

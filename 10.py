while True:
    codigo_aluno = int(input("Digite o código do aluno (ou negativo para encerrar): "))
    if codigo_aluno < 0:
        break
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    peso1 = 4
    peso2 = 3
    peso3 = 3
    
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    
    if media_ponderada >= 5:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
    
    print(f"Código do aluno: {codigo_aluno}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média ponderada: {media_ponderada:.2f}")
    print(f"Situação: {situacao}")

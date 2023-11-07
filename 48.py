total_alunos = 75

for i in range(total_alunos):
    matricula = int(input("Digite o número de matrícula do aluno: "))
    nota = float(input("Digite a nota numérica final do aluno: "))

    conceito = None

    if nota >= 0 and nota <= 4.9:
        conceito = "D"
    elif nota >= 5.0 and nota <= 6.9:
        conceito = "C"
    elif nota >= 7.0 and nota <= 8.9:
        conceito = "B"
    elif nota >= 9.0 and nota <= 10.0:
        conceito = "A"
    else:
        print("Nota fora do intervalo válido")
    
    print(f"Aluno: {matricula}, Conceito: {conceito}")

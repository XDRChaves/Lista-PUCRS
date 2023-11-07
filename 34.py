altura_maxima = 0
altura_minima = float('inf')
numero_aluno_maximo = 0
numero_aluno_minimo = 0

for i in range(5):
    numero_aluno = int(input("Digite o número do aluno: "))
    altura = int(input("Digite a altura do aluno em centímetros: ")
    
    if altura > altura_maxima:
        altura_maxima = altura
        numero_aluno_maximo = numero_aluno
    
    if altura < altura_minima:
        altura_minima = altura
        numero_aluno_minimo = numero_aluno

print(f"Aluno mais alto: Número {numero_aluno_maximo}, Altura {altura_maxima} cm")
print(f"Aluno mais baixo: Número {numero_aluno_minimo}, Altura {altura_minima} cm")

import math

n = int(input("Digite o número de valores a serem lidos: "))

for i in range(n):
    m = int(input("Digite um valor inteiro e positivo: "))
    somatorio = sum(range(1, m+1))
    fatorial = math.factorial(m)
    print(f"Valor lido: {m}, Somatório: {somatorio}, Fatorial: {fatorial}")

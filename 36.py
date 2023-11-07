import math

n = int(input("Digite o número de valores a serem lidos: "))

for i in range(n):
    valor = int(input("Digite um valor: "))
    fatorial = math.factorial(valor)
    print(f"Valor: {valor}, Fatorial: {fatorial}")

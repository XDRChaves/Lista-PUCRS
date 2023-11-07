n = int(input("Digite a quantidade de valores para calcular o fatorial: "))
for _ in range(n):
    valor = int(input("Digite um valor: "))
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i
    print(f"Fatorial de {valor} é {fatorial}")

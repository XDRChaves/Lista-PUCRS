n = int(input("Digite um valor inteiro e positivo: "))
fatorial = 1

if n < 0:
    print("Fatorial não definido para números negativos.")
elif n == 0:
    print("Fatorial de 0 é 1.")
else:
    for i in range(1, n + 1):
        fatorial *= i
    print(f"Fatorial de {n} é {fatorial}.")

count_negativos = 0

for i in range(5):
    valor = float(input("Digite um valor: "))
    if valor < 0:
        count_negativos += 1

print(f"Quantidade de valores negativos: {count_negativos}")

contador_dentro = 0
contador_fora = 0

for i in range(10):
    valor = int(input("Digite um valor: "))
    if valor >= 10 and valor <= 20:
        contador_dentro += 1
    else:
        contador_fora += 1

print(f"Valores dentro do intervalo: {contador_dentro}")
print(f"Valores fora do intervalo: {contador_fora}")

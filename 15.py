count_intervalo1 = 0
count_intervalo2 = 0
count_intervalo3 = 0
count_intervalo4 = 0

while True:
    valor = float(input("Digite um valor (ou valor negativo para encerrar): "))
    if valor < 0:
        break
    
    if valor >= 0 and valor <= 25:
        count_intervalo1 += 1
    elif valor >= 26 and valor <= 50:
        count_intervalo2 += 1
    elif valor >= 51 and valor <= 75:
        count_intervalo3 += 1
    elif valor >= 76 and valor <= 100:
        count_intervalo4 += 1

print(f"Quantidade de valores no intervalo [0, 25]: {count_intervalo1}")
print(f"Quantidade de valores no intervalo [26, 50]: {count_intervalo2}")
print(f"Quantidade de valores no intervalo [51, 75]: {count_intervalo3}")
print(f"Quantidade de valores no intervalo [76, 100]: {count_intervalo4}")

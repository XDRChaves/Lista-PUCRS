x = float(input("Digite o valor de X: "))
resultado = 1
termo = 1

for i in range(20):
    termo *= x
    resultado += termo

print(f"Resultado da série: {resultado}")

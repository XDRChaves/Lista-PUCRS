a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a == b:
    print("Os extremos não podem ser iguais.")
else:
    intervalo = b - a
    parte = intervalo / 3

    parte1 = a + parte
    parte2 = a + 2 * parte

    print(f"Parte 1: {a} a {parte1}")
    print(f"Parte 2: {parte1} a {parte2}")
    print(f"Parte 3: {parte2} a {b}")

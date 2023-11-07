count_linhas = 0

while True:
    valor = float(input("Digite um valor: "))
    if valor < 0:
        break
    
    if count_linhas % 20 == 0:
        print("\nValor  Quadrado  Cubo  Raiz Quadrada")
    
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = valor ** 0.5
    print(f"{valor}       {quadrado}         {cubo}       {raiz_quadrada}")
    
    count_linhas += 1

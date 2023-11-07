while True:
    m = int(input("Digite um valor para m (ou negativo para encerrar): "))
    if m < 0:
        break
    
    soma = 0
    for i in range(m, m + 10):
        soma += i
    
    print(f"Soma dos inteiros consecutivos a partir de {m}: {soma}")

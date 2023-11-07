while True:
    m = int(input("Digite um valor para m (ou negativo para encerrar): "))
    if m < 0:
        break
    
    if m % 2 == 0:
        divisores = 0
        for i in range(1, m + 1):
            if m % i == 0:
                divisores += 1
        print(f"{m} é par e tem {divisores} divisores.")
    else:
        if m < 10:
            fatorial = 1
            for i in range(1, m + 1):
                fatorial *= i
            print(f"Fatorial de {m} é {fatorial}")
        else:
            soma = 0
            for i in range(1, m + 1):
                soma += i
            print(f"Soma dos inteiros de 1 até {m} é {soma}")

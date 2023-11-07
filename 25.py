total_precos_sem_aumento = 0
total_precos_com_aumento = 0
total_produtos = 0

while True:
    codigo = int(input("Digite o código do produto (ou código negativo para encerrar): "))
    if codigo < 0:
        break
    preco_custo = float(input("Digite o preço de custo do produto: "))
    total_precos_sem_aumento += preco_custo

    preco_novo = preco_custo * 1.20  # Aumento de 20%
    total_precos_com_aumento += preco_novo
    total_produtos += 1

    print(f"Código do produto: {codigo}")
    print(f"Preço novo do produto: {preco_novo:.2f}")

if total_produtos > 0:
    media_precos_sem_aumento = total_precos_sem_aumento / total_produtos
    media_precos_com_aumento = total_precos_com_aumento / total_produtos
    print(f"Média dos preços sem aumento: {media_precos_sem_aumento:.2f}")
    print(f"Média dos preços com aumento: {media_precos_com_aumento:.2f}")
else:
    print("Nenhum produto foi lido.")

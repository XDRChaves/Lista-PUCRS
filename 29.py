soma = 0
quantidade = 0

for numero in range(13, 74):
    soma += numero
    quantidade += 1

media = soma / quantidade

print(f"Média dos números entre 13 e 73: {media:.2f}")

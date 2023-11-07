import math

N = int(input("Digite o tamanho do conjunto (N): "))
p = int(input("Digite o tamanho dos subconjuntos (p): "))

comb = math.comb(N, p)
arr = math.perm(N, p)

print(f"Combinação de {N} elementos tomados de {p} em {p}: {comb}")
print(f"Arranjo de {N} elementos tomados de {p} em {p}: {arr}")

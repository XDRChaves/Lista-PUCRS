votos_candidatos = [0, 0, 0, 0]
votos_nulos = 0
votos_em_branco = 0

while True:
    voto = int(input("Digite o código do candidato (ou 0 para encerrar): "))
    if voto == 0:
        break
    
    if voto >= 1 and voto <= 4:
        votos_candidatos[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1

for i, votos in enumerate(votos_candidatos, 1):
    print(f"Total de votos para o candidato {i}: {votos}")

print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_em_branco}")

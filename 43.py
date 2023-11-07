grupos = []
for i in range(5):
    grupo = [int(input("Digite o valor A: ")), int(input("Digite o valor B: ")), int(input("Digite o valor C: ")), int(input("Digite o valor D: "))]
    grupos.append(grupo)

print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

print("Grupos em ordem decrescente:")
grupos_ordenados = sorted(grupos, key=lambda x: sum(x), reverse=True)
for grupo in grupos_ordenados:
    print(grupo)

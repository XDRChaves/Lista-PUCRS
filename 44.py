cidades = []
total_cidades = 200

for i in range(total_cidades):
    codigo_cidade = int(input("Digite o código da cidade: "))
    estado = input("Digite o estado da cidade: ")
    veiculos_1992 = int(input("Digite o número de veículos de passeio (em 1992): "))
    acidentes_1992 = int(input("Digite o número de acidentes de trânsito com vítimas (em 1992): "))
    
    cidades.append((codigo_cidade, estado, veiculos_1992, acidentes_1992))

maior_acidente = max(cidades, key=lambda x: x[3])
menor_acidente = min(cidades, key=lambda x: x[3])
print(f"Maior índice de acidentes: {maior_acidente[3]}, Cidade: {maior_acidente[0]}, Estado: {maior_acidente[1]}")
print(f"Menor índice de acidentes: {menor_acidente[3]}, Cidade: {menor_acidente[0]}, Estado: {menor_acidente[1]}")

media_veiculos = sum([cidade[2] for cidade in cidades]) / total_cidades
print(f"Média de veículos nas cidades brasileiras: {media_veiculos}")

media_acidentes_rs = sum([cidade[3] for cidade in cidades if cidade[1] == "RS"]) / len([cidade for cidade in cidades if cidade[1] == "RS"])
print(f"Média de acidentes com vítimas no Rio Grande do Sul: {media_acidentes_rs}")

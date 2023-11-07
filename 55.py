from datetime import datetime

data1_str = input("Digite a primeira data (formato: dd/mm/aaaa): ")
data2_str = input("Digite a segunda data (formato: dd/mm/aaaa): ")

data1 = datetime.strptime(data1_str, "%d/%m/%Y")
data2 = datetime.strptime(data2_str, "%d/%m/%Y")

diferenca = data2 - data1

print(f"Diferença entre as datas: {diferenca.days} dias")

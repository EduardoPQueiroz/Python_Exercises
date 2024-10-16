import os
import json

os.system("cls")

contato = {
    'nome': 'Edson',
    'idade': 50,
    'cel': '11958575757'
}

# Gravando no arquivo Json
with open("cadastro.json", "w", encoding="utf-8") as arq:
    # Gravando o dicionário no arquivo
    json.dump(contato, arq)

with open("cadastro.json", "r", encoding="utf-8") as arq:
    dados_lidos = json.load(arq)
    print("Dados do arquivo json")
    print(dados_lidos)

# modificar o arquivo json
with open("cadastro.json", "r", encoding="utf-8") as arq:
    dados_modificados = json.load(arq)

    # modificando os dados
    dados_modificados["idade"] = 45
    dados_modificados["cel"] = "1245554554"

# Gravando o dicionário no arquivo
with open("cadastro.json", "w", encoding="utf-8") as arq:
    json.dump(dados_modificados, arq)

# Lendo o arquivo modificado
with open("cadastro.json", 'r') as arq:
    dados_modificados_lidos = json.load(arq)
    print("Arquivo Json modificado")
    print(dados_modificados_lidos)

for k, v in dados_modificados_lidos.items():
    print(f"{k} -> {v}")
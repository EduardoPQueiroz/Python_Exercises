import os
import json
os.system("cls")


# Criando uma pessoa
def criar_pessoa():
    nome = str(input("Insira o nome: "))
    

# Criando um dicionário
pessoas =  {
    'pessoa1' : {
        'nome' : 'Luca',
        'idade' : 16,
        'email' : 'luca@etec.com.br'
    },
    'pessoa2' : {
        'nome' : 'Jamal',
        'idade' : 17,
        'email' : 'jamal@etec.com.br'
    }
}



pessoas_json = json.dumps(pessoas, indent=4)
print("Exibindo o dicionário...")
print(pessoas)
print("\nExibindo o objeto json...")
print(pessoas_json)

# gravando no arquivo json
with open("arquivo.json", "w", encoding="utf-8") as file:
    # Gravando o objeto no arquivo json
    file.write(pessoas_json)


# lendo um arquivo json
with open("arquivo.json", "r", encoding="utf-8") as file:
    print("\nExibindo o arquivo lido.")
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

print(pessoas)
print(pessoas_json)

print("\nExibindo para o usuário: ")
for k, v in pessoas.items():
    print(f"Registro...: {k}")
    for k1, v1 in v.items():
        print("\t" + k1 + ":" + str(v1))
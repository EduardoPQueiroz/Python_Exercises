import os
import json
os.system("cls")


# Criando uma pessoa
def criar_pessoa():
    
    nome = str(input("Insira o nome da pessoa a ser adicionada: "))
    idade = int(input("Insira a idade da pessoa a ser adicionada: "))
    email = str(input("Insira o email da pessoa a ser adicionada: "))
    
    return {
        'nome': nome,
        'idade': idade,
        'email': email
    }
    

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

while True:
    print('0 - Sair')
    verificar = input("Aperte qualquer tecla para adicionar")

    match verificar:
        case '0':
            print('Obrigado por utilizar o sistema!')
            break
        case _:
            novaPessoa = criar_pessoa()
            pessoas['pessoa'+str(len(pessoas)+1)] = novaPessoa

pessoas_json = json.dumps(pessoas)
# gravando no arquivo json
with open("arquivo.json", "w", encoding="utf-8") as file:
    # Gravando o objeto no arquivo json
    file.write(pessoas_json)


# lendo um arquivo json
with open("arquivo.json", "r", encoding="utf-8") as file:
    # print("\nExibindo o arquivo lido.")
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

# print(pessoas)
# print(pessoas_json)

print("\nExibindo para o usuário: ")
for k, v in pessoas.items():
    print(f"Registro...: {k}")
    for k1, v1 in v.items():
        print("\t" + k1 + ":" + str(v1))
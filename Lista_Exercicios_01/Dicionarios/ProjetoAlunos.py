import os
os.system("cls")

# Definição da estrutura do dicionário:
notas = {
    'João' : 9.5,
    'Marilía' : 10.0,
    'Jose' : 4.5
}
# Subalgoritmos

def menu() -> None: 
        os.system("cls")
        print("0. sair ")
        print("1. Adicionar novo aluno | Nota")
        print("2. editar aluno | nota ")
        print("3. Listar os alunos")
        print("4. Excluir aluno")
        print("5. Calcular a média da turma")
        print("6. Consultar um aluno")
        print("7. Apagar todos os alunos da sala\n")


def listar_alunos(d : dict) -> None:
    for k,v in d.items():
        print(f"Aluno: {k} ------- {v}")

def cadastar_aluno(d : dict) -> None:
    print("Cadastro de Alunos\n==================\n")
    nome = str(input("Insira o nome de um aluno: "))
    nota = float(input("Insira a nota do Aluno: "))
    if nome in d:
        print("O nome inserido já existe na lista de alunos.")
    else:
        if nota < 0 or nota > 10:
            print("\n***************************\nNota inválida inserida.\n***************************")
        else:
            d[nome] = nota
            print("\n===========================\nNota inserida com sucesso!\n===========================")
#Programa Principal

opcao = ''

while opcao != 0:

    menu()
    
    
    opcao = int(input("insira a opção desejada: "))
        
    match opcao:
        case 0:
            break
        case 1: 
            os.system("cls")
            cadastar_aluno(notas)
            input("Pressione Enter para continuar.")
            continue
        case 2:
            os.system("cls")
            
            input("Pressione Enter para continuar.")
            continue
        case 3:
            os.system("cls")
            listar_alunos(notas)
            input("Pressione Enter para continuar.")
            continue
        case 4: 
            input("Pressione Enter para continuar.")
            continue
        case 5:
            input("Pressione Enter para continuar.")
            continue
        case 6:
            input("Pressione Enter para continuar.")
            continue
        case 7:
            input("Pressione Enter para continuar.")
            continue
        case _:
            print("opção inválida")
            input("Pressione Enter para continuar.")




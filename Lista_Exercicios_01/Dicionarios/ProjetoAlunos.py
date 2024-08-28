import os
os.system("cls")

numeros = "1234567890"
# Definição da estrutura do dicionário:
notas = {
    'João' : 9.5,
    'Marilía' : 10.0,
    'Jose' : 4.5
}
# Subalgoritmos

def valida_nota(nota: float) -> bool:
    try:
        if nota < 0 or nota > 10:
            validez = False
        else:
            validez = True
        return validez
    except:
        print("\n***************************\nDados inválidos.\n***************************")


def valida_nome(nome: str) -> bool:
    for char in nome:
        if char in numeros:
            return False
    return True

def menu() -> None: 
        os.system("cls")
        print("1. Adicionar novo aluno | Nota")
        print("2. Editar aluno | nota ")
        print("3. Listar os alunos")
        print("4. Excluir aluno")
        print("5. Calcular a média da turma")
        print("6. Consultar um aluno")
        print("7. Apagar todos os alunos da sala")
        print("0. SAIR\n")

# 3. LISTAR ALUNOS
def listar_alunos(d : dict) -> None:
    for k,v in d.items():
        print(f"Aluno: {k} ------- {v}")

# 1. ADICIONAR ALUNOS A LISTA
def cadastar_aluno(d : dict) -> None:
    print("Cadastro de Alunos\n==================\n")
    try:
        nome = str(input("Insira o nome de um aluno: "))
        nota = float(input("Insira a nota do Aluno: "))
        if nome in d:
            print("O nome inserido já existe na lista de alunos.")
        else:
            if valida_nota(nota) == False or valida_nome(nome) == False:
                print("\n***************************\nDados inválidos inseridos.\n***************************")
            else:
                d[nome] = nota
                print("\n===========================\nNota inserida com sucesso!\n===========================")
    except:
        print("\n***************************\nDados inválidos inseridos.\n***************************")
    

# 2. EDITAR ALUNOS
def editar_aluno(d: dict) ->  None:
    print("Editando Alunos\n==================")
    edit = str(input("Insira o nome do aluno que deseja editar: "))
    if edit in d:
        nota = float(input("Insira a nova nota do aluno: "))
        valida_nota(nota)
        if nota == False:
            print("\n***************************\nNota inválida inserida.\n***************************")
        else:
            nome = edit
            d[nome] = nota
            print("\n===========================\nNota inserida com sucesso!\n===========================")
    else:
        print("*****************************\nVocê não pode editar um aluno que não está na lista\n*****************************")

#4. EXCLUIR ALUNOS DA LISTA
def excluir_aluno(d: dict) -> None:
    print("\n*********************\nEXCLUINDO ALUNOS\n*********************")
    exc = str(input("Insira o nome do aluno que deseja excluir: "))
    if exc in d:
        confirm = str(input("Você tem certexa que deseja excluir este aluno da lista? Alunos excluidos não poderão ser recuperados posteriormente.\nS/s - Sim / N/n - Não: "))
        if confirm == 'S' or confirm == 's':
            nome = exc
            del d[nome]
            print("\n===============================\nAluno Excluido com sucesso!\n===============================")
        else:
            print("\n===============================\nAção Cancelada\n===============================")
    else:
        print("*****************************\nVocê não pode excluir um aluno que não está na lista\n*****************************")

# CALCULANDO A MÉDIA DA TURMA
def media_da_turma(d: dict) -> None:
    print("=======================\nCalculando a Média\n=======================")
    soma = 0
    for i in d.values():
        soma = soma + i
    media = soma / len(d.values())
    

    print(f"\n=====================================================\nA média das notas dos alunos da turma é igual a: {media}\n=====================================================\n")

# CONSULTANDO NOME E NOTA DE ALUNOS.
def consulta_aluno(d: dict) -> None:
    print("=======================\nConsultando Alunos\n=======================")
    consulta = str(input("Insira o nome do aluno que deseja consultar: "))
    if consulta in d:
        nome = consulta
        print(f"A nota de {consulta} foi {d[nome]}")
    else: 
        print("O nome que você escreveu não está na lista de alunos. ")

# DELETANDO TODOS OS ALUNOS
def deleta_tudo(d: dict):
    print("=======================\nDeletar todos os alunos da lista\n=======================")
    confirm = str(input("ESSA FUNÇÃO APAGARÁ TODOS OS DADOS DOS ALUNOS, SEM A POSSIBILIDADE DE RECUPERAÇÃO, VOCÊ TEM CERTEZA QUE DESEJA DELETÁ-LOS?\n S/s = Sim // N/n = Não: "))
    if confirm == 's' or confirm == 'S':
        d.clear()
        print("Todos os dados foram removidos.")
    else:
        print("Ação cancelada.")



#Programa Principal
os.system("cls")
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
            editar_aluno(notas)
            input("Pressione Enter para continuar.")
            continue
        case 3:
            os.system("cls")
            listar_alunos(notas)
            input("Pressione Enter para continuar.")
            continue
        case 4: 
            os.system("cls")
            excluir_aluno(notas)
            input("Pressione Enter para continuar.")
            continue
        case 5:
            os.system("cls")
            media_da_turma(notas)
            input("Pressione Enter para continuar.")
            continue
        case 6:
            os.system("cls")
            consulta_aluno(notas)
            input("Pressione Enter para continuar.")
            continue
        case 7:
            os.system("cls")
            deleta_tudo(notas)
            input("Pressione Enter para continuar.")
            continue
        case _:
            print("opção inválida")
            input("Pressione Enter para continuar.")
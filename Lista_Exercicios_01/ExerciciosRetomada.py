import os
os.system("cls")

"""subalgoritimos"""

def localiza_e_troca() -> None:
    frase = str(input("escreva uma frase: "))
    caracter_localizar = str(input("insira um caracter para ser localizado: "))
    while len(caracter_localizar) != 1:
        print("--digite apenas UM caracter--")
        continue
    caractere_substituicao = str(input("insira um caracter para substituir o localizado: "))
    while len(caractere_substituicao) != 1:
        print("--digite apenas UM caracter--")
        continue

    frase_nova = frase.replace(caracter_localizar , caractere_substituicao) 
    print(frase_nova)
    
def separa_listas(lista: list) -> None:
    listaInt = []
    listaFloat = []
    listaString = []
    listaBoliviano = []
    for i in range(len(lista)):
        if type(lista[i]) == int:
            listaInt.append(lista[i])
        elif type(lista[i]) == float:
            listaFloat.append(lista[i])
        elif type(lista[i]) == str:
            listaString.append(lista[i])
        else:
            listaBoliviano.append(lista[i])
    print(listaInt)
    print(listaFloat)
    print(listaString)
    print(listaBoliviano)

def limite_dez() -> list:
    lista = []
    for i in range(10):
        elemento = input("insira o que quiser:")
        lista.append(elemento)
    print(lista)        















"""codigo"""


verifica = ''

while verifica != 0:
    opcao = int(input("insira o numero do exercicio desejado(1-3): "))
    match opcao:
        case 1: 
            localiza_e_troca()
        case 2:
            lista = [45, 5.7, "Férias", True, False, 99, 34]
            separa_listas(lista)
            continue
        case 3:
            limite_dez()
            continue

    print("deseja contiuar?")
    verifica = int(input("1-sim \n0-não\n"))
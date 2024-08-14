import os
os.system("cls")

import subalgoritmosList
l = []

print("1.Preencher Lista")
print("2.Exibir Lista")
print("3.Conta elementos")
print("4.Retornar Indice")
print("5.Buscar Elementos")
print("6.Contar Inteiros")
print("0.EXIT\n")


op = ''
while op != 0:
    op = int(input("Insira qual exercicio deseja: "))
    match op:
        case 1:
            print(subalgoritmosList.preenche_lista(l))
        case 2:
            print(subalgoritmosList.exibe_lista(l))
        case 3:
            print(f"a quantidade de elementos no vetor é: {subalgoritmosList.conta_elementos(l)}")
        case 4: 
            elemento = int(input("Insira o elemento que deseja saber o indice na lista: "))
            print(f"O elemento inserido tem indice: {subalgoritmosList.retorna_indice(l, elemento)}")
        case 5:
            elemento = int(input("Insira o elemento que deseja buscar quantas vezes se repete na lista: "))
            print(f"O elemento inserido se repete {subalgoritmosList.busca(l, elemento)} vezes na lista.")
        case 6:
            print(f"Existem {subalgoritmosList.conta_inteiro(l)} números inteiros nessa lista.")


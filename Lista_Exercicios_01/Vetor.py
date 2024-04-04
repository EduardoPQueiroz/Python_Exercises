import os
os.system("cls")

import subalgoritmosVetor 
vetor = [45, -89, 32, -12, 33]
v1 = [41, 72, 39, 4, 35]
v2= [0, 0, 0, 0, 0]

print("1. O primeiro elemento do vetor.")
print("2. Números Negativos do vetor.")
print("3. Soma dos elementos do vetor")
print("4. Media dos elementos no vetor.")
print("5. Números Ímpares no vetor.")
print("6. Exibir extremos do vetor.")
print("7. Exibir indices ímpares")
print("8. Buscar Elemento.")
print("9. Ordenar Vetor.")
print("10. Copiar Vetor")
print("11. Inverte Vetor.")
print("12. Ordenar Vetor em ordem crescente.")
print("13. Ordenar Vetor em ordem decrescente.")
print("14. Ordenar Vetor em ordem crescente ou decrescente.")
print("15. Separar Pares e Impares no vetor")
print("16. Conta número acima da média no Vetor.")
print("17. Exibe o maior número no vetor.")
print("0. SAIR")

op = ''
while op != 0:
    op = int(input("\nInsira qual função deseja utilizar: "))
    match op:
        case 1:
            print(f"\no primeiro elemento do vetor é: {subalgoritmosVetor.primeiroElemento(vetor)}")
            continue
        case 2:
            subalgoritmosVetor.numerosNegativos(vetor)
            continue
        case 3: 
            print(f"\nA soma dos elementos contidos no vetor é igual a: {subalgoritmosVetor.somaVetor(vetor)}")
            continue
        case 4:
            print(f"\nA media dos elementos contidos no vetor é igual a: {subalgoritmosVetor.mediaVetor(vetor)}")
            continue
        case 5:
            subalgoritmosVetor.numerosImpares(vetor)           
            continue
        case 6:
            subalgoritmosVetor.exibeExtremos(vetor)
            continue
        case 7:
            subalgoritmosVetor.exibeIndiceImpar(vetor)
            continue
        case 8: 
            print(f"O Número inserido existe no vetor: {subalgoritmosVetor.buscaVetor(vetor)}")
            continue
        case 9:
            subalgoritmosVetor.ordenaVetor(vetor)
            continue
        case 10:
            subalgoritmosVetor.copiaVetor(v1, v2)
            continue
        case 11: 
            subalgoritmosVetor.inverteVetor(v1, v2)
            continue
        case 12:
            subalgoritmosVetor.ordenaVetorCrescente(v1)
            continue
        case 13:
            subalgoritmosVetor.ordenaVetorDecrescente(v1)
            continue
        case 14:
            subalgoritmosVetor.ordenaVetorCorD(v1)
            continue
        case 15:
            subalgoritmosVetor.separaParesImpares(v1)
            continue
        case 16:
            print(f"Existem {subalgoritmosVetor.contaAcimaMedia(v1)} números acima da média no vetor")
            continue
        case 17:
            print(f"O maior numero no vetor é: {subalgoritmosVetor.maiorNum(v1)}.")
        case 0:
            break   
        case _:
            print("\n-----Insira uma opção válida!-----") 
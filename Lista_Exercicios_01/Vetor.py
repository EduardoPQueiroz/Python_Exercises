import os
os.system("cls")

vetor = [45, -89, 32, -12, 33]

def primeiroElemento() -> int:
    return vetor[0]

def numerosNegativos() -> int:
    vetor_negativo = []
    for i in range(0, 5, 1):
        if vetor[i] < 0:
            vetor_negativo.append(vetor[i])
    return vetor_negativo
def somaVetor() -> int:
    soma = vetor[0]
    for i in range(1, 5, 1):
        soma = soma + vetor[i]
    return soma
def mediaVetor() -> float:
    soma = vetor[0]
    for i in range(1, 5, 1):
        soma = soma + vetor[i]
    media = soma / 5
    return media
def numerosImpares() -> int:
    vetor_impares = []
    for i in range(0 , 5, 1):
        if vetor[i] % 2 != 0:
            vetor_impares.append(vetor[i])
    return vetor_impares

print("1. O primeiro elemento do vetor.")
print("2. Números Negativos do vetor.")
print("3. Soma dos elementos do vetor")
print("4. Media dos elementos no vetor.")
print("5. Números Ímpares no vetor.")
print("0. SAIR")

op = ''
while op != 0:
    op = int(input("\nInsira qual função deseja utilizar: "))
    match op:
        case 1:
            print(f"\no primeiro elemento do vetor é: {primeiroElemento()}")
            continue
        case 2:
            print(f"\nOs números negativos contidos no vetor são: {numerosNegativos()}")
            continue
        case 3: 
            print(f"\nA soma dos elementos contidos no vetor é igual a: {somaVetor()}")
            continue
        case 4:
            print(f"\nA media dos elementos contidos no vetor é igual a: {mediaVetor()}")
            continue
        case 5:
            print(f"\nOs números impares contidos no vetor são: {numerosImpares()}")            
            continue
        case 0:
            break   
        case _:
            print("\n-----Insira uma opção válida!-----") 
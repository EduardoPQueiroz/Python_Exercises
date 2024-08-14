vetor = [45, -89, 32, -12, 33]
v1 = [41, 72, 39, 4, 35]
v2= [0, 0, 0, 0, 0]

def primeiroElemento(vetor: list) -> int:
    return vetor[0]


def numerosNegativos(vetor: list) -> int:
    vetor_negativo = []
    for i in range(0, 5, 1):
        if vetor[i] < 0:
            vetor_negativo.append(vetor[i])
    print(vetor_negativo)

def somaVetor(vetor: list) -> int:
    soma = vetor[0]
    for i in range(1, 5, 1):
        soma = soma + vetor[i]
    return soma

def mediaVetor(vetor: list) -> float:
    soma = vetor[0]
    for i in range(1, 5, 1):
        soma = soma + vetor[i]
    media = soma / 5
    return media

def numerosImpares(vetor: list) -> int:
    vetor_impares = []
    for i in range(0 , 5, 1):
        if vetor[i] % 2 != 0:
            vetor_impares.append(vetor[i])
    print(vetor_impares)

def exibeExtremos(vetor: list):
    print(f"O primeiro elemento do vetor é {vetor[0]}, e o último é {vetor[4]}")

def exibeIndiceImpar(vetor: list):
    for i in range(0, 5, 1):
        if i % 2 != 0:
            print(vetor[i]) 

def buscaVetor(vetor: list) -> bool:
    Buscador = int(input("Insira o número que deseja buscar no vetor: "))
    for i in range(0, 5, 1):
        if Buscador == vetor[i]:
            boliviano = True
            return boliviano

def ordenaVetor(vetor: list):
    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            if vetor[i] < vetor[j]:
                mente = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = mente            
    print(f"O Vetor ordenado = {vetor}") 

def copiaVetor(v1: list, v2: list):
    for i in range(0, 5, 1):
        v2[i] = v1[i]
    print(f"O Valor do vetor 1 foi copiado, este é o vetor 2: {v2}")

def inverteVetor(v1: list, v2: list):
    for i in range(0, 5, 1):
        v2[i] = v1[4-i]
    print(f"O Valor do vetor 1 foi invertido e copiado, este é o vetor 2: {v2}")    

def ordenaVetorCrescente(v1: list):
    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            if v1[i] < v1[j]:
                mente = v1[i]
                v1[i] = v1[j]
                v1[j] = mente            
    print(f"O Vetor ordenado = {v1}") 

def ordenaVetorDecrescente(v1: list):
    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            if v1[i] > v1[j]:
                mente = v1[i]
                v1[i] = v1[j]
                v1[j] = mente            
    print(f"O Vetor ordenado = {v1}")

def ordenaVetorCorD(v1: list):
    opcao = str(input("Insira 'C' para ordem crescente, ou 'D' para decrescente: "))
    if opcao == 'C' or opcao == 'c':
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                if v1[i] < v1[j]:
                    mente = v1[i]
                    v1[i] = v1[j]
                    v1[j] = mente            
        print(f"O Vetor ordenado = {v1}")
    elif opcao == 'D' or opcao == 'd':
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                if v1[i] > v1[j]:
                    mente = v1[i]
                    v1[i] = v1[j]
                    v1[j] = mente            
        print(f"O Vetor ordenado = {v1}")
    else:
        print("Insira uma opção válida.")

def separaParesImpares(v1: list):
    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            if v1[i] % 2 == 0:
                mente = v1[i]
                v1[i] = v1[j]
                v1[j] = mente
    print(f"O vetor ordenado com os pares a esquerda: {v1}")

def contaAcimaMedia(v1: list):
    soma = 0
    counter = 0
    for i in range(0, 5, 1):
        soma = soma + v1[i]
    media = soma / 5
    for i in range(0, 5, 1):
        if v1[i] > media:
            counter = counter + 1
    return counter

def maiorNum(v1: list):
    maior = 0
    for i in range(0, 5, 1):
        if v1[i] > maior:
            maior = v1[i]
    return maior
        

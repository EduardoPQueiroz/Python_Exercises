l = []
def preenche_lista(l):
    continuar = ''
    while continuar != 0:
        valor = int(input("\nInsira um valor no vetor: "))
        l.append(valor)
        continuar = int(input("\nInsira 1 para inserir mais um valor, ou 0 para parar: "))
        continue
    print("\n---lista preenchida!---")

def exibe_lista(l):
    print(l)

def conta_elementos(l):
    qtd_elementos = len(l)
    return qtd_elementos

def retorna_indice(l, elemento):
    distancia_lista = len(l)
    valor = -1
    for i in range(0, distancia_lista, 1):
        if elemento == l[i]:
            valor = i
    return valor

def busca(l, elemento):
    distancia_lista = len(l)
    qtd_elemento = 0
    for i in range(0, distancia_lista, 1):
        if l[i] == elemento:
            qtd_elemento = qtd_elemento + 1
    return qtd_elemento

def conta_inteiro(l):
    dist_lista = len(l)
    qtd_inteiros = 0
    for i in range(0, dist_lista, 1):
        if l[i] == int:
            qtd_inteiros += 1
    return qtd_inteiros
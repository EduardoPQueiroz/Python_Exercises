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
    for i in range(0, len(l), 1):
        if elemento == l[i]:
            valor = i
    return 

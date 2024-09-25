import os
os.system("cls")
'''
with open("arq.txt", "w+", encoding="utf-8") as arq:
    arq.write("Linha 1\n")
    arq.write("Linha 2\n")
    arq.write("Linha 3\n")
    arq.seek(0)
    lista_linhas = arq.readlines()
    # print(lista_linhas[2])
    arq.seek(0)
    for linha in arq.readlines():
        print(linha, end = '')
'''
        
# readlines() - transforma faz uma lista com as linhas do arquivo

# readline() - lê apenas linha onde estáo cursor

# writelines()

'''
with open("arq.txt", "w+" ,encoding = "utf-8") as arq:
    print("Gravando uma linha por vez")
    while True:
        linha = input("Linha: ")
        if linha != "":
            arq.write(linha + '\n')
        else:
            break
    os.system("cls")
    print("\nExibindo arquivo: ")
    arq.seek(0)
    print(arq.read())
'''
'''
with open("arq2.txt", "w+", encoding = "utf-8") as arq:
    print("Gravando varias linhas")
    documento = ["marion\n", "Eduson\n", "45.7\n"]
    arq.writelines(documento)
'''
'''
with open("atividade.txt", "w+", encoding = "utf-8") as arq:
    lista = []
    print("gravando ate o user apertar enter")
    while True:
        linha = str(input("Linha: "))
        if linha != "":
            lista.append(linha)
        else:
            os.system("cls")
            for item in lista:
                print(item)
            break
'''



    
    
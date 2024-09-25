# Manipulaçãoo de arquivos
caminho = "C:\\Users\\etechas\\Python_Exercises\\Lista_Exercicios_01\\operador_ternario\\arquivos_txt\\"
caminho += "arq1.txt"
'''
Modo de abertura: 
------------------------------
'w' | write - gravar

'r' | read - ler

'a' | append - Edição de arquivo

'x' | gravação em arquivo exclusivo

'+' | Gravar e ler ao mesmo tempo

função open() -> abre um arquivo
-------------------------------------------------------

Sintaxe:
    <obj> = open("nome_arquivo", "modo_abertura")

------------------------------------------------------- 
'w' - sobrepõe
'a' - acrescenta
'''

import os 
os.system("cls")

'''Abrindo um arquivo e gravando'''

arq = open("arq1.txt", "w", encoding = "utf-8")
arq.write("Receba a gravaduração!!!!!!!!!!!!!!!!\n")
arq.close()

'''Lendo um arquivo'''
# try:
#     arq = open("arq1.txt", "r", encoding = "utf-8")
#     '''Lê o arquivo integralmente'''
#     print(arq.read()) 
#     arq.close()
# except FileNoFoundError:
#     print("Arquivo não existe")

arq = open("arq1.txt", "a", encoding = "utf-8")
arq.write("\nNova linha")
arq.close()


arq = open("arq2.txt", "w+", encoding = "utf-8")
arq.write("Nova linha")
arq.seek(0) # O método seek posiciona cursor em qualquer casa da linha que vc escolhr
print(arq.read())
arq.close()

# Operador de contexto with
with open("arq1.txt", "r", encoding = "utf-8") as arq:
    arq.seek(0)
    print(arq.read())

# Exercicios
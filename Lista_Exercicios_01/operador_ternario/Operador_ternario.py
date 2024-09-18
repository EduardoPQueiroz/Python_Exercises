import os
os.system("cls" if os.name == "nt" else "clear")

#O operador ternário substitui o if composto em 
#situações onde há somente um comando do lado verdadeiro e um do lado falso

'''
sintaxe:

[<var> = ] <comando true> if <condição> else <comando false>
'''

#Exemplo 1 (sem variável): Verificar se é maior de idade
idade = 10
print("maior de idade") if idade >= 18 else print("menor de idade")

#Exemplo 2: Utilizando comandos SO
#lista arquivos e diretorios no windows
#ls lista arquivos e diretórios no linux e no MACos 

#Exemplo 3: (com variável): aplicando bonus 
venda = 500
bonus = 50 if venda > 1000 else 30
print(venda, bonus)

#exemplo 4 (parte do cálculo): aplicando desconto em uma venda  
venda = 700
com_desconto = venda - (venda * 0.1 if venda > 1000 else venda *0.05)
print(venda,com_desconto)
import os
os.system("cls")

'''Subalgoritimos'''
def verifica_placa(placa: str) -> bool:
    alfabeto = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numeros = "0123456789"
    valido = True
    if len(placa) == 7:
        for char in placa:
            if placa[0] in alfabeto and placa[1] in alfabeto and placa[2] in alfabeto and placa[4] in alfabeto or placa[4] in numeros and placa[3] in numeros and placa[5] in numeros and placa[6] in numeros:
                continue
            else:
                valido = False
                break            
    else:
        print("Tente outra placa, numero indevido de caracteres!")
        valido = False

    return valido

'''Main'''

placa = str(input("insira uma placa de 7 digitos: "))

'''Placa do Usuário'''
print("Placa do Usuário: \n")
print(verifica_placa(placa))

'''Exemplo - Placa 1''' 
placa1 = "abc5d67"
print("\nExemplo de Placa - 1")
print(placa1)
print(verifica_placa(placa1))   


'''Exemplo - Placa 2''' 
print("\nExemplo de Placa - 2")
placa2 = "abc5d6"
print(placa2)
print(verifica_placa(placa2))
      
'''Exemplo - Placa 3''' 
print("\nExemplo de Placa - 3")
placa3 = "1234567"
print(placa3)
print(verifica_placa(placa3))
      
      
'''Exemplo - Placa 4''' 
print("\nExemplo de Placa - 4")
placa4 = "abc5d678"
print(placa4)
print(verifica_placa(placa4))
      
      
'''Exemplo - Placa 5''' 
print("\nExemplo de Placa - 5")
placa5 = "ab@5d67"
print(placa5)
print(verifica_placa(placa5))
      
      
'''Exemplo - Placa 6''' 
print("\nExemplo de Placa - 6")
placa6 = "abc@d67"
print(placa6)
print(verifica_placa(placa6))

'''Exemplo - Placa 7''' 
print("\nExemplo de Placa - 7")
placa7 = "aCB5d67"
print(placa7)
print(verifica_placa(placa7))
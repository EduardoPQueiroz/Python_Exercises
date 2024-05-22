
string = ("Receba essa pedrada na sua cabeça!")
lista = [1, 2, 3, 4, -1, 34]
string2 = ("123")

def vogal_maiuscula(string):
    vogal = "aeiou"
    for i in range(len(string)):
        if string[i] in vogal:
            string = string.replace(string[i], string[i].upper())

    print(string)


def true_inteiros(lista):
    for digito in lista:
        if type(digito) == str and digito.isdigit():
            TudoInt = False
            break
        elif digito < 0:
            TudoInt = False
            break
        else:
            TudoInt = True
    return TudoInt

def isInteiro(string2) -> bool:
    sinais = ("+-")
    alfabeto = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    isInteiro = True
    for i in range(len(string2)):
        if string2[0] in sinais:
            isInteiro = True
            continue
        elif string2[i] in alfabeto:
            isInteiro = False
            break
    return isInteiro
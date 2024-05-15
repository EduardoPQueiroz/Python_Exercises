
string = ("Receba essa pedrada na sua cabeça!")
lista = [1, 2, 3, 4, -1, 34]

def vogal_maiuscula(string):
    for carac in string(0, len(string), 1):
        if carac == "a" or "e" or "i" or "o" or "u":
            string.replace(carac, carac.upper)
    print(string)

def true_inteiros(lista):
    lista = " ".join(lista)
    
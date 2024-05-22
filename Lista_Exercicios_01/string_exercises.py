import subalgorythms_stringExercises
import os
os.system("cls")

#parameters
string = ("Receba essa pedrada na sua cabeça!")
lista = [1, 2, 3, 4, 1, "34"]
string2 = ("23")

print(string)
#Programa principal
print("\nObserve essa mesma string com as vogais maiúsculas através do método replace: ")
subalgorythms_stringExercises.vogal_maiuscula(string)
print(f"a partir de uma lista passada por parametro, todos os itens são int: {subalgorythms_stringExercises.true_inteiros(lista)}")

print(f"Os itens do vetor são int: {subalgorythms_stringExercises.isInteiro(string2)}")
import os
os.system("cls")

"""Learning how the lists work in python"""
# l = ["Edshow", 12, 1.67, True, 34]
# print(f"Exibe a posição 1 da lista: L1 = {l[1]}")
# print(f"Exibe a lista: L = {l}")
# l[4] = "Edshow"
# print(f"L = {l}")

#.append cria e adiciona um elemento ao final da lista
lista = list()
lista.append(43)
lista.append("Edshooooooow")
print(f"\n{lista}")

#.insert insere um elemento na posição determinada
lista.insert(1, "Olokooo")
print(f"\n{lista}")

#.pop remove o elemento na posição determinada, se não for determinada uma posição remove o ultimo elemento.
"""lista.pop(0)
print(f"\n{lista}")

#.remove remove um elemento tendo o conteudo como referencia ao invés da posição.
lista.remove("Olokooo")
print(f"\n{lista}")"""

#.index retorna o indice do elemento passado por parâmetro
indice = lista.index("Edshooooooow")
print(f"\nIndice: {indice}")

#.count Conta quanto elementos específicos existem na lista.
lista.append("Edshooooooow")
qtdEdshow = lista.count("Edshooooooow")
print(f"\nQuantidade: {qtdEdshow}")

#.len conta quantos elementos existem na lista.
qtd_elementos = len(lista)
print(f"\nQuantidade de elementos: {qtd_elementos}")

#.sum soma os elementos numericos da lista
"""lista.insert(0, 34)
lista.pop()
lista.pop()
lista.pop()
print(sum(lista))"""

# '+' concatena listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista2 + lista1
print(f"\nLista 1: {lista1}")
print(f"\nLista 2: {lista2}")
print(f"\nListas concatenadas: {lista3}")

#.extend adiciona ao final da lista outra lista.
lista1.extend(lista2)
print(f"\nListas: {lista1}")

#copy() copia uma lista em outra
lista1 = lista2.copy()
print(f"\nLista: {lista2}")

lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista1.append(4)
print(f"\n{lista1, lista2}")

#.sort ordena os elementos da lista, o parametro reverse true ordena em ordem decrescente.
list = [12, 456, 67, 123, 3]
list.sort()
print(f"\n{list}")
list.sort(reverse = True)
print(f"\n{list}")

#.reverse muda a ordem dos elementos do vetor sem ordená-los
list = [23, 78, 96, 90, 3564, 123, 324, 1324]
list.reverse()
print(f"\n{list}")

#.clear limpa os elementos da lista, sem excluí-la
list.clear()
print(f"\n{list}")

#del() desaloca a lista da memória
del(list)
print(f"\n{list}")



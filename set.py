# NOT ORDER
# Elements uniqes
# Not elements sucha as: dict, list, set

setOne = {1, 2, 3, 3}
print(type(setOne))
print(setOne)

setTwo = {"Hola", "from", "Spain"}
print(setTwo)

setThree = set("Hola from Spain")
print(setThree)

d = {}
with open("atributos.txt") as f:
    for linea in f:
        palabra,atributo = linea.split() # inicializacion tipo tupla
        lista = d.setdefault(palabra,[]) # pag16
        if atributo not in lista: # validation
            lista.append(atributo) # add element to list of dictionary
print(d);

d = {}
with open("atributos.txt") as f:
    for linea in f:
        palabra,atributo = linea.split() # inicializacion tipo tupla
        lista = d.setdefault(palabra,set()) # pag16
        lista.add(atributo) # add element to list of dictionary
print(d);

import collections

d = collections.defaultdict(set) # pag29
with open("atributos.txt") as f:
    for linea in f:
        palabra,atributo = linea.split()
        d[palabra].add(atributo)
print(d)

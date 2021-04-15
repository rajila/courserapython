import re

print('Init with List')
_dataStudents = ['Ronald', 'Mary', 'Thalia', 'David','Elina', 'Charlotte', 'Isa']
print(_dataStudents)
print('Len of elements:', len(_dataStudents))
print('Element 0: ', _dataStudents[1]) # First element
print('Element -1: ', _dataStudents[-1]) # last element
print('Mary in list: ', 'Mary' in _dataStudents)
print('Caoa in list: ', 'Caoa' in _dataStudents)

# loop with range
for i in range(2):
    print(i)

# Join List '+' -> Create NEW LIST
_dataNotes = [1, 2, 3, 4, 5, 6]
print(_dataStudents + _dataNotes)

# repeat elements of list: Create NEW LIST
print(_dataStudents * 1) # * 0 | * -1 -> Empty list

# Changes data and add elements: [:] Create NEW LIST
_dataNotes[1:3] = [10, 20]
print(_dataNotes)
_dataNotes[0:1] = [100, 200, 300] # change the first element: 1 for 100, and added elements in the next position
print(_dataNotes)

# add elements
_dataNumbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(_dataNumbers)
_dataNumbers.append(90)
_dataNumbers.append(100) # add element in the final
print(_dataNumbers)

#join list with extend
_dataOne = [12, 24 ,33]
_dataTwo = [5, 34]
_dataOne.extend(_dataTwo)
print(_dataOne)

# Order
_dataOne.sort() # sort() return NONE
print(_dataOne)
_dataOne.sort(reverse=True)
print(_dataOne)

# Delete elements
_el = _dataOne.pop() # delete the last element
print(_el)
print(_dataOne)
_el = _dataOne.pop(1) # index the element to delete
print(_el)
del _dataOne[1] # index the element to delete
print(_dataOne)

_alphabet = ['a', 'w', 'e', 'q', 'c', 'v', 'g', 'y', 'u', 'w', 'r', 't', 'w']
print(_alphabet)
_alphabet.remove('e')
print(_alphabet)
_alphabet.remove('w') # only remove the first element
print(_alphabet)
del _alphabet[1:3]
print(_alphabet)

# Read data od the consola
# _notes = list()
# while(True):
#     _dataIN = input('Enter a number: ')
#     if _dataIN == 'done' : break
#     _notes.append(float(_dataIN))
# print('Average is:', sum(_notes) / len(_notes))

# string to list
_txtName = 'Ronald'
_lName = list(_txtName)
print(_lName)

# list to string: JOIN
_txtName = '-'.join(_lName)
print(_txtName)

# Objects and Values: String is inmutable
_fruitOne = 'apple'
_fruitTwo = 'apple'
print(_fruitOne is _fruitTwo) # TRUE, because they refer to the same object
_fruitOne = _fruitTwo
_fruitTwo = 'd'
print(_fruitOne is _fruitTwo) # FALSE

# functions
def delete_head(__t):
    __t.pop(0)

print(_alphabet)
delete_head(_alphabet)
print(_alphabet)

def delete_head2(__t):
    __t = __t
    __t.pop(0)

delete_head2(_alphabet)
print(_alphabet)

def delete_head3(__t):
    __t = __t[:] # [:] -> new list
    __t.pop(0)

delete_head3(_alphabet)
print(_alphabet)

def delete_head4(__t):
    __t[:].pop(0) # [:] -> delete first element of new list

delete_head4(_alphabet)
print(_alphabet)

_listXXX = list([1,2,3,4])
print(_listXXX)

# Is necesary create thw ENUMERATE
_position = None
print(_position)
for _index, _el in enumerate(_listXXX):
    if _el == 3:
        _position = _index
        break
print('position ->', _position)

# List comprimida
lComp = [el ** 2 for el in range(11) if el % 2 == 0]
print('lComp', lComp)

lt = [1 if el % 2 == 0 else 0 for el in range(11)]
print('lt', lt)

classA = ['A', 'C', 'P', 'Q']
classB = ['M', 'P', 'X', 'A']
lUnion = [a for a in classA for b in classB if a == b]
print('lUnion', lUnion)

# List comprimida []
'''
En el primer bucle, la lista se crea (y se itera) como un todo; en realidad,
existe cuando se ejecuta el bucle.
'''
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

# Generator ()
'''
En el segundo bucle, no hay ninguna lista,
solo hay valores subsequentes producidos por el generador, uno por uno.
'''
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

lwords = ['hi', 'from', 'any', 'salprieta', 'salmon']
textWords = 'hi from any salprieta salmon'
print('sal' in lwords) # false
print(textWords.find('sal')) # index of first coincidencia, no sirve para comparar palabras
print(re.findall('sal', textWords)) # retorna una parte de las palabras: ['sal', 'sal']
print(re.search('^sal', textWords)) # no encuentra la coincidencia: None
print(re.search('^hi', textWords)) # si encuentra devuelve un object

print(lwords.index('from')) # retorna la posicion de la lista, en donde se encuentra la palabra. primera ocurrencia
# print(lwords.index('sal')) # retorna error porque no encuentra la palabra en la lista

matriz = []
matriz.append([1,2,3])
matriz.append([4,5,6])
print('value celda[0][1] -> ', matriz[0][1])
print('# row ->', len(matriz))
print('# col ->', len(matriz[0]))

treplace = 'salmon is animal del mar. Alimento de los osos, tambien sirve de alimento para las personas. El salmon se lo come con poca sal'
print(treplace)
treplace = treplace.lower().replace('alimento', 'ajis')
print(treplace)
treplace = treplace.replace('sal', 'SSAALL')
print(treplace)

lTestOne = [1,2,3]
lTestOne.insert(-1, 10) # insert on position -1. tail position of list
lTestTwo = lTestOne # Apunta  a la misma direccion de memoria
print('L1 ->', lTestOne)
lTestOne.append(21)
print('L1 ->', lTestOne)
print('L2 ->', lTestTwo)
lTestThree = lTestOne.copy() # crea una copia de la lista y guarda en otra direccion de memoria
lTestOne.append(31)
print('L1 ->', lTestOne)
print('L3 ->', lTestThree)
lTestThree.clear() # elimina todos los elementos de la lista
print('L3 ->', lTestThree)
tu = tuple()
tu = (1,2) + (3,4)
print(tu)
tu = tu[0] + tu[1]
print(tu)
tu = (1,2,3,4)
print(tu)
tu = tu[1:-1]
print(tu)
tu = tu[0]
print(tu)
x = 1
y = 2
x,y,z = x,x,y
z,y,z = x,y,z
print(x, y, z)
a = 1
b = 0
a = a^b
b = a^b
a = a^b
print(a,b, 1//5+1/5, [i for i in range(-1,-2)], sep="sep")
def f(x,y):
    if x==y:
        return x
    else:
        return f(x, y-1)
print(f(0,3))

tv = (1,2,3,4)
tv = tv[-2:-1]
tv = tv[-1]
print(tv)

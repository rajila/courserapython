print('Hi Dictionaries!!!')
_mapStudents = dict() # Create a dictionary
print(_mapStudents) # map empty
_mapStudents['one'] = 'uno'
print(_mapStudents)
# definition and init
_mapStudents = {'one':'uno', 'two':'dos', 'three':'tres'}
print(_mapStudents)
print('Length dictionary:', len(_mapStudents))
# Keys
print()
print('key \'one\' is in the dictionary (KEYS):','one' in _mapStudents)
print('value \'uno\' is in the dictionary (KEYS):', 'uno' in _mapStudents)
# values
print()
print('key \'one\' is in the dictionary (VALUES):','one' in list(_mapStudents.values()))
print('value \'uno\' is in the dictionary (VALUES):','uno' in list(_mapStudents.values()))

_word = 'RonaldDanielAjilaCalva'
_mapA = dict()
for _letter in _word.lower() :
    _mapA[_letter] = _mapA.get(_letter,0) + 1
print(_mapA)
print(_mapA.get('q')) # Sin error aunq no exista la key: q. Si no existe la key retorna un None
# print(_mapA['q']) # Error porq no existe key: q

dicOne = {}
print(type(dicOne))
dicOne[0] = 'Hola'
print(type(dicOne))

dicTwo = dict(((0,'hi'), [1,'ronald']))
print(dicTwo)

dicThree = dict(zip(['one', 'two'], range(1,3))) # no import size of elements
print(dicThree)

dicFour = dict(a1 = 'a', b1 = 'b') # solo permite claves de tipo string (name de varaibles). ERROR dict('a' = 'a', 'b' = 'b'), dict(1 = 'a', 2 = 'b')
print(dicFour)

dicFive = dict()
dicFive[(1,2)] = (4,5)
dicFive[('1','2')] = (4,5)
# dicFive[([1,2,3],2)] = (6,7) # ERROR
print(dicFive)

dicSix = dict(zip(range(1,9), [el*el for el in range(1,9)]))
print(dicSix)
key = 1
while key in dicSix: # evaluate condition on WHILE
    del dicSix[key]
    key += 1
print(dicSix)

dicSix = dict(zip(range(1,9), [el*el for el in range(1,9)]))

# for key in dicSix: del dicSix[key] # ERROR ERROR ERROR loop dictionary and can not removed element

for key, val in list(dicSix.items()): # new list
    del dicSix[key]
print(dicSix)

dicSeven = dict(((1,2),(2,-10),(3,40),(4,-20)))
print(dicSeven)
for key in [k for k in dicSeven if dicSeven[k] < 0]:
    del dicSeven[key]
print(dicSeven)


dicSeven = dict(zip(range(1,11), [el*el*el for el in range(1,11)]))
print(dicSeven)
print('Delete key 3 ->', dicSeven.pop(3))
print(dicSeven)
print('Delete key 3 ->', dicSeven.pop(3, 'No existe')) # If not exist key, not ERROR
print(dicSeven)

dicSeven = dict(zip(range(1,3), [el*el*el for el in range(1,3)]))
print(dicSeven)
print('Delete last key, value ->', dicSeven.popitem())
print(dicSeven, len(dicSeven))
print('Delete last key, value ->', dicSeven.popitem())
print(dicSeven, len(dicSeven))
# print('Delete last key, value ->', dicSeven.popitem()) # ERROR ERROR ERROR, dictionary empty

dicNine = dict()
dicNine[1] = []
dicNine[2] = "Hola"
print(dicNine)

dicNine11 = dicNine.copy() # for list, dic, apunta misma referencia
print(dicNine11)
dicNine11[2] = "Mundo"
print(dicNine, dicNine11)

dicNine11[1].append('Spain')
dicNine11[1].append('Madrid')
print(dicNine, dicNine11)

dicNine11[1] = ['Valencia']
print(dicNine, dicNine11)



d1 = {} # creando una variable de tipo diccionario
print(type(d1))

d2 = {'Valencia':500, 'Madrid': 1000}
print(type(d2))

d3 = dict() # diccionario sin elementos 'VACIO'
print(type(d3))

d4 = dict(((1,4), (56, 90))) # crea un diccionario, usando tuplas
print(d4)

d5 = dict(([45,20], [89, 1000])) # crear un diccionario , usando listas
print(d5)


d6 = dict( (  (5, 200), [10, 800]   ) ) # crea un diccionario, usando tupla y lista
print(d6)


d7 = dict()
d7[5] = 200
d7[10] = 800
print('d7', d7)



d8 = dict(  zip([10,20,30],[1000,2000,3000])      )
print(d8)

d9 = dict(  zip([10,20,30],[1000,2000,3000, 4000])      )
print(d9)

d10 = dict(hola=50, h1=100)
print(d10)







d11 = dict()
d11['edad'] = 100 # clave de tipo string
d11[10] = 'Ten' # clave de tipo entero
d11[('Valencia', 'Madrid')] = '1000km' # clave de tipo TUPLA
d11['notas'] = [9.3, 8.4, 9.2] # clave de tipo string, pero el valor es una LISTA
print(d11)

# claves de tipo LIST, CONJUNTO, Y DICCIONARIO NO SON PERMITIDAS. MENSAJE DE ERROR
# d11[[1,2]] = 'mi lista'
print(d11)

print('hash 1 ->', hash(1))
print('hash HOLA ->', hash('HOLA'))
print('hash hola ->', hash('hola'))







tupla1 = ( 1, 2, (5,6,7) )
print(hash(tupla1))



























d15 = dict()
d15[0] = 'Hola'
d15[1] = 'como'
d15[2] = 'estas'

print(d15)

# nombre = d15[5]
nombre = d15.get(5, 'valor Por defecto')
nombre2 = d15.setdefault(10, 'Hola otra vez');
print(nombre)
print(nombre2)
print(d15)

# pag11

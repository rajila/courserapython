_data = 1, 2, 3, 4, 5, 6
print(_data, ' -> ', type(_data))
_dataNotes = (10, 20, 30, 40, 50)
print(_dataNotes, ' -> ', type(_dataNotes))
_tuplaOneElement = ('a') # Not is TUPLE, is a string
print(_tuplaOneElement, ' -> ', type(_tuplaOneElement)) # error to create a tuple: one element
_tuplaOneElement = ('a',) # Create a tuple with element
print(_tuplaOneElement, ' -> ', type(_tuplaOneElement)) # OK

# empty tuple
_emptyTuple = tuple()
print(_emptyTuple)

# crete a tuple with elements
_nameTuple = tuple('RonaldDanielAjilaCalva')
print(_nameTuple[0])
print(_nameTuple)
print(_nameTuple[1:4])
_nameTuple = ('O',) + _nameTuple[1:] # create new tuple. Use + for concatenar
print(_nameTuple)
# _nameTuple[1:3] = ('O', 'N') # Error. Tuple is INMUTABLE
# _nameTuple[2] = 'N' # error. Tuple is INMUTABLE

# function
def changeData(__data):
    __data =  ('O',)

changeData(_nameTuple) # no change value of variable. Tuple is INMUTABLE
print(_nameTuple)

_nameFull = 'Isabella Charlotte David Elina Ronald Mary Cecilia Thalia'
_listTuples = list()
for _word in _nameFull.split():
    _listTuples.append((len(_word),_word)) # List of tuples
print(_listTuples)
_listTuples.sort(reverse=True) # Orderna por el primer elemeto de la tupla
print(_listTuples)
#_listTuples.sort(key=lambda tup:(-tup[1], tup[0]), reverse=True)

_dataW = [3, 4]
_x, _y = _dataW
print(_x)
print(_y)
(_x, _y) = 23, 44
print(_x)
print(_y)
# swap
_x, _y = _y, _x
print(_x)
print(_y)
# _x, _y = 43, 43, 43 # ERROR, very much values
data = (1, 2, 3, 4, 5, 6)
m, n, o, *p = data
print()
print('m: {}'.format(m)) # variable normal
print('data: {}'.format(p)) # p is a LIST
print()

# Dictinaries and tuplas
_dataCourses = {'A': 10, 'B': 40, 'C': 24, 'D': 55}
print(_dataCourses)
print(_dataCourses.items())
_listTuplesC = list(_dataCourses.items())
print(_listTuplesC)

# Using tuples as keys in dictionaries
_dictionaryTuple = {}
_dictionaryTuple['Ronald', 'Ajila'] = 100
_dictionaryTuple['Thalia', 'Ajila'] = 70
print(_dictionaryTuple)

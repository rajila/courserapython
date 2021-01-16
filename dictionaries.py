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

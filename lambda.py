'''
Una función lambda es una función sin nombre (también puedes llamarla una función anónima).
Por supuesto, tal afirmación plantea inmediatamente la pregunta: ¿cómo se usa algo que no se puede identificar?

Afortunadamente, no es un problema, ya que se puede mandar llamar dicha función si realmente se necesita,
pero, en muchos casos la función lambda puede existir y funcionar mientras permanece completamente de incógnito.
'''

dos = lambda : 2
cuadrado = lambda x : x * x
potencia = lambda b, e : b ** e

for el in range(-2, 3):
    print(cuadrado(el), end=' ')
    print(potencia(el, dos()))

def printFun(args, fun):
    for val in args:
        print('f(', val, ') = ', fun(val), sep='')

print()
printFun([x for x in range(-2, 3)], lambda x : 2 * x ** 2 - 4 * x + 2)

# test lambda with any arguments
def testFun(lx, ly, fun):
    for index in range(len(lx)):
        print('f(', lx[index], ',', ly[index], ') = ', fun(lx[index], ly[index]), sep='')

print()
testFun([x+x for x in range(-2, 3)], [x*x for x in range(-2, 3)], lambda x, y : 2 * x ** 2 - 4 * x + 2*y)

# función map()
'''
En el más simple de todos los casos posibles, la función map() toma dos argumentos:

Una función.
Una lista.

return: Iterator

Nomenclatura: map(función, lista)
'''
print()
print(list(map(lambda x : 2 ** x, [x for x in range(5)])))

print()
for x in map(lambda x : x ** x, [x for x in range(5)]):
    print(x, end=' ')

print()
for x in map(lambda x, y : x ** y, [x for x in range(10)], [2]*10):
    print(x, end=' ')

print()
for x in map(lambda x : x[0] ** x[1], [(x,2) for x in range(10)]):
    print(x, end=' ')

print()
for name in map(lambda name, surname: '{} {}'.format(name, surname), 'Ronald', 'Ajila'):
    print(name)

print()
for sumN in map(lambda x, y: '{} + {} = {}'.format(x, y, x+y), (15,10,5), (25,2,3)): # Only LIST iterables
    print(sumN)

# function filter()
'''
Espera el mismo tipo de argumentos que map(),
pero hace algo diferente - filtra su segundo argumento mientras es guiado por direcciones que fluyen
desde la función especificada en el primer argumento (la función se invoca para cada elemento de la lista,
al igual que en map() ).

Los elementos que regresan True de la función pasan el filtro - los otros son rechazados.
'''
from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print()
print(data)
print(filtered)

'''
omencemos con una definición: cierres es una técnica que permite almacenar valores a
pesar de que el contexto en el que se crearon ya no existe
'''
def exterior(valExt):
    valInt = valExt
    def interior():
        return valInt
    return interior

var = 1
fun = exterior(var)
print(fun())
print(exterior(10)())
print(exterior(25)())

def calExponente(exponente):
    exponente = exponente
    def getResult(base):
        return base ** exponente
    return getResult

print('2 ** 2 =', calExponente(2)(2))
print('2 ** 3 =', calExponente(3)(2))
print('2 ** 4 =', calExponente(4)(2))
print('2 ** 5 =', calExponente(5)(2))

'''
Close with LAMBDA
'''
def sumCierre(x):
    x = x
    return lambda y : 'Suma {} + {} = {}'.format(y, x, int(x)+int(y))

sumFive = sumCierre(5)

for el in range(1,11):
    print(sumFive(el))

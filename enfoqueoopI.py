class SupA:
    varA = 1
    def __init__(self):
        pass

    def funA(self):
        return 'A'

    def funC(self):
        return 'CA'

class SupB:
    varB = 2
    def __init__(self):
        pass

    def funB(self):
        return 'B'

    def funC(self):
        return 'CB'

    def do(self):
        '''
            Nota: la situación en la cual la subclase puede modificar el comportamiento de su superclase
            (como en el ejemplo) se llama polimorfismo.
            La palabra proviene del griego (polys: "muchos, mucho" y morphe, "forma, forma"),
            lo que significa que una misma clase puede tomar varias formas dependiendo de las
            redefiniciones realizadas por cualquiera de sus subclases.
        '''
        self.doIt()

    def doIt(self):
        print('call from Superclass SupB')

'''
    La herencia múltiple ocurre cuando una clase tiene más de una superclase.
'''
class Sub(SupA, SupB): # herencia multiple
    def doIt(self):
        print('call from Subclass Sub')

data = Sub()

print(data.varA, data.funA())
print(data.varB, data.funB())
print(data.funC())

data.do()

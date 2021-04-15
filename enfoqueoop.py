'''
    El enfoque orientado a objetos sugiere una forma de pensar completamente diferente.
    Los datos y el código están encapsulados juntos en el mismo mundo, divididos en clases.

    Nota:   En su lugar, debes agregar una instrucción específica.
            Las propiedades deben agregarse a la clase manualmente.
            self -> is obligatorio en todos los metodos de la clase
'''

# Superclass
class Pila: # name class
    def __init__(self): # define constructor
        print('Init isntance')
        self.type = 'STACK' # var public
        self.__stack = list() # var private: __<name_var>

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

    def getSize(self):
        return len(self.__stack)

# Subclass
class SumarPila(Pila): # (<name_class>) Son from <name_class>
    '''
        Variables de Clase
        Una variable de clase es una propiedad que existe en una sola copia y
        se almacena fuera de cualquier objeto.
    '''
    count = 0 # class variable. static variable JAVA
    __size = 0 # variable class private. Get variable: SumarPila._SumarPila__size
    def __init__(self): # constructor of class 'SumarPila'
        Pila.__init__(self) # call contructor from superclass
        # super().__init__() # call constructor of superclass
        self.__sum = 0 # variable instance private, encapsulamiento (poco strict)
        SumarPila.count += 1
        SumarPila.__size += 10

    def push(self, value):
        self.__sum += value
        Pila.push(self, value)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum

    def __hidden(self):
        print('Hidden')

pilaNumbers = Pila() # instance of Pilas class
# print(len(pilaNumbers.__stack)) # ERROR
print(pilaNumbers.type)

pilaNumbers.push(1)
pilaNumbers.push(2)
pilaNumbers.push(3)
pilaNumbers.push(4)
print('Size Stack:', pilaNumbers.getSize())
print('Pop Top element: ', pilaNumbers.pop())
print('Size Stack:', pilaNumbers.getSize())
print(pilaNumbers.__dict__)

sumpila = SumarPila()
sumpila.push(10)
sumpila.push(20)
sumpila.push(30)
sumpila.push(40)
sumpila.push(50)
print('Size Stack:', sumpila.getSize())
print('Suma:', sumpila.getSum())
sumpila.pop()
print('Size Stack:', sumpila.getSize())
print('Suma:', sumpila.getSum())

'''
Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto de propiedades y métodos predefinidos.
Cada objeto los tiene, los quieras o no.
Uno de ellos es una variable llamada __dict__ (es un diccionario).

La variable contiene los nombres y valores de todas las propiedades (variables) que el objeto contiene actualmente.
Vamos a usarla para presentar de forma segura el contenido de un objeto.
'''
print(sumpila.__dict__)

sumpila.data = 800 # add vaible out class
print(sumpila.__dict__) # __dict__ -> dictionary that show object properties

# GET value of class variable
'''
    Las variables de clase no se muestran en el diccionario de un
    objeto __dict__ (esto es natural ya que las variables de clase no son partes de un objeto),
    pero siempre puedes intentar buscar en la variable del mismo nombre,
    pero a nivel de clase, te mostraremos esto muy pronto.

    Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).

    Hemos dicho antes que las variables de clase existen incluso cuando no se creó ninguna
    instancia de clase (objeto).
'''
sumpilaTwo = SumarPila()
print('sumpila.count:', sumpila.count) # get varibale public of INSTANCIA
print('SumarPila.count:', SumarPila.count) # get variable public of <name_class>
print('sumpila._SumarPila__size:', sumpila._SumarPila__size)
print('SumarPila._SumarPila__size:', SumarPila._SumarPila__size)

# checking if attr exist
print(hasattr(sumpila, 'count')) # variable de clase
print(hasattr(sumpila, '_SumarPila__sum')) # variable de instancia privada

# call method Hidden
# sumpila.__hidden() # ERROR
sumpila._SumarPila__hidden()

# name, module class
print('name class: ', SumarPila.__name__)
print('name instance: ', type(sumpila).__name__)

print('module class: ', SumarPila.__module__)
print('module instance: ', sumpila.__module__)

def getClass(cls):
    for el in cls.__bases__: # __bases__ only for Class
        print(el.__name__)

getClass(SumarPila)
getClass(Pila)

class MiClase:
    pass

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys(): # loop keys
        if name.startswith('i'): # verify if name startwith 'i'
            val = getattr(obj, name) # get property
            if isinstance(val, int): # checking if val is type INT
                setattr(obj, name, val + 1) # set property

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self): # define formate on str object
        return 'Point -> (' + str(self.x) + ', ' + str(self.y) + ')'

pointIni = Point(5, 25)
print(pointIni)

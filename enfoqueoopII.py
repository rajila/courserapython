class MyZeroDivisionError(ZeroDivisionError):
    pass

def doTheDivision(mode):
    if mode:
        raise MyZeroDivisionError ('My custom Exception')
    else:
        raise ZeroDivisionError('Exception System')

for mode in [False, True]:
    try:
        doTheDivision(mode)
    except ZeroDivisionError as eOne:
        print(eOne, eOne.args, eOne.__class__)

class Pizza:
    def __init__(self, typepizza, cheese):
        self.typePizza = typepizza
        self.cheese = cheese

    def __str__(self):
        return self.typePizza + ' : ' + str(self.cheese)

class PizzaError(Exception):
    def __init__(self, pizza, msn):
        super().__init__(msn)
        self.pizza = pizza

class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, msn):
        super().__init__(pizza, msn) # skype var 'SELF' -> PizzaError.__init__(self, pizza, msn)

def makePizza(pizzaO):
    if pizzaO.typePizza not in ['carnita', 'fourcheese', 'barbacoa']:
        raise PizzaError(pizzaO, '\'No pizza\'')
    if pizzaO.cheese > 100:
        raise DemasiadoQuesoError(pizzaO, '\'Very much cheese\'')
    print('¡Pizza ready!')

print()
for pizzaData, cheeseData in [('carnita', 20), ('peperoni', 50), ('barbacoa', 200), ('atun', 309), ('fourcheese', 50)]:
    try:
        makePizza(Pizza(pizzaData, cheeseData))
    except DemasiadoQuesoError as dqe:
        print('Error (', dqe.__class__, '):', dqe, ' => ', dqe.pizza)
    except PizzaError as pe:
        print('Error (', pe.__class__, '):', pe, ' => ', pe.pizza)

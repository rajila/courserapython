'''
    La programación procedimental fue el enfoque dominante para el desarrollo de software durante décadas de TI,
    y todavía se usa en la actualidad. Además, no va a desaparecer en el futuro,
    ya que funciona muy bien para proyectos específicos (en general, no muy complejos y no grandes,
    pero existen muchas excepciones a esa regla).

    En el enfoque procedimental, es posible distinguir dos mundos diferentes y completamente separados:
    el mundo de los datos y el mundo del código. El mundo de los datos está poblado con variables de diferentes tipos,
    mientras que el mundo del código está habitado por códigos agrupados en módulos y funciones.

    El enfoque orientado a objetos sugiere una forma de pensar completamente diferente.
    Los datos y el código están encapsulados juntos en el mismo mundo, divididos en clases.
'''

stack = list()

def push(value):
    stack.append(value)

def pop():
    value = stack[-1]
    del stack[-1]
    return value

push(1)
push(2)
push(3)
push(4)

while len(stack) != 0:
    print(pop())

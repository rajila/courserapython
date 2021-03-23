name = 'Ronald'
def thing():
    print("Hello", name, apellido)

def surname():
    apellido = 'NA'
    print(name, apellido)

def pmensaje():
    global mensaje
    mensaje = 'Cambio desde pmensaje'
    print(mensaje)

apellido = 'Ajila'
thing()
surname()
print(apellido)
mensaje = 'Hola desde funcion'
print('mensaje -> ', mensaje)
pmensaje()
print('mensaje -> ', mensaje)

num = 153
entero = num%10
num = num//10
print(entero)
print(num)
entero = num%10
num = num//10
print(entero)
print(num)
entero = num%10
num = num//10
print(entero)
print(num)

d = {('valencia','madrid'):20}
# elemento: madrid, valencia, murcia
print(('madrid','valencia') in d)
print(('valencia','madrid') in d)

name = 'Ronald'
def thing():
    print("Hello", name, apellido)

def surname():
    apellido = 'NA'
    print(name, apellido)

def pmensaje():
    global mensaje
    mensaje = 'Cambio desde pmensaje()'
    print(mensaje)

apellido = 'Ajila'
thing() # Hello Ronald Ajila
surname()
print(apellido)
mensaje = 'Hola desde exterior'
print('mensaje -> ', mensaje) # Msn Start
pmensaje() # Change var 'mensaje'
print('mensaje -> ', mensaje) # Msn End

d = {('valencia','madrid'):20}
# elemento: madrid, valencia, murcia
print(('madrid','valencia') in d) # False
print(('valencia','madrid') in d) # True

nameR = 'RonaldRonald'
def testData(name=nameR):
    print('name: {}'.format(name))

nameR = 'DanielDaniel'
testData()

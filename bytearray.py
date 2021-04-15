'''
Antes de comenzar a hablar sobre archivos binarios, tenemos que informarte sobre una de las clases especializadas
que Python usa para almacenar datos amorfos.

Los datos amorfos son datos que no tienen forma específica - son solo una serie de bytes.

Esto no significa que estos bytes no puedan tener su propio significado o que no puedan representar ningún objeto útil,
por ejemplo, gráficos de mapa de bits.

Los datos amorfos no pueden almacenarse utilizando ninguno de los medios presentados anteriormente:
no son cadenas ni listas.

Debe haber un contenedor especial capaz de manejar dichos datos.

Python tiene más de un contenedor, uno de ellos es una clase especializada llamada bytearray - como su nombre indica,
es un arreglo que contiene bytes (amorfos).

Si deseas tener dicho contenedor, por ejemplo, para leer una imagen de mapa de bits y procesarla de alguna manera,
debes crearlo explícitamente, utilizando uno de los constructores disponibles.

Observa:

data = bytearray(100)

Tal invocación crea un objeto bytearray capaz de almacenar diez bytes.

NOTA: dicho constructor llena todo el arreglo con ceros.

Bytearrays se asemejan a listas en muchos aspectos. Por ejemplo, son mutables, son suceptibles a la función len(),
y puedes acceder a cualquiera de sus elementos usando indexación convencional.

Existe una limitación importante - no debes establecer ningún elemento del arreglo de bytes con un valor que no
sea un entero (violar esta regla causará una excepción TypeError) y tampoco está permitido asignar un
valor fuera del rango de 0 a 255 (a menos que quieras provocar una excepción ValueError).
'''
from os import strerror

dataByte = bytearray(20) # init array with zeros

print('Init ->', dataByte)

for data in range(len(dataByte)):
    dataByte[data] = ord('a') + data

print('Update ->', dataByte)
print('Hex ->', end=' ')
for data in dataByte:
    print(hex(data), end=' ')

try:
    # Write file
    fileWrite = open('text.bin', 'wb')
    '''
    El método write() toma su argumento (bytearray) y lo envía (como un todo) al archivo.
    El método write() devuelve la cantidad de bytes escritos correctamente.

    NOTA: En este caso, no hemos utilizado el resultado; esto puede no ser apropiado en todos los casos.
    '''
    fileWrite.write(dataByte)
    fileWrite.close()

    # Read file
    '''
    readinto():
    La lectura de un archivo binario requiere el uso de un método especializado llamado readinto(),
    ya que el método no crea un nuevo objeto del arreglo de bytes,
    sino que llena uno creado previamente con los valores tomados del archivo binario.

    El método devuelve el número de bytes leídos con éxito.

    El método intenta llenar todo el espacio disponible dentro de su argumento;
    si existen más datos en el archivo que espacio en el argumento,
    la operación de lectura se detendrá antes del final del archivo;
    el resultado del método puede indicar que el arreglo de bytes solo se ha
    llenado de manera fragmentaria (el resultado también lo mostrará y la parte del arreglo
    que no está siendo utilizada por los contenidos recién leídos permanece intacta).
    '''
    dataByteRead = bytearray(20)
    fileRead = open('text.bin', 'rb')
    fileRead.readinto(dataByteRead)
    fileRead.close()

    print()
    print('Hex ->', end=' ')
    for data in dataByteRead:
        print(hex(data), end=' ')

    '''
    CUIDADO
    Se ofrece una forma alternativa de leer el contenido de un archivo binario mediante el método denominado read().

    Invocado sin argumentos, intenta leer todo el contenido del archivo en la memoria,
    haciéndolo parte de un objeto recién creado de la clase bytes.

    Esta clase tiene algunas similitudes con bytearray,
    con la excepción de una diferencia significativa: es immutable.

    NOT USE:
        data = bytearray(bf.read())

    NOTA:
        Ten cuidado - no utilices este tipo de lectura si no estás seguro de que el contenido del
        archivo se ajuste a la memoria disponible.
    '''

    # Not code

    '''
    Si el método read() se invoca con un argumento, se especifica el número máximo de bytes a leer.

    read(5) -> lee 5 bytes

    El método intenta leer la cantidad deseada de bytes del archivo,
    y la longitud del objeto devuelto puede usarse para determinar la cantidad de bytes realmente leídos.
    '''
    fileRead = open('text.bin', 'rb')
    '''
    Nota: los primeros cinco bytes del archivo han sido leídos por el código;
    los siguientes cinco todavía están esperando ser procesados.
    '''
    dataFile = bytearray(fileRead.read(5))
    fileRead.close()

    print()
    print('Hex ->', end=' ')
    for data in dataFile:
        print(hex(data), end=' ')

    # read and copy on other file ONE
    bufferTmp = bytearray(5) # var where saved data of file
    fileR = open('text.bin', 'rb')
    fileW = open('textOut.bin', 'wb')

    lenDataR = fileR.readinto(bufferTmp) # max reading 5 bytes
    while lenDataR > 0:
        fileW.write(bufferTmp[:lenDataR])
        lenDataR = fileR.readinto(bufferTmp) # max reading 5 bytes
    fileR.close()
    fileW.close()

    # read and copy on other file TWO
    fileR = open('text.bin', 'rb')
    fileW = open('textOut.bin', 'ab')
    lDataR = bytearray(fileR.read(5))
    while len(lDataR) > 0:
        fileW.write(lDataR)
        lDataR = bytearray(fileR.read(5))
    fileR.close()
    fileW.close()
except IOError as ioe:
    print('Error', strerror(e.errno))

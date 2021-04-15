'''
Afortunadamente, existe una función que puede simplificar el código de manejo de errores.
Su nombre es strerror(), y proviene del módulo os y espera solo un argumento: un número de error.

Su función es simple: proporciona un número de error y una cadena que describe el significado del error.

Nota: Si pasas un código de error inexistente (un número que no está vinculado a ningún error real),
la función lanzará una excepción ValueError.

Usar read() sin argumentos:
RECUERDA - el leer un archivo muy grande (en terabytes) usando este método puede dañar tu sistema operativo.
'''
from os import strerror

try:
    nameFile = input('Name file: ')
    fileIn = open(nameFile, 'r')
    txt = fileIn.read(1)
    while txt != '':
        print(txt, end='')
        txt = fileIn.read(1)
    fileIn.close()

    print()

    '''
    El método intenta leer una línea completa de texto del archivo,
    y la devuelve como una cadena en caso de éxito. De lo contrario,
    devuelve una cadena vacía.
    readline()
    '''
    fileIn = open(nameFile, 'r')
    txtLine = fileIn.readline()
    while txtLine != '':
        print(txtLine.strip()) # strip() -> delete spaces and \n on start-end line
        txtLine = fileIn.readline()
    fileIn.close()

    print()

    '''
    Otro método, que maneja el archivo de texto como un conjunto de líneas,
    no como caracteres, es readlines().

    Cuando el método readlines(), se invoca sin argumentos, intenta leer todo el contenido del archivo y
    devuelve una lista de cadenas, un elemento por línea del archivo.

    Puedes esperar que readlines() procese el contenido del archivo de manera más efectiva que readline(),
    ya que puede ser invocado menos veces.

    Nota: cuando no hay nada que leer del archivo, el método devuelve una lista vacía.
    Úsalo para detectar el final del archivo.
    '''
    fileIn = open(nameFile, 'r')
    txtLines = fileIn.readlines(10)
    while len(txtLines) != 0:
        for ltxt in txtLines:
            print(ltxt.strip()) # strip() -> delete spaces and \n on start-end line
        txtLines = fileIn.readlines(10)
    fileIn.close()

    print()

    '''
    El último ejemplo que queremos presentar muestra un rasgo muy interesante del objeto devuelto
    por la función open() en modo de texto.

    Creemos que puede sorprenderte - el objeto es una instancia de la clase iterable.

    ¿Extraño? De ningúna manera. ¿Usable? Si, por supuesto.

    El protocolo de iteración definido para el objeto del archivo es muy simple:
    su método __next__ solo devuelve la siguiente línea leída del archivo.

    Además, puedes esperar que el objeto invoque automáticamente a close() cuando cualquiera de las
    lecturas del archivo lleguen al final del archivo.

    Mira el editor y ve cuán simple y claro se ha vuelto el código.
    '''
    for line in open(nameFile, 'rt'):
        print(line.strip())

except IOError as exc:
    print('File can not opening:', strerror(exc.errno))

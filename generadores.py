# Using CLASS
class Fibonacci:
    def __init__(self, N):
        self.__N = N
        self.__index = 0
        self.__F1 = self.__F2 = 1

    # Obligatorio (Se ejecuta una sola vez)
    def __iter__(self):
        return self

    # Obligatorio (Se ejecuta en cada iteración)
    def __next__(self):
        self.__index += 1
        if self.__index > self.__N: raise StopIteration # terminate loop
        if self.__index == 1 or self.__index == 2: return 1
        fCurrent = self.__F1 + self.__F2 # get element number current
        self.__F1, self.__F2 = self.__F2, fCurrent # swaping
        return fCurrent

for data in Fibonacci(15):
    print(data, end=' ')

# Using YIELD on functions (No function. Is a Object Generator)
def seqFibonacci(N):
    F1 = F2 = 1
    for i in range(N):
        if i in [0, 1]:
            yield 1
        else:
            current = F1 + F2
            F1, F2 = F2, current
            yield current

print()
print(list(seqFibonacci(15)))
print()

def seqTest1():
    print(1, 'A') # call: 1
    yield 'Hello' # same RETURN. call: 2
    print(2, 'B') # call: 4

for el in seqTest1():
    print(['radc']*4) #   call: 3

def seqTest2():
    print(1, 'A') # call: 1.0
    yield 'Hi' # same RETURN call: 1.1
    print(2, 'B') # call: 2.0
    yield 'from' # same RETURN call: 2.1
    print(3, 'C') # call: 3.0
    yield 'Madrid' # same RETURN call: 3.1
    print(4, 'D') # call: 4.0

print()
for el in seqTest2():
    print(el) #         call: 1.1,      2.1,    3.1
    print(['Hi']*4) #   call: 1.2,      2.2,    3.2

def seqTest3():
    yield 'Hi'
    yield 'from'
    yield 'Madrid'
    print('End') # not print if using next(). Yes print if using for-in

genIter = seqTest3()
print(next(genIter)) # OK
print(next(genIter)) # OK
print(next(genIter)) # OK
# print(next(genIter)) # ERROR

print()
def seqTest4():
    x = yield 'Hola' # X tiene el valor enviado por 'SEND'
    print('from')
    yield x

getIter1 = seqTest4()
print(next(getIter1)) # print: Hola
print(next(getIter1)) # print: from \n none

print()
getIter2 = seqTest4()
print(next(getIter2)) # print: Hola
print(getIter2.send('Spain')) # print: from \n Spain

# ERROR, first call next(), for case seqTest4
# print()
# getIter3 = seqTest4()
# print(getIter3.send('Spain'))

print()
def seqTest5():
    x = yield 'Hola' # X tiene el valor enviado por 'SEND'
    print('from') # no print, because no exit other YIELD before

getIter1 = seqTest5()
print(next(getIter1)) # print: Hola

# ERROR, first call next()
# print()
# getIter2 = seqTest5()
# print(getIter2.send('Spain'))

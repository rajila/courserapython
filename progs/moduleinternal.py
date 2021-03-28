__counter = 0 # var global
print("I like to be a module.")
print(__name__) # __name__ -> variable general on python

def sumCustom (lst):
    global __counter # refere var global
    __counter += 1
    sum = 0
    for el in lst:
        sum += el
    return sum

if __name__ == '__main__':
    print('Sum: ', sumCustom(range(1,9)))

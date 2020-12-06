print('Init with List')
_dataStudents = ['Ronald', 'Mary', 'Thalia', 'David','Elina', 'Charlotte', 'Isa']
print(_dataStudents)
print('Len of elements:', len(_dataStudents))
print('Element 0: ', _dataStudents[1]) # First element
print('Element -1: ', _dataStudents[-1]) # last element
print('Mary in list: ', 'Mary' in _dataStudents)
print('Caoa in list: ', 'Caoa' in _dataStudents)

# loop with range
for i in range(2):
    print(i)

# Join List '+' -> Create NEW LIST
_dataNotes = [1, 2, 3, 4, 5, 6]
print(_dataStudents + _dataNotes)

# repeat elements of list: Create NEW LIST
print(_dataStudents * 1) # * 0 | * -1 -> Empty list

# Changes data and add elements: [:] Create NEW LIST
_dataNotes[1:3] = [10, 20]
print(_dataNotes)
_dataNotes[0:1] = [100, 200, 300] # change the first element: 1 for 100, and added elements in the next position
print(_dataNotes)

# add elements
_dataNumbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(_dataNumbers)
_dataNumbers.append(90)
_dataNumbers.append(100) # add element in the final
print(_dataNumbers)

#join list with extend
_dataOne = [12, 24 ,33]
_dataTwo = [5, 34]
_dataOne.extend(_dataTwo)
print(_dataOne)

# Order
_dataOne.sort() # sort() return NONE
print(_dataOne)
_dataOne.sort(reverse=True)
print(_dataOne)

# Delete elements
_el = _dataOne.pop() # delete the last element
print(_el)
print(_dataOne)
_el = _dataOne.pop(1) # index the element to delete
print(_el)
del _dataOne[1] # index the element to delete
print(_dataOne)

_alphabet = ['a', 'w', 'e', 'q', 'c', 'v', 'g', 'y', 'u', 'w', 'r', 't', 'w']
print(_alphabet)
_alphabet.remove('e')
print(_alphabet)
_alphabet.remove('w') # only remove the first element
print(_alphabet)
del _alphabet[1:3]
print(_alphabet)

# Read data od the consola
# _notes = list()
# while(True):
#     _dataIN = input('Enter a number: ')
#     if _dataIN == 'done' : break
#     _notes.append(float(_dataIN))
# print('Average is:', sum(_notes) / len(_notes))

# string to list
_txtName = 'Ronald'
_lName = list(_txtName)
print(_lName)

# list to string: JOIN
_txtName = '-'.join(_lName)
print(_txtName)

# Objects and Values: String is inmutable
_fruitOne = 'apple'
_fruitTwo = 'apple'
print(_fruitOne is _fruitTwo) # TRUE, because they refer to the same object
_fruitOne = _fruitTwo
_fruitTwo = 'd'
print(_fruitOne is _fruitTwo) # FALSE

# functions
def delete_head(__t):
    __t.pop(0)

print(_alphabet)
delete_head(_alphabet)
print(_alphabet)

def delete_head2(__t):
    __t = __t
    __t.pop(0)

delete_head2(_alphabet)
print(_alphabet)

def delete_head3(__t):
    __t = __t[:]
    __t.pop(0)

delete_head3(_alphabet)
print(_alphabet)

def delete_head4(__t):
    __t[:].pop(0)

delete_head4(_alphabet)
print(_alphabet)

_listXXX = list([1,2,3,4])
print(_listXXX)

# Is necesary create thw ENUMERATE
_position = None
print(_position)
for _index, _el in enumerate(_listXXX):
    if _el == 3:
        _position = _index
        break
print(_position)

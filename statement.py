for _el in range(0, 10, 2):
    print(_el)

_notes = [1,2,3,4,5,6,7]
print(_notes) # print all elements
print(_notes[:]) # print all elements
print(_notes[0:-1])
print(_notes[1:-2])
print(_notes[-2:1]) # empty
print(_notes[:-2])
print(_notes[-2:])
print(_notes[-4:-2])
print('_notes[-2:-4] -> ', _notes[-2:-4]) # empty
print('_notes[-2:1:-1] -> ', _notes[-2:1:-1])
print(_notes[::1])
print(_notes[::2])

listName = ['Ronald', 'Daniel']
print('\'Ronald\' in list: ', 'Ronald' in listName) # TRUE
print('\'Ron\' in list: ', 'Ron' in listName) # FALSE, because evaluate all content of element

txtName = 'Ronald Daniel'
print('\'Ronald\' in str: ', 'Ronald' in txtName) # TRUE
print('\'Ron\' in str: ', 'Ron' in txtName) # TRUE, because evaluate if exits of content on str

print(ord('a'))

print(3*'abc'+'zz')
print(float("1.3"))

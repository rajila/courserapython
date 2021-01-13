import numpy as np
_matrixA = list()

for _el in range(3): # row: 3
    _matrixA.append([_el] * 5) # 5 is column
print(_matrixA)
print(type(_matrixA))
print(len(_matrixA))

# using library
_matrixB = np.array([2,6,8,10])
print(_matrixB)

_matrixC = np.array([[2,6,8,10], [22,26,28,30]])
print(_matrixC)

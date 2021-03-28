from sys import path

path.append('C:\\Users\\RONALD\\Desktop\\courserapython\\modules')
# path.append('..\\modules') # ERROR
path.append('C:\\Users\\RONALD\\Desktop\\courserapython\\packages')

import moduleinternal as minternal # without path
import module as mexternal
import extra.iota as ei

print('I -> ', minternal.__counter)
print('Sum I: ', minternal.sumCustom(range(1,9)))
print('II -> ', minternal.__counter)
print('Sum II: ', minternal.sumCustom(range(1,9)))
print('III -> ', minternal.__counter)
print('Sum III: ', mexternal.sumCustom(range(1,9)))

print(ei.FunI())
print(ei.Div())

ei.getException(1)
ei.getException(2)
ei.getException(3)

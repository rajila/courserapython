print('Init processing file')

_nameFile = input('Enter the file name: ')

_fileHandle = open(_nameFile)

## Print of text
for _txtLine in _fileHandle:
    if 'paploo.uhi.ac.uk' in _txtLine:
        print(_txtLine.rstrip())

## Line count
_fileHandle = open(_nameFile)
_numLines = 0
for _txtLine in _fileHandle:
    _numLines = _numLines + 1
print('\nLine count: ', _numLines)

## Read the WHOLE file
_fileHandle = open(_nameFile)
_allTxt = _fileHandle.read();
print('Character count: ',len(_allTxt))

## Exception Control
_nameOtherFile = input('Enter the new file name: ')

try:
    _fileHandle = open(_nameOtherFile)
except:
    print('File cannot be opened: ', _fileHandle)
    quit()

_allTxt = _fileHandle.read();
print('Character count: ',len(_allTxt))

# Writing files
_nameNewFile = input('Enter the file name to create: ')
try:
    _fileHandleW = open(_nameNewFile, 'w')
except:
    print('File cannot be opened: ', _fileHandle)
    quit()
_fileHandleW.write('Hi, my name is Ronald!!')
_fileHandleW. write('I study at UPM')
_fileHandleW.close()
# Output: Hi, my name is Ronald!!I study at UPM

_fileHandleW = open(_nameNewFile, 'w')
_fileHandleW.write('Hi, my name is Ronald!!\n')
_fileHandleW. write('I study at UPM\n')
_fileHandleW. write('I\'m from Ecuador\n')
_fileHandleW.close()
# Opening it in write mode clears out the old data

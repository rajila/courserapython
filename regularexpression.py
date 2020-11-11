import re

def regulareOne():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        if re.search('From:', _line):
            print(_line.strip())

def regulareTwo():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        if re.search('^From:', _line):
            print(_line.strip())

def regulareThree():
    _file = open('mbox.txt', 'r')
    _count = 0
    for _line in _file:
        # print(_count, ' ', _line.strip())
        _count = _count + 1
        if re.search('^From.+@.+', _line): # . -> anything Character... + -> one or more elements ... * -> zero o more elements
            print(_line.strip())

def regularFour():
    _txt = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    _result = re.findall('\S+@\S+', _txt) # findall --> return an list with elements
    print(_result)
    _result = re.findall('\S+@\S*', _txt) # \S --> evaluate all characters except whitespace
    print(_result)
    _result = re.findall('.+@\S+', _txt)
    print(_result)
    _result = re.findall('@\S+', _txt)
    print(_result)
    _result = re.findall('\S+@\S+|@\S+', _txt) # | --> evaluate twos regular expresions
    print(_result)

def regularFive():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        _result = re.findall('\S+@\S+', _line)
        if len(_result) > 0:
            print(_result)

def regularSix():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        _result = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', _line)
        if len(_result) > 0:
            print(_result)

def regularSeven():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        if re.search('^X\S*: [0-9.]+', _line): # same [0-9] or [0-9.] fix
            print(_line.strip())

def regularEight():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        _result = re.findall('^X\S*: ([0-9.]+)', _line)
        if len(_result) > 0:
            print(_result)

def regularNine():
    _file = open('mbox.txt', 'r')
    for _line in _file:
        _result = re.findall('^Details:.*rev=([0-9]+)', _line)
        if len(_result) > 0:
            print(_result)

def regularTen():
    _txt = 'We just received $10.00 for cookies.'
    _result = re.findall('\$[0-9]+', _txt)
    print(_result)

def regularEleven():
    _txt = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
    _result = re.findall('@([^ ]*)', _txt) # result = uct.ac.za
    print(_result)
    _result = re.findall('@(\S*)', _txt) # result = uct.ac.za
    print(_result)
    _txt = 'DDDaDDDataa1aa1aa1aaaa1 12345'
    _result = re.findall('.+', _txt)
    print('+ ', _result)
    _result = re.findall('.*', _txt)
    print('* ', _result)
    _result = re.findall('.+$', _txt)
    print('+ ', _result)
    _result = re.findall('.*$', _txt)
    print('* ', _result)
    _result = re.findall('^.+?[a]', _txt)
    print('+ ', _result)
    _result = re.findall('^.*?[a]', _txt)
    print('* ', _result)
    _result = re.findall('^.+[a]', _txt)
    print('+ ', _result)
    _result = re.findall('^.*[a]', _txt)
    print('* ', _result)
    _result = re.findall('.+?$', _txt)
    print('+ ', _result)
    _result = re.findall('.*?$', _txt)
    print('* ', _result)
    _result = re.findall('.+[a]', _txt)
    print('+ ', _result)
    _result = re.findall('.*[a]', _txt)
    print('* ', _result)
    _result = re.findall('.+?[a]', _txt)
    print('+ ', _result)
    _result = re.findall('.*?[a]', _txt)
    print('* ', _result)

# regulareOne()
# regulareTwo()
# regulareThree()
# regularFour()
# regularFive()
# regularSix()
# regularSeven()
# regularEight()
# regularNine()
# regularTen()
regularEleven()

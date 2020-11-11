import re

_file = open('regexsum.txt', 'r')
_suma = 0
for _line in _file:
    _digits = re.findall('[0-9]+', _line.strip())
    if len(_digits) > 0:
        for _dg in _digits:
            _suma = _suma + int(_dg)
print(_suma)

# Same code than above, only much more shorter
_file = open('regexsum.txt', 'r')
_txtAll = _file.read().strip()
# _txtAll = 'We are surrounded in our daily lives with computers ranging\n'
print(sum([int(_el) for _el in re.findall('[0-9]+', _txtAll)]))
# print(_txtAll)
# print(re.findall('[0-9]+', _txtAll))
# print([int(_el) for _el in re.findall('[0-9]+', _txtAll)])

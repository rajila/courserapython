import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup # For tags HTML
import ssl

# Ignore SSL certificate error
_ctx = ssl.create_default_context()
_ctx.check_hostname = False
_ctx.verify_mode = ssl.CERT_NONE

_fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for _line in _fhand :
    print(_line.decode().strip())

_url = input('Enter - ')
_html = urllib.request.urlopen(_url, context=_ctx).read();
_soup = BeautifulSoup(_html, 'html.parser')
_tags = _soup('a'); # get all tags: <a>
for _el in _tags :
    print(_el.get('href', None))

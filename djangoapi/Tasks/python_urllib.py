# urllib:- Python urllib module provides several methods to work with URLs

from urllib import request
from pprint import PrettyPrinter
from urllib import parse

# open url - Get Request
# data = request.urlopen(url='http://127.0.0.1:8000/all-users/')
# print data

# create PrettyPrinter object
pp = PrettyPrinter(indent=4)

# print data
# pp.pprint(data.read().decode())

# get response headers as dictionary
# pp.pprint(dict(data.info()))


# HTTP Post request:- urlopen() function automatically use HTTP POST request if request has request body

post_data = {"name": "Vishvajit", "address": "Noida"}
post_data_encode = parse.urlencode(query=post_data).encode('ascii')

# print encoded data
print(post_data_encode)


post_url = "http://127.0.0.1:8000/all-users/"

response = request.urlopen(url=post_url, data=post_data_encode)

# getting all the request headers
pp.pprint(dict(response.info()))

# getting all the request body along with request body
pp.pprint(response.read())

# url parsing
# url='http://127.0.0.1:8000/all-users/?name=vishvajit&course=BCA"'
url='http://127.0.0.1:8000/all-users/'
url_parse = parse.urlparse(url=url)
print(url_parse)
print(url_parse.hostname)
print(url_parse.scheme)
print(url_parse.path)

# url unparse
# url_unparse = parse.urlunparse(url_parse)
# print(url_unparse)

# urlsplit
# url_split = parse.urlsplit(url=url)
# pp.pprint(url_split)

# url unsplit
# url_unsplit = parse.urlunsplit(url_split)
# print(url_unsplit)

# url join
# url_join = parse.urljoin(url,"vishvajit.html")
# print(url_join)

url_quote = parse.quote(string="http://127.0.0.1:8000/all-users")
print(url_quote)

# replace spaces with plus sign
url_quoteplus = parse.quote_plus(string="http://127.0.0.1:8000/all-users")
print(url_quoteplus)

# url_unquote
url_unquote = parse.unquote(string=url_quote)
print(url_unquote)

# url_unquoteplus
url_unquoteplus = parse.unquote_plus(string=url_quoteplus)
print(url_unquoteplus)

# url encode
query = {"name": "Vishvajit", "course": "BCA","address": "Noida"}
url_encode = parse.urlencode(query=query)
print(url_encode)




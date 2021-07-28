# http:- Python http module sets of classes that are used to send request to the server.http module also provides numbers of status code along with the messages.
import http
from http import client
import json
from pprint import PrettyPrinter

# create the object
obj = http.HTTPStatus
print(obj.OK)

# value of status
print(obj.OK.value)

# phrase of status
print(obj.OK.phrase)

# description of the status
print(obj.OK.description)


# Make HTTP Connection

connection = client.HTTPConnection(host="www.httpbin.org")
print(connection)

# send get request
# connection.request(method='GET', url="/all-users/")

# response object
# print(connection.getresponse())

# print response data as bytes
# print(type(connection.getresponse().read()))

# print response data as
# response = connection.getresponse()

# print status code message
# print(response.reason)

# get headers
# print(response.getheaders())

# get headers as string
# print(response.headers)

# access particular header
# print(response.getheader('server'))

# headers information as dictionary
# print(dict(response.info()))

# create PrettyPrinter object
pp = PrettyPrinter(indent=4)
# pp.pprint(response.getheaders())

# make post request

# headers
# headers = {"Content-type": "application/json"}

# request data
# data = {"name": "Vishvajit"}
# json_data = json.dumps(data)

# for making post request
# connection.request(method='POST', url="/post", body=json_data, headers=headers)

# response = connection.getresponse()
# pp.pprint(response.getheaders())

# getting all the request data
# pp.pprint(response.read().decode())


# making put requests

headers = {"Content-type": "application/json"}
data = {"name": "Vishvajit"}
json_data = json.dumps(data)
connection.request(method='PUT', url="/put", body=json_data, headers=headers)

# print request data
# pp.pprint(connection.getresponse().read().decode())

# print all the responses as dictionary
pp.pprint(client.responses)

# constants
pp.pprint(client.HTTP_PORT)
pp.pprint(client.HTTPS_PORT)

# close the connection
connection.close()

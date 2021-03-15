import jwt
import datetime
import time

credentials = {'username': 'vishvajit', 'password': 'ABC12'}
# token = jwt.encode(credentials, 'mysecret', algorithm='HS256', headers={'Unique': 123})
# print(token)

#reading data with validation
# print(jwt.decode(token, 'mysecret', algorithms='HS256'))

#read data without validation
# print(jwt.decode(token, options={'verify_signature': False}))

#reading headers withiot validation
# print(jwt.get_unverified_header(token))


# credentials1 = {'username': 'vishvajit1', 'password': 'ABC121'}
# private_key = b'this is private key'
# public_key=  b'This is the public key'

# token1 = jwt.encode(credentials1, private_key, algorithm='HS256')
# print(token1)
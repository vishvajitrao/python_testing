# Hashlib:- Python Hashlib module is used to generate message digest or secure hash from the source message
import hashlib
from pprint import pprint
import base64


# list of available algorithms
pprint(hashlib.algorithms_available)


print("--------SHA256 Example -----")
m = hashlib.sha256(string=b"This is a SHA256 Example")
print(m.digest())
# update
m.update(b"Hi")
print(m.digest())

print("--------MD5 Example -----")
m = hashlib.sha256(string=b"This is a MD5 Example")

# return the digest of the data passed o the update() method
print(m.digest())


# update the hash object with bytes-like object
m.update(b"Hi")
print("Digest- ",m.digest())

# return the digest in only hexadecimal digits
print("Hex Digest:- ",m.hexdigest())

print("-------------")
print("Size of the result hash:- ", m.digest_size)
print("Internal block Size of the result hash:- ", m.block_size)
print("The canonical name of the hash:- ", m.name)


print("--------sha224 Example -----")
m = hashlib.sha224(string=b"This is a sha224 Example")
print(m.digest())
# update
m.update(b"Hi")
print(m.digest())


print("--------sha384 Example -----")
m = hashlib.sha384(string=b"This is a sha384 Example")
print(m.digest())
# update
m.update(b"Hi")
print(m.digest())


# {'blake2b',
#  'blake2s',
#  'md4',
#  'md5',
#  'md5-sha1',
#  'ripemd160',
#  'sha1',
#  'sha224',
#  'sha256',
#  'sha384',
#  'sha3_224',
#  'sha3_256',
#  'sha3_384',
#  'sha3_512',
#  'sha512',
#  'sha512_224',
#  'sha512_256',
#  'shake_128',
#  'shake_256',
#  'sm3',
#  'whirlpool'}


# hashlib.new():- it takes string name of desired algorithm as the first parameter.

n1 = hashlib.new("sha3_224", data=b"My name is hashlib")
print(n1.hexdigest())

n2 = hashlib.new("sha3_256", data=b"My name is hashlib")
print(n2.hexdigest())

# list of the hash algorithm guaranteed to be supported by this module
pprint(hashlib.algorithms_guaranteed)



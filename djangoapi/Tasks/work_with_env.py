# This file contains all the environment variables related task.
import os
from pprint import pprint

# list all the environment variables
pprint(os.environ)


# get specific environment variable value
print(os.environ.get('SNAP_VERSION'))

# setup environment variables
os.environ['my-username'] = "vishvajitrao12"
os.environ['my-password'] = "Vishvajit12@,"

print("Environment Variable save successfully.....")

print(" ------ Get single environment variable value ------ ")
print("Username is:- ",os.environ.get('my-username'))
print("Password is:- ",os.environ.get('my-password'))

print(" ------ Delete variable value ------ ")
print("Username is:- ",os.environ.pop('my-username'))
print("Password is:- ",os.environ.pop('my-password'))

print(" ------ Get single environment variable value ------ ")
print("Username is:- ",os.environ.get('USERNAMESS='))
print("Password is:- ",os.environ.get('my-password'))
pprint(os.environ)


# Python subprocess module is a built-in Python module that is used to execute new Python application. It is also able to access user input.

import subprocess
from pprint import pprint

# all the function and attributes of Python subprocess module
pprint(dir(subprocess))


# subprocess run
subprocess.call(['ls', '-a'])






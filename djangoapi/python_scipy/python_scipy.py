from scipy import constants, optimize
from math import cos

# constants:- Python scipy provides various constants
# ------ constants ------

# return unit in miter
print("---- Return unit in miter -----")

print(constants.acre)
print(constants.yotta)  # 1e+24
print(constants.zetta)  # 1e+21
print(constants.exa)  # 1e+18
print(constants.peta)  # 1000000000000000.0
print(constants.tera)  # 1000000000000.0
print(constants.giga)  # 1000000000.0
print(constants.mega)  # 1000000.0
print(constants.kilo)  # 1000.0
print(constants.hecto)  # 100.0
print(constants.deka)  # 10.0
print(constants.deci)  # 0.1
print(constants.centi)  # 0.01
print(constants.milli)  # 0.001
print(constants.micro)  # 1e-06
print(constants.nano)  # 1e-09
print(constants.pico)  # 1e-12
print(constants.femto)  # 1e-15
print(constants.atto)  # 1e-18
print(constants.zepto)  # 1e-21

# -- Return unit in bytes
print("---- Return unit in bytes -----")
print(constants.mega)
print(constants.tera)
print(constants.kilo)
print(constants.giga)

print("------ SciPy Optimizer ------")
# Optimize:- SciPy Optimizer is a set of functions that are used to find either the root of equations or minimum value of the function.


def eqn(x):
    return x + cos(x)

result = optimize.root(eqn, 0)
print(result.x)

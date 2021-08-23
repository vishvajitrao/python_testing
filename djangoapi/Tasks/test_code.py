from pytest import *


# Pytest
# Pytest is one of the most popular framework for building a simple and scalable test.

# 1. Simple usages

def capital_case(x):
    return x.upper()


def test_capital_case():
    assert capital_case('vishvajit') == 'VISHVAJIT'


# Group multiple test in a class
print("------- Group multiple test in a class ----------")
class TestClass:
    def test_one(self):
        name = "Vishvajit"
        assert "V" in name

    def test_two(self):
        name = "VISHVAJIT"
        assert name.lower() == 'vishvajit'






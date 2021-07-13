# from arrow import *


# ['Arrow', 'ArrowFactory', 'FORMAT_ATOM', 'FORMAT_COOKIE', 'FORMAT_RFC1036', 'FORMAT_RFC1123', 'FORMAT_RFC2822', 'FORMAT_RFC3339', 'FORMAT_RFC822', 'FORMAT_RFC850', 'FORMAT_RSS', 'FORMAT_W3C', 'ParserError', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'get', 'now', 'utcnow']

# utc_date = utcnow()
# print(utc_date)
# print(utc_date.shift(hours=5, minutes=30))
#
# # local date and time
# local_date_time = utc_date.to('Asia/Kolkata')
# print(local_date_time)
#
# # convert into timestamp
# print(local_date_time.timestamp())
#
# # format date and time
# print(local_date_time.format())
#
# # format can take string format
# print(local_date_time.format('YYYY-MM-DD HH:mm:ss ZZ'))
#
# # humanize
# print(local_date_time.humanize())

# Pytest
# Pytest is one of the most popular framework for building a simple and scalable test.

# 1. Simple usages

# def capital_case(x):
#     return x.upper()
#
#
# def test_capital_case():
#     assert capital_case('vishvajit') == 'VISHVAJIT'


# Group multiple test in a class

# class TestClass:
#     def test_one(self):
#         name = "Vishvajit"
#         assert "Vt" in name
#
#     def test_two(self):
#         name = "VISHVAJIi"
#         assert name.lower()

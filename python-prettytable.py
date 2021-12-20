# prettytable:- This is a simple Python library that is used to show data in simple tabular format.

from prettytable import PrettyTable

# create the instance of the PrettyTable

table = PrettyTable()

# add fields names
table.field_names = ['Name', 'Age', 'Email', 'Occupation']

# add row one by one

table.add_row(['Vishvajit Rao', 22, 'vishvajitrao1998@gmail.com', 'Software Developer'])
table.add_row(['John', 30, 'john@gmail.com', 'Teacher'])

# add multiple rows simultaneously

table.add_rows(
    [
        ['Pankaj', 28, 'pankaj@gmail.com', 'Senior Developer'],
        ['Ansh', 21, 'ansh@gmail.com', 'Software Developer'],
    ]
)

# We can Column by column

# table.add_column('Name', ['Abhi'])
# table.add_column('Age', [23])
# table.add_column('Email', ['abhi@gmail.com'])
# table.add_column('Occupation', ['Tester'])
print(table)

print("**************************************************\n")

# Importing Data from csv file
# from prettytable import from_csv
#
# with open("students.csv") as fp:
#     mytable = from_csv(fp=fp)
#
# print(mytable)


# importing data from database

# import sqlite3
# from prettytable import from_db_cursor
#
# connection = sqlite3.connect("mydb.db")
# cursor = connection.cursor()
# cursor.execute('SELECT column1, column2, column3 FROM table_name')
# mytable = from_db_cursor(cursor=cursor)
#
# print(mytable)


# Access specific column data using get_string() format.
# print(table.get_string(fields=['Name', 'Age']))

# Changing the alignment of the columns
table.align['Name'] = 'l'
print(table)
print("**************************************************\n")
# There are three types of alignment available here
# 'l' - Left
# 'r' - Right
# 'c' - Center


# Sorting table on the basis of specific column
# Note:- By default sortby parameter sort the column in ascending order, to sort the column in descending order you have to enable property reversesort=True
print("Ascending Order:- ")
print(table.get_string(sortby='Age'))
print("**************************************************\n")
print("Descending Oreder:- ")
table.reversesort = True
print(table.get_string(sortby='Age'))

print("**************************************************\n")
print("Styling the table - MS WORD Friendly")
from prettytable import MSWORD_FRIENDLY
table.set_style(MSWORD_FRIENDLY)
table.border = False
print(table)

# Displaying table in JSON format
print("**************************************************\n")
print("Display table data in json format:-" )
print(table.get_json_string())


# Displaying table in HTML format
print("**************************************************\n")
print("Display table data in json format:- ")
print(table.get_html_string())

# Displaying table in CSV format
print("**************************************************\n")
print("Display table data in csv format:- ")
print(table.get_csv_string())






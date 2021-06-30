from peewee import *

db = SqliteDatabase("testing.db")


# create database 
class Students(Model):
    first_name = CharField()
    last_name = CharField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Students, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


# Python peewee support multiple database 

# SQLite:- SqliteDatabase("testing.db")
# MySQL:- MySQLDatabase('my_app', user='app', password='db_password',host='10.1.0.8', port=3306)
# Postgresql:- PostgresqlDatabase('my_app', user='postgres', password='secret',host='10.1.0.9', port=5432)
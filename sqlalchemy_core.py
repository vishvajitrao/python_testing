from sqlalchemy import create_engine,Table, String,Integer, MetaData, Column, text
from sqlalchemy.sql import select


#create engine
engine = create_engine('sqlite:///sal-core.db', echo=True)

#create object of the MetaData() class
meta = MetaData()

#create cutsomers table
Customers = Table('Customers', meta, Column('id', Integer, primary_key=True),Column('name', String))

meta.create_all(engine)
conn = engine.connect()


# ins = Customers.insert()
# print(str(ins))


# ins = Customers.insert().values(name='XYZ')
# print(str(ins))

# Pick the data from through complite
# print(ins.compile().params)

#executing
# result = conn.execute(ins)
# print(result)


#insert multiple data
# data = [{'name': "XYZ2"},{'name': 'ABC'}, {'name': 'ABC2'}]
# conn = engine.connect()
# conn.execute(ins, data)


#select records from database table
# s = Customers.select(Customers)
# results = conn.execute(s)
# for i in results:
#     print(i)


#fetch all cutomers who id is greater than 2
# s = Customers.select().where(Customers.c.id>2)
# results = conn.execute(s)
# for i in results:
#     print(i)



#textual data
# t = text('SELECT * FROM Customers')
# results = conn.execute(t)
# for i in results:
#     print(i.name)


#Use parameters
# t = text('SELECT * FROM Customers where Customers.id BETWEEN :x AND :y')
# t = t.bindparams(x=3, y=5)
# results = conn.execute(t)
# for i in results:
#     print(i.name)


#upadte records 
# t = Customers.update().where(Customers.c.name=='XYZ').values(name='Python')
# result = conn.execute(t)
# print(result)



#delete records 
# t = Customers.delete().where(Customers.c.id==5)
# result = conn.execute(t)
# print(result)




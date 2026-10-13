from pymongo import MongoClient

con = MongoClient('localhost', 27017)

db = con.db_cadastro

print(type(db))

collections = db.db_cadastro

print(type(collections))
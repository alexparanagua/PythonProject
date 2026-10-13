import pymongo

con = pymongo.MongoClient("mongodb://admin:secret@localhost:27017/")

db = con.cadastrodb

print(db.minhacolecao2.find_one())

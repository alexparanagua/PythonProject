import pymongo

con = pymongo.MongoClient("mongodb://admin:secret@localhost:27017/")

db = con.cadastrodb

for doc in db.minhacolecao2.find():
    print(doc)
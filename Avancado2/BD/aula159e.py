import pymongo

con = pymongo.MongoClient("mongodb://admin:secret@localhost:27017/")

db = con.cadastrodb

colecao = db["minhacolecao2"]

n = colecao.count_documents({})

print(n)
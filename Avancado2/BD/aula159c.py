import pymongo

con = pymongo.MongoClient("mongodb://admin:secret@localhost:27017/")

db = con.cadastrodb

documento1 = {'nome': 'Elon', 'sobrenome': 'Musk', 'twitter': "@Comprou"}

documento2 = {'site': 'http://pypro.com.br', 'youtube': 'http://youtube.com/@pypro_br'}


db.minhacolecao2.insert_one(documento1)
db.minhacolecao2.insert_one(documento2)


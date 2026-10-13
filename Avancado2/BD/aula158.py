from pymongo import MongoClient
import datetime

con = MongoClient("mongodb://admin:secret@localhost:27017/")

db = con.db_cadastro
collections = db.db_cadastro

post1 = {"autor": "Piva Jr",
         "texto": "Linguagem de Programação",
         "tags": ["Python", "C/C++", "Java"],
         "data": datetime.datetime.now(datetime.UTC) }

colecao = db.posts
post_id = colecao.insert_one(post1).inserted_id

post2 = {"autor": "Piva Jr",
         "texto": "Estruturas de Dados",
         "tags": ["Listas", "Pilhas", "Árvores"],
         "data": datetime.datetime.now(datetime.UTC) }

colecao = db.posts
post_id = colecao.insert_one(post2).inserted_id


for post in colecao.find():
    print(post)

print(db.name)

print(db.collection.names)
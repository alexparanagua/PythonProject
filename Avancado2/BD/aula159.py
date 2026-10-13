import pymongo

con = pymongo.MongoClient("mongodb://admin:secret@localhost:27017/")

db = con.cadastrodb

db.create_collection("minhacolecao2")

db.minhacolecao2.insert_one({
    'titulo': 'Curso de Python',
    'descrição': 'Curso completo da Linguagem Python',
    'by': 'pyPRO',
    'url': 'http://www.pypro.com.br',
    'tags': ['python', 'profissional', 'pyPRO'],
    'likes': 200
})

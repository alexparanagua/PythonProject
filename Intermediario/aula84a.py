from datetime import datetime as dd
#from textblob import TextBlob as tx
from deep_translator import GoogleTranslator as gg

def retornadata(hoje):
    #foi removido o translate do TexBlob
    # mes = tx(hoje.strftime('%B')).translate(from_lang='es', to='pt-br')
    mes = gg(source='en', target='pt').translate(hoje.strftime('%B'))
    return f"{hoje.day} de {mes} de {hoje.year}"

hoje = dd.now()
print(retornadata(hoje))
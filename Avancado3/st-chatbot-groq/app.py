import time
from groq import Groq
from config_token import V_GROQ
from config_token import V_MODELO

client = Groq(api_key=V_GROQ)
max_token=512
lista_historico = []

def enviarTextoChat(msg):
    retorno =''
    stream = client.chat.completions.create(
        model=V_MODELO,
        messages=[{"role":"user","content":msg}],
        stream=True,
        max_tokens=max_token
    )
    for chuck in stream:
        if chuck.choices and chuck.choices[0].delta and chuck.choices[0].delta.content:
            resp = chuck.choices[0].delta.content
            print(resp,end='',flush=True)
            retorno+=resp
            time.sleep(0.05)
    lista_historico.append({"msg": msg, "resp": retorno})

while True:
    if lista_historico:
        print('-------------------------------------------------------')
        print('--------------------HISTORICO--------------------------')
        print('-------------------------------------------------------')
        i = 1
        for reg in lista_historico:
            print(f' Msg  {i} : {reg['msg']}')
            print(f' Resp {i} : {reg['resp']}')
            i+=1
    print('-------------------------------------------------------')
    print('*Para sair digite 0')
    print('-------------------------------------------------------')
    envio=input("Chat iniciado: ")
    enviarTextoChat(envio)
    if envio=='0':
        break

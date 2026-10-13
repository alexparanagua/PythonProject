from fastapi import FastAPI

app = FastAPI(title="Minha Primeira API")


@app.get("/")
def raiz():
    return {"mensagem": "API no ar! Bora Pythonar..."}

@app.get("/outrotest")
def outrotest():
    return {"mensagem": "API no ar! Bora Pythonar..."}

'''Como executar: rode uvicorn app:app --reload 
    e acesse http://127.0.0.1:8000/. 
    Depois, acesse /docs para ver a documentação automática.'''
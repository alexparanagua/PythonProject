try:
    aws()
except:
    print("ocorreu algum erro")

try:
    len(9.4)
except TypeError as erro:
    print(f"erro apresentado: {erro}")

def retorna_valor(dic,key):
    try:
        return dic[key]
    except KeyError:
        return None
    except TypeError:
        return None

di = {"nome": "Piva"}
print(retorna_valor(di,5))
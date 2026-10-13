import secrets
import string

alfanumerico = string.ascii_letters + string.digits

#gerando senha de 10 digitos alfanumericos
senha = "".join(secrets.choice(alfanumerico) for _ in range(10))
print(senha)

#gerando token para url seguro
t = secrets.token_urlsafe()
print("token url: ", t)

#gerando token hexadecimal
t = secrets.token_hex()
print('token hexa: ',t)

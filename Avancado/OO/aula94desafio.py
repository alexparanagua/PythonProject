from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=1000, salt_size=10)

    def nome_completo(self):
        return self.__nome+" "+self.__sobrenome

    def checa_senha(self, value):
        return cryp.verify(value,self.__senha)

usuario = Usuario("Alex","Lima", "alexparanagua@gmail.com", "123")

print("Nome Completo: ",usuario.nome_completo())

while True :
    senha_digitada = input("Digite a senha: ")
    if(usuario.checa_senha(senha_digitada)):
        print("Senha correta")
        break
    else :
        print("Senha incorreta")
        continue
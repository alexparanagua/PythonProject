import os

print(os.getcwd())

diretorio = os.path.join(os.getcwd(), 'teste')
if not os.path.exists(diretorio):
    os.mkdir(diretorio)
os.chdir(diretorio)

print(os.getcwd())

os.chdir("..")
print(os.listdir())

scanner = os.scandir()
arquivo = list(scanner)
scanner.close()
print(arquivo)

os.rmdir('pythonteste')
os.rename('teste', 'pythonteste')

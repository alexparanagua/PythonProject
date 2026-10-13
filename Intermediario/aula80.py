import os

print(os.getcwd())

os.chdir("..")

print(os.getcwd())

os.chdir('Intermediario')

print(os.getcwd())

os.chdir('c:\\Users\\alex.lima\\java')

print(os.getcwd())

print(os.path.isabs('Users\\alexlima'))

print(os.name)

print(os.path.join(os.getcwd(),'teste'))
os.mkdir(os.path.join(os.getcwd(),'teste'))


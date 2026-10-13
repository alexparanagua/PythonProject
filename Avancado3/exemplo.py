import pyfiglet

texto = "Alex"
fonte = 'slant'

print(pyfiglet.figlet_format(texto,fonte))

texto = "Alex"
fonte = 'double'

print(pyfiglet.figlet_format(texto,fonte))

texto = "Alex"
fonte = 'univers'

print(pyfiglet.figlet_format(texto,fonte))

texto = "Alex"
fonte = '5x8'

print(pyfiglet.figlet_format(texto,fonte))

#lista de fontes
lista_fontes = [i for i in pyfiglet.FigletFont.getFonts()]
print(lista_fontes)
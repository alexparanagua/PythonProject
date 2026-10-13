import sqlite3

con = sqlite3.connect('empresa.db')
print(type(con))
con.close()
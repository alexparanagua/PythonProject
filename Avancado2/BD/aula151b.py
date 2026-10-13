from mysql.connector import connect

con = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root'
)

print(type(con))

#aqui fazemos operacoes


con.close()
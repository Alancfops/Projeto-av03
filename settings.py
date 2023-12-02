import sqlite3
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
sql_user = '''CREATE TABLE IF NOT EXISTS usuario(
  idUser INTEGER PRIMARY KEY AUTOINCREMENT,
  username varchar(255),
  password varchar(255)
)'''

sql_anot = '''CREATE TABLE IF NOT EXISTS anotacao (
  idAnotacao INTEGER PRIMARY KEY AUTOINCREMENT,
  conteudo varchar(255),
  idUser references usuario(idUser)
)'''

cursor.execute(sql_user)
cursor.execute(sql_anot)

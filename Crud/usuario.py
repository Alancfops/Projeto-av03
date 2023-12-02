from utils import *

@connection_db
def cadastrar(cursor, username, password):
  sql_user='INSERT INTO usuario(username, password) VALUES (?, ?)'
  return cursor.execute(sql_user, [username, password])

@connection_db
def login(cursor, username, password):
    sql_user = 'SELECT * FROM usuario WHERE username = ? AND password = ?'
    return cursor.execute(sql_user, [username, password]).fetchone()

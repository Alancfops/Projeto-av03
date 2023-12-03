from utils import *
import hashlib

@connection_db
def cadastrar(cursor, username, password):
  password_hash = hashlib.sha256(password.encode()).hexdigest()
  sql_user='INSERT INTO usuario(username, password) VALUES (?, ?)'
  return cursor.execute(sql_user, [username, password_hash])

@connection_db
def login(cursor, username, password):
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    sql_user = 'SELECT * FROM usuario WHERE username = ? AND password = ?'
    return cursor.execute(sql_user, [username, password_hash]).fetchone()


@connection_db
def check_existing_user(cursor, username):
    sql_check_user = 'SELECT idUser FROM usuario WHERE username = ?'
    result = cursor.execute(sql_check_user, [username]).fetchone()
    return result is not None



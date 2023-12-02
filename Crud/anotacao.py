from utils import *
@connection_db
def insert_anot(cursor, conteudo, idUser):
    sql_anot = 'INSERT INTO anotacao (conteudo, idUser) VALUES (?, ?)'
    return cursor.execute(sql_anot, [conteudo, idUser])


@connection_db
def update_anot(cursor, conteudo, idAnotacao, idUser):
    sql_anot = 'UPDATE anotacao SET title=? WHERE idAnotacao=? AND idUser=?'
    return cursor.execute( sql_anot, [conteudo, idAnotacao, idUser])

@connection_db
def delete_anot(cursor, idAnotacao, idUser):
    sql_anot = 'DELETE FROM anotacao WHERE idAnotacao=? AND idUser=?'
    return cursor.execute(sql_anot, [idAnotacao, idUser])

@connection_db
def list_anot(cursor, idUser):
    sql_anot = 'SELECT * FROM anotacao WHERE idUser=?'
    return cursor.execute(sql_anot, [idUser]).fetchall()

@connection_db
def listAnot(cursor, idUser):
    sql_anot = '''
        SELECT anotacao.*
        FROM anotacao
        INNER JOIN usuario ON anotacao.idUser = usuario.idUser
        WHERE usuario.idUser = ?
    '''
    return cursor.execute(sql_anot, [idUser]).fetchall()
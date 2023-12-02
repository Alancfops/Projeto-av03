from utils import *
@connection_db
def insert_anot(cursor, conteudo, idUser):
    sql_anot = 'INSERT INTO anotacao (conteudo, idUser) VALUES (?, ?)'
    return cursor.execute(sql_anot, [conteudo, idUser])


@connection_db
def update_anot(cursor, conteudo, idAnotacao, idUsuario):
    sql_anot = 'UPDATE anotacao SET title=? WHERE id=? AND user_id=?'
    return cursor.execute( sql_anot, [conteudo, idAnotacao, idUsuario])

@connection_db
def delete_anot(cursor, idAnotacao, idUsuario):
    sql_anot = 'DELETE FROM anotacao WHERE id=? AND user_id=?'
    return cursor.execute(sql_anot, [idAnotacao, idUsuario])

@connection_db
def list_anot(cursor, idUsuario):
    sql_anot = 'SELECT * FROM anotacao WHERE user_id=?'
    return cursor.execute(sql_anot, [idUsuario]).fetchall()

@connection_db
def listAnot(cursor, idUsuario):
    sql_anot = '''
        SELECT anotacao.*
        FROM anotacao
        INNER JOIN usuario ON anotacao.user_id = usuario.id
        WHERE usuario.id = ?
    '''
    return cursor.execute(sql_anot, [idUsuario]).fetchall()

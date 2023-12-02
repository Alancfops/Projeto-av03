from utils import *
@connection_db
def insert_anot(cursor, conteudo, idUsuario):
    sql_anot = 'INSERT INTO anotacao (conteudo, idUser) VALUES (?, ?)'
    return cursor.execute(sql_anot, [conteudo, idUsuario])


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
        INNER JOIN usuario ON anotacao.idUsuario = usuario.idUsuario
        WHERE usuario.idUsuario = ?
    '''
    return cursor.execute(sql_anot, [idUsuario]).fetchall()

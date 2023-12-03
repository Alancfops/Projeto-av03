from utils import *
@connection_db
def insert_anot(cursor, conteudo, idUser):
    sql_anot = 'INSERT INTO anotacao (conteudo, idUser) VALUES (?, ?)'
    return cursor.execute(sql_anot, [conteudo, idUser])


@connection_db
def update_anot(cursor, conteudo, idAnotacao, idUser):
    sql_anot = 'UPDATE anotacao SET conteudo=? WHERE idAnotacao=? AND idUser=?'
    return cursor.execute( sql_anot, [conteudo, idAnotacao, idUser])

@connection_db
def delete_anot(cursor, idAnotacao, idUser):
    sql_anot = 'DELETE FROM anotacao WHERE idAnotacao=? AND idUser=?'
    return cursor.execute(sql_anot, [idAnotacao, idUser])

@connection_db
def list_anot(cursor, idUser):
    sql_anot = 'SELECT * FROM anotacao WHERE idUser=?'
    return cursor.execute(sql_anot, [idUser]).fetchall()

# @connection_db
# def listAnot(cursor, idUser):
#     sql_anot = '''
#         SELECT anotacao.*
#         FROM anotacao
#         INNER JOIN usuario ON anotacao.idUser = usuario.idUser
#         WHERE usuario.idUser = ?
#     '''
#     return cursor.execute(sql_anot, [idUser]).fetchall()




#Mostrar anotacao de todos os usuarios

# @connection_db
# def listar_anotacoes_usuarios(cursor):
#     sql = '''
#         SELECT usuario.username, anotacao.idAnotacao, anotacao.conteudo
#         FROM usuario
#         INNER JOIN anotacao ON usuario.idUser = anotacao.idUser
#     
#     result = cursor.execute(sql).fetchall()
    
#     for row in result:
#         print(f"Usuário: {row[0]},  Anotação: {row[1]}, Conteúdo: {row[2]}")

#     return result


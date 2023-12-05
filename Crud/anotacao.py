from utils import *


@connection_db
def insert_anot(cursor, conteudo, idUser):
    sql_anot = "INSERT INTO anotacao (conteudo, idUser) VALUES (?, ?)"
    return cursor.execute(sql_anot, [conteudo, idUser])


@connection_db
def update_anot(cursor, conteudo, idAnotacao, idUser):
    sql_anot = "UPDATE anotacao SET conteudo=? WHERE idAnotacao=? AND idUser=?"
    return cursor.execute(sql_anot, [conteudo, idAnotacao, idUser])


@connection_db
def delete_anot(cursor, idAnotacao, idUser):
    sql_anot = "DELETE FROM anotacao WHERE idAnotacao=? AND idUser=?"
    return cursor.execute(sql_anot, [idAnotacao, idUser])


@connection_db
def list_anot(cursor, idUser):
    sql_anot = "SELECT * FROM anotacao WHERE idUser=?"
    return cursor.execute(sql_anot, [idUser]).fetchall()

@connection_db
def historico(cursor):
    sql = """
        SELECT usuario.username, anotacao.idAnotacao, anotacao.conteudo
        FROM usuario
        INNER JOIN anotacao ON usuario.idUser = anotacao.idUser
    """

    resultado = cursor.execute(sql).fetchall()

    for linha in resultado:
        print(f"Usuario: {linha[0]}| Anotacao: {linha[1]}| Conteudo: {linha[2]}")

    return resultado

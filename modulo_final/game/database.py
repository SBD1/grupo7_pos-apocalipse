import psycopg2
import psycopg2.extras

# Função para criar conexão no banco
def conecta_db():
    con = psycopg2.connect(host='localhost',
                           database='Bancos1',
                           user='postgres',
                           password='root')
    return con

# Função para criar tabela no banco
def criar_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

# Função para inserir dados no banco
def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Função para consultas no banco
def consultar_db(sql):
    con = conecta_db()
    cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros

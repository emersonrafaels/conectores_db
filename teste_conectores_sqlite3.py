from main import conectores

# VERIFICANDO OS TIPOS DE QUERY DISPONÍVEIS
query_types = conectores().get_query_types()

"-----------------------------------QUERY COM PARAMS-----------------------------------------------"

# DEFININDO OS PARÂMETROS DE CONEXÃO
caminho_bd_bds = r"BD_TESTES\SQLITE3\DB_PARAMETROS.db"
ssql_bds = "SELECT CAMINHO FROM TBL_CAMINHO_BD WHERE BD = ?"
params_bds = ("DB_MODERNIZASOAS_PARAMETROS",)
tipo_query_bds = query_types[0]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result[1][0][0])

# DEFININDO OS PARÂMETROS DE CONEXÃO
caminho_bd_bds = r"BD_TESTES\SQLITE3\DB_PARAMETROS.db"
ssql_bds = "SELECT CAMINHO FROM TBL_CAMINHO_BD"
params_bds = (None,)
tipo_query_bds = query_types[0]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)

"-----------------------------------QUERY COM PARAMS NONE-----------------------------------------------"

# DEFININDO OS PARÂMETROS DE CONEXÃO
caminho_bd_bds = r"BD_TESTES\SQLITE3\DB_PARAMETROS.db"
ssql_bds = "SELECT CAMINHO FROM TBL_CAMINHO_BD"
params_bds = (None,)
tipo_query_bds = query_types[0]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)

"-----------------------------------QUERY COM INSERT-----------------------------------------------"

caminho_bd_bds = r"BD_TESTES\SQLITE3\DB_LOGS.db"
ssql_bds = "INSERT INTO TBL_ACESSO (FUNCIONAL, DT_HR_ENTRADA) VALUES (?, ?)"
params_bds = ("987297361", "02/09/2021 11:00:00")
tipo_query_bds = query_types[1]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)

"-----------------------------------QUERY COM INSERT MANY-----------------------------------------------"

caminho_bd_bds = r"BD_TESTES\SQLITE3\DB_LOGS.db"
ssql_bds = "INSERT INTO TBL_ACESSO (FUNCIONAL, DT_HR_ENTRADA) VALUES (?, ?)"
params_bds = (("987297361", "02/09/2021 11:00:00"), ("987297362", "02/09/2021 11:00:00"), ("987297363", "02/09/2021 11:00:00"))
tipo_query_bds = query_types[2]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)
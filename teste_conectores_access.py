from main import conectores

# VERIFICANDO OS TIPOS DE QUERY DISPONÍVEIS
query_types = conectores().get_query_types()

"-----------------------------------QUERY COM PARAMS-----------------------------------------------"

# DEFININDO OS PARÂMETROS DE CONEXÃO
caminho_bd_bds = r"BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
ssql_bds = "SELECT processo FROM TBL_PROCESSOS WHERE Codigo_Processo = ?"
params_bds = ("1",)
tipo_query_bds = query_types[0]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)

"-----------------------------------QUERY COM PARAMS NONE-----------------------------------------------"

# DEFININDO OS PARÂMETROS DE CONEXÃO
caminho_bd_bds = r"BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
ssql_bds = "SELECT processo FROM TBL_PROCESSOS"
params_bds = (None,)
tipo_query_bds = query_types[0]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)

"-----------------------------------QUERY COM PARAMS NONE E BD COM SENHA----------------------------------------"

# DEFININDO OS PARÂMETROS DE CONEXÃO
caminho_bd_bds = r"BD_TESTES\ACCESS\BD_TESTE_ACCESS_PASSWORD.accdb"
ssql_bds = "SELECT processo FROM TBL_PROCESSOS"
params_bds = (None,)
tipo_query_bds = query_types[0]
password = "soas"

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds, password)
print(result)

"-----------------------------------QUERY COM INSERT-----------------------------------------------"

caminho_bd_bds = r"BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
ssql_bds = "INSERT INTO TBL_PROCESSOS (Processo) VALUES (?)"
params_bds = ("Leasing",)
tipo_query_bds = query_types[1]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)

"-----------------------------------QUERY COM UPDATE-----------------------------------------------"

caminho_bd_bds = r"BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
ssql_bds = "UPDATE TBL_PROCESSOS SET Processo = ? WHERE Processo = ?"
params_bds = ("Leasing atualizado", "Leasing")
tipo_query_bds = query_types[3]

# EXECUTANDO A QUERY E OBTENDO O RESULTADO
result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)
print(result)
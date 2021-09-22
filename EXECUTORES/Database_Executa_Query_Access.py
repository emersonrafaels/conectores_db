"""

    MICROSERVIÇO RESPONSÁVEL POR TODAS AS INTERAÇÕES
    COM O BANCO DE DADOS (MICROSOFT ACCESS).

    SELECT | INSERT | DELETE | UPDATE | TRUNCATE

    # Arguments
        caminho_banco_dados            - Required : Caminho do Banco de Dados. (String)
        ssql                           - Required : Query a ser executada. (String)
        parametros                     - Required : Parâmetros da query. (Tuple)
        tipo_query                     - Required : Tipo da query a ser executada. (String)
    # Returns
        validador_query                - Required : Validador de execução da Query. (Boolean)

"""


__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "29/08/2021"


import time

from dynaconf import settings
import pyodbc


class Executa_Query():

    """

        MICROSERVIÇO RESPONSÁVEL POR TODAS AS INTERAÇÕES
        COM O BANCO DE DADOS (MICROSOFT ACCESS).

        SELECT | INSERT | INSERT MANY | DELETE | UPDATE | TRUNCATE

        # Arguments
            caminho_banco_dados            - Required : Caminho do Banco de Dados. (String)
            ssql                           - Required : Query a ser executada. (String)
            parametros                     - Required : Parâmetros da query. (Tuple)
            tipo_query                     - Required : Tipo da query a ser executada. (String)
            password                       - Optional : Senha de acesso ao Banco de Dados (String)
        # Returns
            validador_query                - Required : Validador de execução da Query. (Boolean)

    """

    def __init__(self, caminho_banco_dados, ssql, parametros, tipo_query, password="", **kw):

        self.bd = caminho_banco_dados
        self.query = ssql
        self.parametros = parametros
        self.tipo_acao_query = tipo_query
        self.password = password


    @staticmethod
    def open_connection(caminho_bd, password):

        """

            ABRE A CONEXÃO COM O BANCO DE DADOS.
            REALIZA A TENTATIVA DE CONEXÃO COM MÁXIMO DE 10 TENTATIVAS (TIMEOUT).

            # Arguments
                caminho_bd            - Required : Caminho do Banco de Dados. (String)
                password              - Optional : Senha de acesso ao Banco de Dados (String)

            # Returns
                conn                  - Required : Conexão aberta. (conn)
                validador_query       - Required : Validador de execução da Query. (Boolean)

        """

        validador = False
        conn = None
        tentativas = 0

        # INICIA A CONEXÃO COM O BANCO DE DADOS
        while validador is False or tentativas <= 10:

            try:
                # ANALISANDO SE HÁ UMA SENHA PARA CONEXÃO COM O BANCO DE DADOS
                if not password is None and password != "":

                    # O BANCO DE DADOS POSSUI UMA SENHA

                    # OBTENDO OS PARÂMETROS DE CONEXÃO (DRIVER)
                    params_driver_conecction = settings.PARAMS_DRIVER_ACCESS_CONNECTION_WITH_PASSWORD.replace("dbq_value",
                                                                                                              caminho_bd).replace("password_value",
                                                                                                                                  password)

                    # REALIZANDO A CONEXÃO
                    conn = pyodbc.connect(params_driver_conecction)

                else:

                    # O BANCO DE DADOS NÃO POSSUI UMA SENHA

                    # OBTENDO OS PARÂMETROS DE CONEXÃO (DRIVER)
                    params_driver_conecction = settings.PARAMS_DRIVER_ACCESS_CONNECTION_WITH_PASSWORD.replace("dbq_value",
                                                                                                              caminho_bd)

                    # REALIZANDO A CONEXÃO
                    conn = pyodbc.connect(params_driver_conecction)

                validador = True
                return conn, validador

            except Exception as ex:
                print(ex)
                tentativas += 1
                time.sleep(0.5)

        return conn, validador


    @staticmethod
    def close_connection(conn):

        """

            FECHA A CONEXÃO COM O BANCO DE DADOS.

            # Arguments
                conn                  - Required : Conexão aberta. (conn)

            # Returns

        """

        try:
            conn.close()
        except Exception as ex:
            print(ex)


    @staticmethod
    def start_cursor(conn):

        """

            INICIA UM CURSOR PARA ITERAÇÃO COM O BANCO DE DADOS.

            # Arguments
                conn                  - Required : Conexão aberta. (conn)

            # Returns
                cursor                - Required : Cursor iniciado. (cursor)

        """

        try:
            # DEFININDO UM CURSOR
            cursor = conn.cursor()
            return cursor
        except Exception as ex:
            print(ex)
            Executa_Query.close_connection(conn)
            return None


    @staticmethod
    def execute_query_insert_many(conn, ssql, parametros):

        """

            EXECUTA AS QUERYS DE TIPO: INSERT MANY
            PARA SER UTILIZADA PARA INSERT DE MUITOS REGISTROS.

            # Arguments
                conn                  - Required : Conexão aberta. (conn)
                ssql                  - Required : Query a ser executada. (String)
                parametros            - Required : Parâmetros da query. (Tuple)

            # Returns
                validador_query       - Required : Validador de execução da Query. (Boolean)

        """

        cursor = Executa_Query.start_cursor(conn)

        validador = False
        tentativas = 0

        while validador is False and tentativas <= 5:

            try:
                # REALIZANDO A QUERY
                cursor.executemany(ssql, parametros)
                conn.commit()
                validador = True
                return validador
            except Exception as ex:
                print(ex)
                tentativas += 1
                time.sleep(0.5)

        return validador


    @staticmethod
    def execute_query_insert_delete_update_truncate(conn, ssql, parametros):

        """

            EXECUTA AS QUERYS DE TIPO: INSERT | DELETE | UPDATE | TRUNCATE

            # Arguments
                conn                  - Required : Conexão aberta. (conn)
                ssql                  - Required : Query a ser executada. (String)
                parametros            - Required : Parâmetros da query. (Tuple)

            # Returns
                validador_query       - Required : Validador de execução da Query. (Boolean)

        """

        cursor = Executa_Query.start_cursor(conn)

        validador = False
        tentativas = 0

        while validador is False and tentativas <= 5:

            try:
                # REALIZANDO A QUERY
                cursor.execute(ssql, parametros)
                conn.commit()
                validador = True
                return validador
            except Exception as ex:
                print(ex)
                tentativas += 1
                time.sleep(0.5)

        return validador


    @staticmethod
    def get_result_cursor(cursor):

        """

            PERCORRE TODOS OS RESULTADOS OBTIDOS NO CURSOR.

            # Arguments
                cursor                - Required : Cursor aberto com os dados obtidos (cursor)

            # Returns
                result                - Required : Lista com os resultados (List)

        """

        # INICIANDO A LISTA QUE ARMAZENARÁ O RESULTADO
        result = []

        try:
            # PERCORRENDO TODOS OS RESULTADOS
            for row in cursor:
                result.append(row)
        except Exception as ex:
            print(ex)

        return result


    @staticmethod
    def get_result_columns(cursor_description):

        """

            PERCORRE TODOS AS COLUNAS DA TABELA OBTIDOS NO CURSOR.

            # Arguments
                cursor_description    - Required : Cursor aberto com os dados obtidos (cursor)

            # Returns
                result                - Required : Lista com os resultados (List)

        """

        # INICIANDO A LISTA QUE ARMAZENARÁ O RESULTADO
        result = []

        try:
            # PERCORRENDO TODOS OS RESULTADOS
            result = [column[0] for column in cursor_description]
        except Exception as ex:
            print(ex)

        return result


    @staticmethod
    def execute_query_select(conn, ssql, parametros):

        """

            EXECUTA AS QUERYS DE TIPO: SELECT

            # Arguments
                conn                  - Required : Conexão aberta. (conn)
                ssql                  - Required : Query a ser executada. (String)
                parametros            - Required : Parâmetros da query. (Tuple)

            # Returns
                validador_query       - Required : Validador de execução da Query. (Boolean)

        """

        cursor = Executa_Query.start_cursor(conn)

        validador = False
        tentativas = 0

        try:

            if parametros[0] is None and len(parametros) == 1:

                # REALIZANDO A QUERY
                cursor.execute(ssql)

            else:

                # REALIZANDO A QUERY
                cursor.execute(ssql, parametros)

            # DEFININDO O VALIDADOR COMO TRUE
            validador = True

            # RETORNANDO O RESULTADO
            return validador, Executa_Query.get_result_cursor(cursor), Executa_Query.get_result_columns(cursor.description)


        except Exception as ex:
            Executa_Query.close_connection(conn)
            print(ex)


        return validador, None, None


    def Orquestrador_Executa_Query(self):

        validador = False

        # INICIANDO A CONEXÃO COM O BANCO DE DADOS
        conn, validador = Executa_Query.open_connection(self.bd, self.password)

        if validador is True:

            validador = False

            # VALIDANDO O TIPO DE QUERY A SER EXECUTADA

            if self.tipo_acao_query == "INSERT_MANY":

                # EXECUTANDO INSERT MANY
                validador = Executa_Query.execute_query_insert_many(conn,
                                                                    self.query,
                                                                    self.parametros)

            elif self.tipo_acao_query == "INSERT" or self.tipo_acao_query == "UPDATE" or \
                    self.tipo_acao_query == "DELETE" or self.tipo_acao_query == "TRUNCATE":

                # EXECUTANDO QUERY INSERT / UPDATE / DELETE
                validador = Executa_Query.execute_query_insert_delete_update_truncate(conn,
                                                                                      self.query,
                                                                                      self.parametros)

            elif self.tipo_acao_query == "SELECT":

                # EXECUTANDO QUERY SELECT
                validador, resultado_query, resultado_query_colunas = Executa_Query.execute_query_select(conn, self.query, self.parametros)
                Executa_Query.close_connection(conn)
                return validador, resultado_query, resultado_query_colunas

            Executa_Query.close_connection(conn)
            return validador
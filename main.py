from dynaconf import settings

from EXECUTORES.Database_Executa_Query_Access import Executa_Query as Executa_Query_ACCESS
from EXECUTORES.Database_Executa_Query_SQLITE import Executa_Query as Executa_Query_SQLITE3


class conectores():

    def __init__(self):

        self.query_types = settings.QUERY_TYPES
        self.databases = settings.DATABASES


    def get_query_types(self):

        """

            OBTÉM TODAS AS QUERYS DISPONÍVEIS.

            # Arguments

            # Returns
                query_types                - Required : Lista as querys disponíveis (List)

        """

        return self.query_types


    def get_databases_available(self):

        """

            OBTÉM TODAS OS TIPOS BANCOS DE DADOS DISPONÍVEIS.

            # Arguments

            # Returns
                databases                  - Required : Lista as bds disponíveis (List)

        """

        return self.databases


    def execute_query_sqlite(self, caminho_bd, query, params_query, tipo_query):

        """

            MICROSERVIÇO RESPONSÁVEL POR TODAS AS INTERAÇÕES
            COM O BANCO DE DADOS (SQLITE3).

            SELECT | INSERT | INSERT MANY | DELETE | UPDATE | TRUNCATE

            # Arguments
                caminho_banco_dados            - Required : Caminho do Banco de Dados. (String)
                ssql                           - Required : Query a ser executada. (String)
                parametros                     - Required : Parâmetros da query. (Tuple)
                tipo_query                     - Required : Tipo da query a ser executada. (String)
            # Returns
                validador_query                - Required : Validador de execução da Query. (Boolean)

        """

        result = Executa_Query_SQLITE3(caminho_bd, query,
                                       params_query, tipo_query).Orquestrador_Executa_Query()
        return result


    def execute_query_access(self, caminho_bd, query, params_query, tipo_query, password=""):

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

        result = Executa_Query_ACCESS(caminho_bd, query,
                                      params_query, tipo_query,
                                      password).Orquestrador_Executa_Query()
        return result


    def execute_query_sqlserver(self):

        print("CONECTANDO SQLSERVER")
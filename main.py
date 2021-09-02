from dynaconf import settings

from EXECUTORES.Database_Executa_Query_SQLITE import Executa_Query as Executa_Query_SQLITE3


class conectores():

    def __init__(self):

        self.query_types = settings.QUERY_TYPES


    def get_query_types(self):

        return self.query_types


    def execute_query_sqlite(self, caminho_bd, query, params_query, tipo_query):

        result = Executa_Query_SQLITE3(caminho_bd, query, params_query, tipo_query).Orquestrador_Executa_Query()
        return result


    def execute_query_sqlserver(self):

        print("CONECTANDO SQLSERVER")
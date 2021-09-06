from unittest import main, TestCase

from main import conectores


class Testes(TestCase):


    def test_seleciona_tipos_query_disponiveis(self):

        """
            OBTÉM AS QUERYS DISPONÍVEIS (CRUDS).

            É ESPERADO QUE O RETORNO SEJA UMA LISTA DE DADOS.
        """

        esperado = list

        # VERIFICANDO OS TIPOS DE QUERY DISPONÍVEIS
        query_types = conectores().get_query_types()

        # REALIZANDO OS TESTES
        self.assertIsInstance(query_types, esperado)


    def test_select_sqlite3_com_parametros(self):

        # DEFININDO O VALOR ESPERADO
        esperado = r'C:\Users\Emerson\Desktop\UFABC\Cursos\Python\Tkinter\Moderniza\ModernizaSOAS\DB_ModernizaSOAS'

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\SQLITE3\DB_PARAMETROS.db"
        ssql_bds = "SELECT CAMINHO FROM TBL_CAMINHO_BD WHERE BD = ?"
        params_bds = ("DB_MODERNIZASOAS_PARAMETROS",)
        tipo_query_bds = "SELECT"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertEqual(result[1][0][0], esperado)


    def test_select_sqlite3_sem_parametros(self):

        # DEFININDO O VALOR ESPERADO
        esperado = r'C:\Users\Emerson\Desktop\UFABC\Cursos\Python\Tkinter\Moderniza\ModernizaSOAS\DB_ModernizaSOAS'

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\SQLITE3\DB_PARAMETROS.db"
        ssql_bds = "SELECT CAMINHO FROM TBL_CAMINHO_BD"
        params_bds = (None,)
        tipo_query_bds = "SELECT"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertEqual(result[1][0][0], esperado)


    def test_insert_sqlite3_com_parametros(self):

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\SQLITE3\DB_LOGS.db"
        ssql_bds = "INSERT INTO TBL_ACESSO (FUNCIONAL, DT_HR_ENTRADA) VALUES (?, ?)"
        params_bds = ("987297361", "02/09/2021 11:00:00")
        tipo_query_bds = "INSERT"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertTrue(result)


    def test_insert_many_sqlite3_com_parametros(self):

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\SQLITE3\DB_LOGS.db"
        ssql_bds = "INSERT INTO TBL_ACESSO (FUNCIONAL, DT_HR_ENTRADA) VALUES (?, ?)"
        params_bds = (("987297361", "02/09/2021 11:00:00"), ("987297362", "02/09/2021 11:00:00"),
                      ("987297363", "02/09/2021 11:00:00"))
        tipo_query_bds = "INSERT_MANY"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertTrue(result)


if __name__ == '__main__':

    # EXECUTOR DE TESTES
    main()
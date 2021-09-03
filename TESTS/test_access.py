from unittest import main, TestCase

from main import conectores


class Testes(TestCase):


    def test_seleciona_tipos_query_disponiveis(self):

        esperado = list

        # VERIFICANDO OS TIPOS DE QUERY DISPONÍVEIS
        query_types = conectores().get_query_types()

        # REALIZANDO OS TESTES
        self.assertIsInstance(query_types, esperado)


    def test_seleciona_tipos_bds_disponiveis(self):

        esperado = list

        # VERIFICANDO OS TIPOS DE BDS DISPONÍVEIS
        query_types = conectores().get_databases_available()

        # REALIZANDO OS TESTES
        self.assertIsInstance(query_types, esperado)


    def test_select_access_com_parametros(self):

        # DEFININDO O VALOR ESPERADO
        esperado = r'Liberação'

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
        ssql_bds = "SELECT processo FROM TBL_PROCESSOS WHERE Codigo_Processo = ?"
        params_bds = ("1",)
        tipo_query_bds = "SELECT"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertEqual(result[1][0][0], esperado)


    def test_select_access_sem_parametros(self):

        # DEFININDO O VALOR ESPERADO
        esperado = list

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
        ssql_bds = "SELECT processo FROM TBL_PROCESSOS"
        params_bds = (None,)
        tipo_query_bds = "SELECT"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertTrue(result[0], esperado)


    def test_select_access_sem_parametros_com_senha(self):

        # DEFININDO O VALOR ESPERADO
        esperado = list

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\ACCESS\BD_TESTE_ACCESS_PASSWORD.accdb"
        ssql_bds = "SELECT processo FROM TBL_PROCESSOS"
        params_bds = (None,)
        tipo_query_bds = "SELECT"
        password = "soas"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_access(caminho_bd_bds, ssql_bds,
                                                   params_bds, tipo_query_bds,
                                                   password)

        # REALIZANDO OS TESTES
        self.assertTrue(result[0], esperado)


    def test_insert_access_com_parametros(self):

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
        ssql_bds = "INSERT INTO TBL_PROCESSOS (Processo) VALUES (?)"
        params_bds = ("Leasing",)
        tipo_query_bds = "INSERT"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertTrue(result)


    def test_insert_many_access_com_parametros(self):

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
        ssql_bds = "INSERT INTO TBL_PROCESSOS (Processo) VALUES (?)"
        params_bds = (("Leasing1",), ("Leasing2",), ("Leasing3",))
        tipo_query_bds = "INSERT_MANY"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertTrue(result)


    def test_update_access_com_parametros(self):

        # DEFININDO OS PARÂMETROS DE CONEXÃO
        caminho_bd_bds = r"..\BD_TESTES\ACCESS\BD_TESTE_ACCESS.accdb"
        ssql_bds = "UPDATE TBL_PROCESSOS SET Processo = ? WHERE Processo = ?"
        params_bds = ("Leasing atualizado", "Leasing")
        tipo_query_bds = "UPDATE"

        # EXECUTANDO A QUERY E OBTENDO O RESULTADO
        result = conectores().execute_query_access(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)

        # REALIZANDO OS TESTES
        self.assertTrue(result)


if __name__ == '__main__':

    # EXECUTOR DE TESTES
    main()
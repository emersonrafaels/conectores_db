


<h1 align="center">
    <img alt="Conectores DB" title="#ConectoresDB" src="./assets/banner.png" />
</h1>

<h4 align="center"> 
	🚧 Conectores DB 1.0 🚀 em desenvolvimento... 🚧
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/emersonrafaels/conectores_db?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/emersonrafaels/conectores_db">

  	
  <a href="https://www.linkedin.com/in/emerson-rafael/">
    <img alt="Siga no Linkedin" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
	
  
  <a href="https://github.com/emersonrafaels/conectores_db/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/emersonrafaels/deep_check_orientation">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/emersonrafaels/conectores_db/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/emersonrafaels/deep_check_orientation?style=social">
  </a>
</p>


## 💻 Sobre o projeto

📦 **Conectores DB** é um projeto que permite **interagir com diferentes Banco de Dados** realizando **Abertura da Conexão**, **Execução da Query** e **Fechamento da Conexão**.

Atualmente funcionando para:

 1. SQLITE3
 2. Microsoft Access

## 🛠  Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python]

## 🚀 Como executar o projeto

1. **Instalando**: pip install -r requirements.txt
2. **Importando**: from main import conectores

Ex: Realizando querys com o SQLITE:

    from main import conectores
    
    # VERIFICANDO OS TIPOS DE QUERY DISPONÍVEIS  
	query_types = conectores().get_query_types()
	
	# QUERY COM PARAMS
	# DEFININDO OS PARÂMETROS DE CONEXÃO  
	caminho_bd_bds = r"BD_TESTES\SQLITE3\DB_PARAMETROS.db"  
	ssql_bds = "SELECT CAMINHO FROM TBL_CAMINHO_BD WHERE BD = ?"  
	params_bds = ("DB_MODERNIZASOAS_PARAMETROS",)  
	tipo_query_bds = query_types[0]  
  
	# EXECUTANDO A QUERY E OBTENDO O RESULTADO  
	result = conectores().execute_query_sqlite(caminho_bd_bds, ssql_bds, params_bds, tipo_query_bds)  
	


## ➊ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas (O download pode ser realizado pela própria página do Python ou Anaconda):
[Python](https://www.anaconda.com/products/individual).

## 💾 Databases - CRUD's disponíveis
Classificador de tipo de PDF usando cálculo de percentual de texto contido no PDF.

| Banco de Dados        | Ações disponíveis 
| ------------- |:--------------------:|
| SQLITE3| SELECT, INSERT, INSERT MANY, UPDATE, DELETE, TRUNCATE  |
| Microsoft Access | SELECT, INSERT, INSERT MANY, UPDATE, DELETE, TRUNCATE  |

## [≝] Testes
Os testes estão na pasta: **TESTS/***.
Nela é possível verificar os testes disponíveis em arquivos individuais para cada um dos bancos de dados disponíveis.

Os bancos utilizados nos testes estão em: **BD_TESTES/***

## 📝 Licença

Este projeto está sob a licença MIT.

Feito com ❤️ por **Emerson Rafael** 👋🏽 [Entre em contato!](https://www.linkedin.com/in/emerson-rafael/)

[Python]: https://www.python.org/downloads/
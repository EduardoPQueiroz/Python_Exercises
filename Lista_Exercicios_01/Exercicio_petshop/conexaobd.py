import pyodbc
import pandas as pd
import os
os.system("cls")



#SubAlgoritimos

def listar_pets() -> None:
    lista_dados = []
            inst_consulta.execute("select * from petshop")
            data = inst_consulta.fetchall()

            # Insere os valores da tabela na lista
            for dt in data:
                lista_dados.append(dt) 

            #Odena a lista
            lista_dados = sorted(lista_dados)

            #gera um dataFrame com os dados da lista utilizando pandas
            dados_df = pd.DataFrame.from_records(lista_dados, columns = ['Id', 'Tipo', 'Nome', 'Idade'], index = 'Id')

            #verifica de não há registros de dados no dataFrame
            if dados_df.empty:
                print("-Não há pets cadastrados-")
            else:
                print(dados_df)
            input("pressione algo para continuar. . .")


#Programa principal
try:
    #Configurar as informações de conexãi
    server = 'localhost'
    database = 'petshop'
    username = 'sa'
    password = '*123456HAS*'
     
    #  Estabelecer Conexão
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True 
    print("Conexão efetuada com sucesso!")


while conexao == True:
    os.system("cls")
    print("MENU")
    print("0 - SAIR")
    print("1 - CADASTRAR PETS")
    print("2 - LISTAR PETS")
    print("3 - EDITAR PET")
    print("4 - EXCLUIR PET")
    print("5 - EXCLUIR TODOS OS PETS")


    escolha = int(input("Escolha: "))
    os.system("cls")
    match escolha:
        case 0:
            conexao = False
        case 1: 
            try:
                #Coletando os dados do usuário
                tipo = str(input("Insira o tipo de Pet: "))
                nome = str(input("Insira o nome do PET: "))
                idade = int(input("Insira a idade do seu Pet: "))

                # Montando a instruçaõ SQL em uma string
                cadastro = f"""
                INSERT INTO petshop (tipo_pet, nome_pet, idade)
                VALUES('{tipo}', '{nome}', {idade})
                """
                inst_cadastro.execute(cadastro) #Execurta a instrução no banco de dados 
                conn.commit()
            except ValueError:
                print("Digite uma idade numérica!")
            except:
                print("Erro em alguma transação na tabela")
            else:
                print("Dados gravados com sucesso!")
        
        case 2:

            listar_pets()

      #  case 3:

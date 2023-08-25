from databricks import sql
import pandas as pd
import os

connection = sql.connect(
                        server_hostname = "adb-6239857225875003.3.azuredatabricks.net",
                        http_path = "/sql/1.0/warehouses/83abf734db81005f",
                        access_token = "dapi4b7f8e8b7e90fd45be3a72103921fb89-3")

names = 'datathon_04.db_datathon.'
cursor = connection.cursor()

cursor.execute("SELECT ASK_OPEN_AI('Clientes com proposta emitida') FROM datathon_04.db_datathon.base_proposta_clientes_unificado WHERE cd_corretor_lider = 879")

def getRecom(id=879):

  cursor.execute(f"SELECT * FROM datathon_04.db_datathon.base_proposta_clientes_unificado WHERE cd_corretor_lider = {id} ")
  result = cursor.fetchall()
  # for row in result:
  #   print(row)

  return pd.DataFrame(result)

def getProdutosVida():

  cursor.execute(f"SELECT * FROM datathon_04.db_datathon.base_proposta_clientes_unificado WHERE cd_corretor_lider = {id} ")
  result = cursor.fetchall()
  # for row in result:
  #   print(row)

  return pd.DataFrame(result)

def getProdutosPrev():

  cursor.execute(f"SELECT * FROM datathon_04.db_datathon.base_proposta_clientes_unificado WHERE cd_corretor_lider = {id} ")
  result = cursor.fetchall()
  # for row in result:
  #   print(row)

  return pd.DataFrame(result)

def closeCon():
  cursor.close()
  connection.close()

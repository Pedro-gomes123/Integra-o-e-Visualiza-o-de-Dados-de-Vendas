import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

arquivo = 'PLANILHA DE VENDAS C&L-  2025.xlsx'

colunas = ['EMPRESA', 'VALOR', 'VENDEDOR', 'VENCIMENTO']

dadosCeL = pd.read_excel(arquivo, sheet_name='C&L JAN')
dadosCJ = dadosCeL[colunas]

dadosCeL = pd.read_excel(arquivo, sheet_name='C&L FEV')
dadosCF = dadosCeL[colunas]

dadoscel = pd.read_excel(arquivo, sheet_name='C&L MAR')
dadosCM = dadoscel[colunas]

dadosCeL = pd.read_excel(arquivo, sheet_name='C&L ABR')
dadosCA = dadosCeL[colunas]

dadosCeL = pd.read_excel(arquivo, sheet_name='C&L MAIO')
dadosCM = pd.concat([dadosCM, dadosCeL[colunas]], ignore_index=True)

dadosCeL = pd.read_excel(arquivo, sheet_name='C&L JUN')
dadosCJ = pd.concat([dadosCJ, dadosCeL[colunas]], ignore_index=True)

dadosdc = pd.read_excel(arquivo, sheet_name='D CARV JAN')
dadosdj = dadosdc[colunas]

dadosdc = pd.read_excel(arquivo, sheet_name='D CARV FEV')
dadosdf = dadosdc[colunas]

dadosdc = pd.read_excel(arquivo, sheet_name='D CARV MAR')
dadosdm = dadosdc[colunas]

dadosdc = pd.read_excel(arquivo, sheet_name='D CARV ABR')
dadosdm = pd.concat([dadosdm, dadosdc[colunas]], ignore_index=True)

dadosdc = pd.read_excel(arquivo, sheet_name='D CAR MAIO')
dadosdj = pd.concat([dadosdj, dadosdc[colunas]], ignore_index=True)

dadosdc = pd.read_excel(arquivo, sheet_name='D CAR JUN')
dadosdf = pd.concat([dadosdf, dadosdc[colunas]], ignore_index=True)

dados_unificado = pd.concat([dadosCJ, dadosCF, dadosCM, dadosdj, dadosdf, dadosdm], ignore_index=True)

print(dados_unificado.info())
dados_unificado['VALOR'] = pd.to_numeric(dados_unificado['VALOR'], errors='coerce')
print(dados_unificado['VALOR'].dtype)
Vendas = dados_unificado['VALOR'].sum()
valor_formatado = f"{Vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f'Total de Vendas: {valor_formatado}')

vendas_por_vendedor = dados_unificado.groupby('VENDEDOR')['VALOR'].sum().sort_values(ascending=False)

vendas_por_vendedor_formatado = vendas_por_vendedor.apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

print("\nComparativo de vendas por vendedor:")
print(vendas_por_vendedor_formatado)

# Salvar os dados no MySQL
usuario = 'root'
senha = 'Pedro2006$'
host = 'localhost'
porta = 3306
banco = 'vendas_db'  

engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}')

dados_unificado.to_sql('vendas', con=engine, if_exists='append', index=False)

print('Dados inseridos no MySQL com sucesso!')

tabela = 'vendas'



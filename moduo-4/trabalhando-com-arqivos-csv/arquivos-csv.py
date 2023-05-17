# formas
# 1metodos internos csv
import csv
with open('advertising.csv', 'r', encoding='utf8') as arquivo:
     arquivo_csv = csv.reader(arquivo, delimiter=',')
     print(arquivo_csv)
     for i, linha in enumerate(arquivo_csv):
          if i == 0:
               print(f'indice da lista {i}')
               print(linha)

# 2 bibliotecas pandas
# pip install pandas
# pip install numpy
# pip install openpyxl

import pandas as pd

tabela = pd.read_csv('advertising.csv', sep=',')
print(tabela)

# total investido em televisao
print(tabela['TV'].sum())
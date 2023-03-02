import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados/dataframe.csv', parse_dates = ['Data'], usecols = list(range(0,6)))

print(df.dtypes)
print(df.head())


# Exercício 1 - Qual o valor máximo da coluna Minutos?
print(df[5:].max())
# Exercício 2 - Qual o valor mínimo de distância acima de 2.0?


# Exercício 3 - Crie um plot com a frequência acumulada da coluna Distancia.


# Exercício 4 - Qual o dia da semana no índice de posição zero?


# Exercício 5 - Qual o dia da semana nos índices nas 5 primeiras posições?


# Exercício 6 - Extraia todos os dias da semana (em formato texto) e insira em uma nova coluna no dataframe df.


# Exercício 7 - Crie um gráfico de barras com o total da distância percorrida em cada dia da semana.


# Exercício 8 - Delete a coluna Tempo do dataframe df.


# Exercício 9 - Qual o total de corridas de taxi por dia da semana?


# Exercício 10 - Qual a média para cada uma das colunas por dia da semana?
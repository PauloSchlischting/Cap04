
#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Configurações dos parametros dos graficos
from matplotlib import rcParams

rcParams['figure.figsize'] = 12, 4
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'

#Carregando os dados
df = pd.read_csv("dados/dataset.csv")
print(df.shape)
print(df.info)
df.head()
print(df.sample(5))
print(df.tail())


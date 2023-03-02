# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações dos parametros dos graficos
from matplotlib import rcParams

rcParams['figure.figsize'] = 12, 4
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'

# Carregando os dados
df = pd.read_csv("dados/dataset.csv")
print(df.shape)
print(df.info)
df.head()
print(df.sample(5))
print(df.tail())

print(df.dtypes)

# Separando as variaveis em numericas e categóricas

# Lista de colunas categóricas
cats = ['corredor_armazem',
        'modo_envio',
        'prioridade_produto',
        'genero']

# Lista de colunas numéricas
nums = ['numero_chamadas_cliente',
        'avaliacao_cliente',
        'custo_produto',
        'compras_anteriores',
        'desconto',
        'peso_gramas']

target = ['entregue_no_prazo']

# Explorando as variáveis numéricas

# Resumo das variáveis numéricas
print(df[nums].describe())

print(df['custo_produto'].hist())
#plt.show()

#Explorando as variáveis categóricas

#Resumo das variáveis categóricas
print(df[cats].describe())

for col in cats:
    print(f'''Total de registros por categoria da Variável {col}:''')
    print(df[col].value_counts())
    print()

features = nums
for i in range(0,len(features)):
    plt.subplot(1, len(features), i + 1)
    sns.boxplot(y=df[features[i]], color='magenta', orient='v')
    plt.tight_layout()
    #plt.show()

#Analise univariada - Dist plot

plt.figure(figsize=(20, 10))
for i in range(0, len(nums)):
    plt.subplot(3, 3, i + 1)
    sns.histplot(x=df[features[i]], kde=True, color='green')
    plt.xlabel(features[i])
    plt.tight_layout()
#plt.show()

#Analise Bivariada - Mapa de correlação
corr_df = df[nums].corr()

plt.figure(figsize=(8, 10))
sns.heatmap(df[nums].corr(), cmap='Blues', annot=True, fmt='.2f')
#plt.show()

#Pair plot
#sns.pairplot(df[nums], diag_kind='kde')
#plt.show()

#Colunas categóricas x variável target

features = cats
for i in range(0, len(features)):
    plt.subplot(2, 2, i+1)
    sns.countplot(data=df, x=features[i], hue='entregue_no_prazo')
    plt.tight_layout()
#plt.show()


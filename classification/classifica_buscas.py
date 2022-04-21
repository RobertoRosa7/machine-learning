from dados import carregar_buscas
import pandas as pd

x, y = carregar_buscas()

df = pd.read_csv('data/busca.csv')
y_df = df['comprou']
x_df = df[['home', 'busca', 'logado']]

x_dummies_df = pd.get_dummies(x_df)
y_dummies_df = y_df

x = x_dummies_df.values
y = y_dummies_df.values

print(y)

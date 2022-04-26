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

porcentagem_treino = 0.9
tamanho_de_treino = int(porcentagem_treino * len(y))
tamanho_de_teste = int(len(y) - tamanho_de_treino)

treino_x = x[:tamanho_de_treino]
treino_y = y[:tamanho_de_treino]

teste_x = x[-tamanho_de_teste:]
teste_y = y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_x, treino_y)

resultado = modelo.predict(teste_x)
diferencas = resultado - teste_y

acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_y)
taxa_acertos = 100.0 * total_acertos / total_elementos


print(total_elementos)
print(taxa_acertos)


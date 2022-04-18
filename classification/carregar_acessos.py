#-*- coding: UTF-8 -*-
from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

x,y = carregar_acessos()
model = MultinomialNB()
model.fit(x, y)
# print(model.predict([[1,0,1], [0,1,0], [1,0,0], [1,1,1]]))
result = model.predict(x)
differ = result - y
accuracy = [d for d in differ if d == 0]
total = len(accuracy)
total_elem = len(x)
taxa = 100.0 * total / total_elem

print(taxa)

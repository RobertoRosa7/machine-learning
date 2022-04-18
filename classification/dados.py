#-*- coding: UTF-8 -*-
import csv, sys, os

sys.path.append(os.path.abspath(os.getcwd()))
# print()

def carregar_acessos():
  x = []
  y = []

  # path = os.getcwd() + '/classification/data/acesso.csv'
  with open('data/acesso.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    leitor.__next__()
    for home,como_funciona,contato, comprou in leitor:
      x.append([int(home), int(como_funciona), int(contato)])
      y.append(int(comprou))
  return x, y
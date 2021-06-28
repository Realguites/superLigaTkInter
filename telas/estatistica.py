from tkinter import *
from tkinter import ttk
import requests

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 

num = 0
total = 0
maior = 0
carros_maiores = []
destaques = 0
clubes = None

def dados():
  global num, total, maior, destaques, carros, carros_maiores

  num = 0
  total = 0
  maior = 0
  carros_maiores = []
  destaques = 0

  URL_CLUBES = "http://localhost:3000/clubes"
  r = requests.get(url=URL_CLUBES)
  clubes = r.json()

  for carro in carros:
    num += 1
    total += float(carro["preco"])
    if float(carro["preco"]) > maior:
      maior = float(carro["preco"])      
    if carro["destaque"]:
      destaques += 1  

  # percorre a lista para identificar os veículos de maior valor (pode ser mais que 1)
  for carro in carros:
    if float(carro["preco"]) == maior:
      carros_maiores.append(carro["modelo"])

def monta_labels(notebook):

  cadframe = ttk.Frame(notebook, width=680, height=580)

  dados()

  totalf = locale.currency(total, grouping=True, symbol=None)
  media = total / num
  mediaf = locale.currency(media, grouping=True, symbol=None)
  maiorf = locale.currency(maior, grouping=True, symbol=None)

  # Labels para exibir dados
  ttk.Label(cadframe, text=f"Número de Veículos Cadastrados: {num}").grid(column=1, row=1, sticky=W)
  ttk.Label(cadframe, text=f"Número de Veículos em Destaque: {destaques}").grid(column=1, row=2, sticky=W)
  ttk.Label(cadframe, text=f"Total do Preço dos Veículos R$: {totalf}").grid(column=1, row=3, sticky=W)
  ttk.Label(cadframe, text=f"Preço Médio dos Veículos R$: {mediaf}").grid(column=1, row=4, sticky=W)
  ttk.Label(cadframe, text=f"Maior Preço de Veículo R$: {maiorf}").grid(column=1, row=5, sticky=W)
  ttk.Label(cadframe, text=f"Veículo(s) de Maior Preço: {', '.join(carros_maiores)}").grid(column=1, row=6, sticky=W)

  for child in cadframe.winfo_children(): 
    child.grid_configure(padx=20, pady=10)    

  return cadframe
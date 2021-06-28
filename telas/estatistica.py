from tkinter import *
from tkinter import ttk
import requests

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 


total = 0
maior = 0
destaques = 0
clubes = None

def dados():
  global total, destaques, clubes
  total = 0
  destaques = 0

  URL_CLUBES = "http://localhost:3000/clubes"
  r = requests.get(url=URL_CLUBES)
  clubes = r.json()
  total = len(clubes)
  for clube in clubes:  
    if clube["destaque"]:
      destaques += 1  

def monta_labels(notebook):

  cadframe = ttk.Frame(notebook, width=680, height=580)

  dados()

  ttk.Label(cadframe, text=f"Número de Clubes Cadastrados: {total}").grid(column=1, row=1, sticky=W)
  ttk.Label(cadframe, text=f"Número de Clubes em Destaque: {destaques}").grid(column=1, row=2, sticky=W)
  
  for child in cadframe.winfo_children(): 
    child.grid_configure(padx=20, pady=10)    

  return cadframe
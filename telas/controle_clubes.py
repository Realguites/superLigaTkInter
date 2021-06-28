from tkinter import *
from tkinter import ttk
import requests

URL_CLUBES = "http://localhost:3000/clubes"


divisao = {0,1,2,3,4}
clubes = {}

def agrupa_clubes():
  global clubes, divisao
  divisao = {}
  r = requests.get(url=URL_CLUBES)
  clubes = r.json()
  for clube in clubes:
    if clube["divisao"] in divisao:
      divisao[clube["divisao"]] += 1
    else:
      divisao[clube["divisao"]] = 1  

def preenche_grid_clubes(tree):
    agrupa_clubes()
    # adding data to the treeview
    for div, num in divisao.items():
        tree.insert('', END, values=(div, num))

def monta_grid_divisao(notebook):
  gridframe = ttk.Frame(notebook, width=250, height=580)

  # columns
  columns = ('#1', '#2')

  tree = ttk.Treeview(gridframe, columns=columns, show='headings')

  # define headings
  tree.heading('#1', text='Divisão')
  tree.heading('#2', text='Nº de clubes')

  # largura de cada coluna
  tree.column("#1", width=150)
  tree.column("#2", width=400, anchor=CENTER)

  preenche_grid_clubes(tree)

  # bind the select event
  def item_selected(event):
    selected = tree.focus()
    temp = tree.item(selected, 'values')

  def limpa():
      # limpa a grid  
    for i in tree.get_children():
        tree.delete(i) 
  def atualizar():
    limpa()
    preenche_grid_clubes(tree) 

  ttk.Button(gridframe, text="Atualizar", command=atualizar).grid(column=3, row=1, sticky=W)

  tree.bind('<<TreeviewSelect>>', item_selected)

  tree.grid(row=1, column=0, sticky='nsew', padx=(10, 0), pady=10)

  # add a scrollbar
  scrollbar = ttk.Scrollbar(gridframe, orient=VERTICAL, command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  scrollbar.grid(row=1, column=1, sticky='ns')

  return gridframe
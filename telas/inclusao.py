from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import requests

URL_CLUBES = "http://localhost:3000/clubes"
r = requests.get(url=URL_CLUBES)
clubes = r.json()
#print(clubes)

#URL_MARCAS = "http://localhost:3000/marcas"
#r = requests.get(url=URL_MARCAS)
#marcas = r.json()
#print(marcas)

#lista = []
# percorre a lista de dicionÃ¡rios
#for marca in marcas:
  #lista.append(marca["nome"])

def monta_formulario(notebook):
    cadframe = ttk.Frame(notebook, width=680, height=580)
    
    # Labels do FormulÃ¡rio
    ttk.Label(cadframe, text="Nome: ").grid(column=1, row=1, sticky=E)
    ttk.Label(cadframe, text="Foto: ").grid(column=1, row=2, sticky=E)
    ttk.Label(cadframe, text="Divisão: ").grid(column=1, row=3, sticky=E)
    ttk.Label(cadframe, text="Destaque: ").grid(column=1, row=4, sticky=E)

    # Campos de Entrada de Dados
    nome = StringVar()
    nome_entry = ttk.Entry(cadframe, width=40, textvariable=nome)
    nome_entry.grid(column=2, row=1, sticky=W)

    foto = StringVar()
    ttk.Entry(cadframe, width=10, textvariable=foto).grid(column=2, row=2, sticky=W)
    
    divisao = StringVar()
    ttk.Entry(cadframe, width=10, textvariable=divisao).grid(column=2, row=3, sticky=W)
    

    destaque = StringVar()
    ttk.Entry(cadframe, width=60, textvariable=destaque).grid(column=2, row=4, sticky=W)

    def incluir():
      dados = {"nome": nome.get(),
               "foto": foto.get(),
               "divisao": divisao.get(),
               "destaque": destaque.get()}

      response = requests.post(URL_CLUBES, json=dados)
      print(response.text)
      print(response.status_code)

      if response.status_code == 201:
        showinfo(title='Clube Cadastrado',
                 message=f"código do Clube {response.text}")
      else:
        showinfo(title='Erro...',
                 message="Clube não cadastrado")

    ttk.Button(cadframe, text="Incluir Clube", command=incluir).grid(column=2, row=6, sticky=W)

    for child in cadframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    return cadframe
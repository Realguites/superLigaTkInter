from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,askyesno
import requests

URL_CLUBES = "http://localhost:3000/clubes"
r = requests.get(url=URL_CLUBES)
clubes = r.json()

def atualiza_lista():
  global clubes
  r = requests.get(url=URL_CLUBES)
  clubes = r.json()

def monta_grid(notebook):
    gridframe = ttk.Frame(notebook, width=800, height=780)

    # columns
    columns = ('#1', '#2', '#3', '#4', '#5')

    tree = ttk.Treeview(gridframe, columns=columns, show='headings')

    # define headings
    tree.heading('#1', text='Id')
    tree.heading('#2', text='Nome')
    tree.heading('#3', text='Foto')
    tree.heading('#4', text='Divisão')
    tree.heading('#5', text='Destaque')

    # largura de cada coluna
    tree.column("#1", width=180)
    tree.column("#2", width=100)
    tree.column("#3", width=60, anchor=CENTER)
    tree.column("#4", width=100, anchor=E)
    tree.column("#5", width=100, anchor=E)

    # adding data to the treeview
    for clube in clubes:
      tree.insert('', END, values=(clube["id"],clube["nome"], clube["foto"], clube["divisao"], clube["destaque"]))



    # bind the select event
    def item_selected(event):
                    
        for selected_item in tree.selection():
            # dictionary
            item = tree.item(selected_item)
            if (item['values'][4] !=  1) :
                answer = askyesno(title='Confirmação',message='Deseja tornar este clube um destaque?')
                if answer:
                  requests.put(url=URL_CLUBES+"/destacar/" + str(item['values'][0]))
                  atualiza_lista()
            else:
                answer = askyesno(title='Confirmação',message='Este clube é um destaque, deseja retirá-lo?')
                if answer:
                  requests.put(url=URL_CLUBES+"/destacar/" + str(item['values'][0]))
                  atualiza_lista()

            limpa()
            exibir_todos()
            
    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=1, column=0, sticky='nsew', padx=(10, 0), pady=10)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(gridframe, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')
    
    # add a scrollbar
    scrollbar = ttk.Scrollbar(gridframe, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

    # ----------------------------------------------------- frame para filtros e ordenações
    filter_order_frame = ttk.Frame(gridframe)
    filter_order_frame.grid(row=2, column=0, columnspan=2, pady=12)

    # ----------------------------------------------------- Filtros
    filterframe = ttk.Frame(filter_order_frame)
    filterframe.grid(row=0, column=0, padx=(10, 20))
    
    nome = StringVar()

    def limpa():
          # limpa a grid  
      for i in tree.get_children():
        tree.delete(i)

    def exibir_todos():
      limpa()
      for clube in clubes:
        tree.insert('', END, values=(clube["id"],clube["nome"], clube["foto"], clube["divisao"], clube["destaque"]))
      nome.set("")  

    def filtro():
      ttk.Label(filterframe, text="Nome do Clube: ").grid(column=0, row=1, sticky=W)
      ttk.Entry(filterframe, width=20, textvariable=nome).grid(column=0, row=2, sticky=W)

      def filtrar():
        limpa()
        for clube in clubes:
          if (clube["nome"] == nome.get()):
            tree.insert('', END, values=(clube["id"], clube["nome"], clube["divisao"], clube["destaque"]))

        if len(tree.get_children()) == 0:
          showinfo(title="Atenção",
                  message=f"Não há clubes com o nome {nome.get()}")
          exibir_todos()        

      ttk.Button(filterframe, text="Filtar", command=filtrar).grid(column=1, row=2, sticky=W)    
      ttk.Button(filterframe, text="Todos", command=exibir_todos).grid(column=2, row=2, sticky=W)

    filtro()

    # ------------------------------------------ Ordenações
    orderframe = ttk.Frame(filter_order_frame)
    orderframe.grid(row=0, column=1)

    def ordem():
      ttk.Label(orderframe, text="Selecione a ordem desejada").grid(column=0, columnspan=3, row=0, sticky=W)

      order = StringVar()
      order.set("id")
      ttk.Radiobutton(orderframe, text='Código', variable=order, value='id').grid(column=0, row=1, sticky=W)
      ttk.Radiobutton(orderframe, text='nome', variable=order, value='nome').grid(column=1, row=1, sticky=W)
      ttk.Radiobutton(orderframe, text='destaque', variable=order, value='destaque').grid(column=2, row=1, sticky=W)

      def ordenar():
        global clubes
        if order.get() == "id":
          clubes = sorted(clubes, key=lambda club: club['id'], reverse=True) 
        elif order.get() == "nome":
          clubes = sorted(clubes, key=lambda club: club['nome']) 
        elif order.get() == "destaque":  
          clubes = sorted(clubes, key=lambda club: club['destaque']) 

        exibir_todos()

      ttk.Button(orderframe, text="Ordenar", command=ordenar).grid(column=3, row=1, sticky=W)

    ordem()
    
    return gridframe



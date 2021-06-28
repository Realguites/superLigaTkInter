import tkinter as tk
from tkinter import ttk

from telas import inclusao
from telas import listagem
from telas import controle_clubes
from telas import estatistica


# root window
root = tk.Tk()
root.geometry('680x600+60+60')
root.title('Super Liga')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=2, expand=True)

# create frames
frame1 = inclusao.monta_formulario(notebook)
frame2 = listagem.monta_grid(notebook)
frame3 = controle_clubes.monta_grid_divisao(notebook)
frame4 = estatistica.monta_labels(notebook)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)


# add frames to notebook

notebook.add(frame1, text='Inclusão de clubes')
notebook.add(frame2, text='Listagem de clubes')
notebook.add(frame3, text='Controle de clubes')
notebook.add(frame4, text='Estatísticas')


root.mainloop()
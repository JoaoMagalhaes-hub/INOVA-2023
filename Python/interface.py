import tkinter as tk
from tkinter import ttk

def exibir_mensagem():
    nome = nome_entry.get()
    mensagem_label['text'] = 'Seja Bem vindo(a), ' + nome

root = tk.Tk()
root.title('Inova Uniesp')
fonte = ('Arial', 10)

nome_label = ttk.Label(root, text='Nome:', font=fonte)
nome_entry = ttk.Entry(root, font=fonte,width=30)
nome_label.grid(row=0, column=0, padx=10,pady=5)
nome_entry.grid(row=0, column=1, padx=10, pady=5)
mensagem_label = ttk.Label(root, text='Digite o seu nome!', font= fonte)
mensagem_label.grid(row=2, column=0, columnspan=2, pady=5)

root.geometry('300x300')
root.configure(bg='azure')
botao = ttk.Button(root, text='Clique aqui!', command=exibir_mensagem)
botao.grid(row=1, column=0, columnspan=2, padx=5, pady=10)












root.mainloop()
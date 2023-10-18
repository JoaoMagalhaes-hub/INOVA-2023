import tkinter as tk
from tkinter import ttk


def calcular_imc(peso, altura):
    imc = peso / (altura **2)
    return imc

def cadastrar_pessoa():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    imc = calcular_imc(peso, altura)
    #classificacao_label= exibir_classificacao_imc(imc)
    resultado_label.config(text=f'Nome: {nome} \n Idade: {idade} \n Peso: {peso}, kg \n Altura: {altura} \n IMC: {imc:.2f}')


    


root = tk.Tk()
root.title('Inova Uniesp')
fonte = ('Arial', 10)


nome_label = ttk.Label(root, text='Nome:', font=fonte)
nome_entry = ttk.Entry(root, font=fonte,width=30)
nome_entry.grid(row=0, column=1, padx=10, pady=5)
nome_label.grid(row=0, column=0, padx=10,pady=5)

idade_label = ttk.Label(root, text='Idade:', font=fonte)
idade_entry = ttk.Entry(root, font=fonte,width=30)
idade_entry.grid(row=1, column=1, padx=10, pady=5)
idade_label.grid(row=1, column=0, padx=10,pady=5)

peso_label = ttk.Label(root, text='Peso (kg):', font=fonte)
peso_entry = ttk.Entry(root, font=fonte,width=30)
peso_entry.grid(row=2, column=1, padx=10, pady=5)
peso_label.grid(row=2, column=0, padx=10,pady=5)

altura_label = ttk.Label(root, text='Altura (m):', font=fonte)
altura_entry = ttk.Entry(root, font=fonte,width=30)
altura_entry.grid(row=3, column=1, padx=10, pady=5)
altura_label.grid(row=3, column=0, padx=10,pady=5)

mensagem_label = ttk.Label(root, text='Calcule seu IMC!', font= fonte)
mensagem_label.grid(row=5, column=0, columnspan=2, pady=5)


root.geometry('300x300')
root.configure(bg='azure')
botao = ttk.Button(root, text='Clique aqui!', command=cadastrar_pessoa)
botao.grid(row=8, column=0, columnspan=2, padx=5, pady=10)
resultado_label = ttk.Label(root, text='')
classificacao_label = ttk.Label(root, text='')
resultado_label.grid(row=6, column=0, columnspan=2, pady=5)
classificacao_label.grid(row=7, column=0, columnspan=2, pady=5 )

root.mainloop()
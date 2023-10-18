#Tkinter biblioteca gráfica
#as tk referencia os objetos e classes do módulo Tkinter
import tkinter as tk
#themed Tkinter, é um conjuntos de widgets (elementos de interface)
from tkinter import ttk
#Cria a janela principazl
root = tk.Tk()
root.title('Inova Uniesp')
#Cria os widgets
nome_label = ttk.Label(root, text= 'Olá Senhoras e Senhores:', font=('Arial', 12, 'bold'), foreground='blue')
#Ajusta a posição Geometricamente na tela
nome_label.pack(padx= 20, pady=20)
#Código deve fiar abaixo # Cria a janela principal
#Define o tamanho da janela 
root.geometry('500x500')
#Define a cor de fundo da janela
root.configure(bg='azure')
#Cria os widgets
#nome_label = ttk.Label(root, text='Olá', font=('Arial', 12, 'bold'), foreground='blue')
root.mainloop()
from random import *
from tkinter import *

def nome():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    classe = int(input('''Qual sua classe?\n 
                       [ 1 ] Mago\n 
                       [ 2 ] Ladino\n 
                       [ 3 ] Necromante\n 
                       [ 4 ] Cavaleiro\n 
                       [ 5 ] Arqueiro\n 
                       [ 6 ] Bardo\n 
                       [ 7 ] Feitiçeiro\n
                       [ 8 ] Bruxo'''))
    caracteres = int(input('Quantos caractéres seu nome terá? '))






tela = Tk()
tela.title('Gerador de nomes RPG')
tela.geometry('800x600')


tela.mainloop()